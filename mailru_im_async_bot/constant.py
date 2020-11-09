from enum import Enum, unique


@unique
class Parts(Enum):
    FILE = "file"
    STICKER = "sticker"
    MENTION = "mention"
    VOICE = "voice"
    FORWARD = "forward"
    REPLY = "reply"


@unique
class PayLoadFileType(Enum):
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"


@unique
class ChatType(Enum):
    PRIVATE = "private"
    GROUP = "group"
    CHANNEL = "channel"

