import enum


class RelationshipType(enum.Enum):
    """
    Your relationship with another peer

    **Members:**

    - **NONE**
    - **FOLLOWING**: You're following the target peer
    - **FOLLOWS_YOU**: The peer follows you
    - **AWAITING_APPROVAL**: You or the target peer is awaiting approval to follow the other
    - **MUTUALLY_FOLLOWING**: Both you and the target peer follow eachother
    - **BLOCKED**: You blocked the target peer
    - **BLOCKED_YOU**: The target peer blocked you
    """

    NONE = "NONE"
    FOLLOWING = "FOLLOWING"
    FOLLOWS_YOU = "FOLLOWS_YOU"
    AWAITING_APPROVAL = "AWAITING_APPROVAL"
    MUTUALLY_FOLLOWING = "MUTUALLY_FOLLOWING"
    BLOCKED = "BLOCKED"
    BLOCKED_YOU = "BLOCKED_YOU"
