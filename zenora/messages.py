import typing
import datetime

"""
{'id': '756748477316202626', 'type': 0, 'content': 'change the branch', 'channel_id': '753859569859690509', 'author': {'id': '406882130577063956', 'username': 'Hjacobs', 'avatar': 'aa6fb65225a58726292323435512925d', 'discriminator': '9441', 'public_flags': 0}, 'attachments': [], 'embeds': [], 'mentions': [], 'mention_roles': [], 'pinned': False, 'mention_everyone': False, 'tts': False, 'timestamp': '2020-09-19T05:28:16.699000+00:00', 'edited_timestamp': None, 'flags': 0}

"""


class Message:

    __slots__ = ["data", "app"]

    def __init__(self, data: typing.Dict, app):
        self.data = data
        self.app = app

    @property
    def id(self):
        return int(self.data["id"])

    @property
    def type(self):
        return int(self.data["type"])

    @property
    def content(self):
        return self.data["content"]

    @property
    def channel(self):
        return self.app.get_channel(int(self.data["channel_id"]))

    def __str__(self):
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("type", self.type),
            ("content", self.content),
            ("channel", self.channel),
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join("%s=%r," % i for i in attrs),
        )
