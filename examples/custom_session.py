import sys
import configparser
from socialvoidpy import SocialvoidClient

config = configparser.ConfigParser()
config.read("session.ini")
sv = SocialvoidClient()
try:
    # Could be safer but this is an example
    try:
        session_challenge = sys.argv[1]
    except IndexError:
        session_challenge = None

    if session_challenge is None:
        sv.session.create("Fridgevoid", "1.0.1", "Samsung Smart Fridge")
        config["public_hash"] = sv.session.public_hash
        config["private_hash"] = sv.session.private_hash
        config["session_id"] = sv.session.session_id
        with open("session.ini", "w+") as file:
            config.write(file)
        print(
            "Session challenge (keep it safe! use by passing as an argument):",
            sv.session.session_challenge,
        )
    else:
        sv.session.public_hash = config["public_hash"]
        sv.session.private_hash = config["private_hash"]
        sv.session.session_id = config["session_id"]
        sv.session.session_challenge = session_challenge
        sv.session.session_exists = True
finally:
    sv.close()
