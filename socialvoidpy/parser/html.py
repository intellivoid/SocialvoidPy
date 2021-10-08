import html
import typing
from html.parser import HTMLParser
from collections import defaultdict
from urllib.parse import quote, unquote, urlsplit
from ..types.text_entity import _TextEntity
from ..types.text_entity import *


def _unparse(
    text: str, entities: typing.List[_TextEntity], offset: int, length: int
) -> str:
    noffset = offset
    ntext = ""
    for i in entities:
        if offset >= i.length + i.offset:
            continue
        ntext += html.escape(text[offset : i.offset])
        nentities = [j for j in entities if i.offset + i.length >= j.offset and i != j]
        if nentities:
            atext = _unparse(text, nentities, i.offset, i.length)
        else:
            atext = html.escape(text[i.offset : i.offset + i.length])
        if i.type == "BOLD":
            ntext += f"<b>{atext}</b>"
        elif i.type == "ITALIC":
            ntext += f"<b>{atext}</b>"
        elif i.type == "CODE":
            ntext += f"<code>{atext}</code>"
        elif i.type == "STRIKE":
            ntext += f"<s>{atext}</s>"
        elif i.type == "UNDERLINE":
            ntext += f"<u>{atext}</u>"
        elif i.type == "URL":
            ntext += f'<a href="{html.escape(i.value)}">{atext}</a>'
        elif i.type == "MENTION":
            ntext += f'<a href="sv://peer/{quote(i.value)}">{atext}</a>'
        elif i.type == "HASHTAG":
            ntext += atext
        else:
            raise ValueError(f"Unknown text entity type: {i.type}")
        offset = i.offset + i.length
    return ntext + html.escape(text[offset : length + noffset])


def unparse(text: str, entities: typing.List[_TextEntity]) -> str:
    """
    Unparses text and entities into an HTML encoded string

    **Parameters:**

    - **text**: Raw text
    - **entities**: Entities (will be sorted, pass a copy if you don't want order to be changed)
    """

    entities.sort(key=lambda i: (i.offset, -i.length))
    return _unparse(text, entities, 0, len(text))


_ENDTAG_MAP = {
    "strong": "BOLD",
    "b": "BOLD",
    "em": "ITALIC",
    "i": "ITALIC",
    "u": "UNDERLINE",
    "del": "STRIKE",
    "s": "STRIKE",
    "code": "CODE",
    # No a because it can be URL or MENTION
}


class _EntityHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self._text = ""
        self._entities: typing.List[_TextEntity] = []
        # entity, offset, length, value
        self._building_entities: typing.DefaultDict[
            str,
            typing.List[_TextEntity, typing.Optional[int], int, typing.Optional[str]],
        ] = defaultdict(list)

    def handle_starttag(self, tag: str, attrs: typing.List[typing.Tuple[str, str]]):
        if tag in ("strong", "b"):
            self._building_entities["BOLD"].append([BoldTextEntity, None, 0, None])
        elif tag in ("em", "i"):
            self._building_entities["ITALIC"].append([ItalicTextEntity, None, 0, None])
        elif tag == "u":
            self._building_entities["UNDERLINE"].append(
                [UnderlineTextEntity, None, 0, None]
            )
        elif tag in ("del", "s"):
            self._building_entities["STRIKE"].append([StrikeTextEntity, None, 0, None])
        elif tag == "code":
            self._building_entities["CODE"].append([CodeTextEntity, None, 0, None])
        elif tag == "a":
            try:
                url = next(i[1] for i in attrs if i[0] == "href")
            except StopIteration:
                return
            self._building_entities["URL"].append([URLTextEntity, None, 0, url])

    def handle_data(self, data: str):
        data = html.unescape(data)
        for i in self._building_entities.values():
            for j in i:
                if j[1] is None:
                    j[1] = len(self._text)
                j[2] += len(data)
        self._text += data

    def handle_endtag(self, tag: str):
        if tag in _ENDTAG_MAP:
            entity = self._building_entities[_ENDTAG_MAP[tag]].pop()
            self._entities.append(entity[0](entity[1], entity[2], entity[3]))
        elif tag == "a":
            entity = self._building_entities["URL"].pop()
            parsed = urlsplit(entity[3])
            if (
                parsed.scheme == "sv"
                and parsed.netloc == "peer"
                and len(parsed.path) > 1
                and parsed.path[0] == "/"
            ):
                self._entities.append(
                    MentionTextEntity(entity[1], entity[2], parsed.path[1:])
                )
            else:
                self._entities.append(URLTextEntity(entity[1], entity[2], entity[3]))


def parse(text: str) -> typing.Tuple[str, typing.List[_TextEntity]]:
    """
    Parses an HTML encoded string into an unencoded string and its entities

    **Parameters:**

    - **text**: HTML encoded string to parse
    """

    parser = _EntityHTMLParser()
    parser.feed(text)
    parser.close()
    return parser._text, parser._entities
