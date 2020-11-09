from enum import Enum, unique


@unique
class EventType(Enum):
    NEW_MESSAGE = "newMessage"
    EDITED_MESSAGE = "editedMessage"
    DELETED_MESSAGE = "deletedMessage"
    PINNED_MESSAGE = "pinnedMessage"
    UNPINNED_MESSAGE = "unpinnedMessage"
    NEW_CHAT_MEMBERS = "newChatMembers"
    LEFT_CHAT_MEMBERS = "leftChatMembers"
    CHANGED_CHAT_INFO = "changedChatInfo"
    CALLBACK_QUERY = "callbackQuery"


class Event:
    def __init__(self, id, type_, data):

        self.id = id
        self.type = type_
        self.data = data

        if type_ == EventType.NEW_MESSAGE:
            self.text = data.get('text', '')
            self.from_chat = data['chat']['chatId']
            self.message_author = data['from']

    def __repr__(self):
        return "Event(id='{self.id}', type='{self.type}', data='{self.data}')".format(self=self)
