# Zenora, a modern Python API wrapper for the Discord REST API
#
# Copyright (c) 2020 K.M Ahnaf Zamil
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import typing


class Emoji:

    """A server emoji object

    :return: Zenora Guild Emoji object
    :rtype: zenora.emojis.Emoji
    """

    __slots__ = ["data", "app"]

    def __init__(self, data: typing.Dict, app):
        self.data = data
        self.app = app

    @property
    def id(self) -> typing.Optional[int]:
        """Returns the snowflake ID of the emoji."""
        return int(self.data["id"])

    @property
    def name(self) -> typing.Optional[str]:
        """Returns name of the emoji."""
        return self.data["name"]

    @property
    def roles(self) -> typing.Optional[typing.List[int]]:
        """Returns the roles this emoji is whitelisted to"""
        return self.data["roles"]

    @property
    def user(self) -> typing.Optional[str]:
        """Returns the user that created this emoji"""
        if "user" in self.data:
            return self.data["user"]
        return None

    @property
    def require_colons(self) -> typing.Optional[bool]:
        """Returens whether this emoji must be wrapped in colons"""
        return self.data["require_colons"]

    @property
    def managed(self) -> typing.Optional[bool]:
        """Returens whether this emoji is managed"""
        return self.data["managed"]

    @property
    def animated(self) -> typing.Optional[bool]:
        """Returens whether this emoji can be used, may be false due to loss of Server Boosts"""
        return self.data["animated"]

    def __str__(self):
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("name", self.name),
            ("roles", self.roles),
            ("user", self.user),
            ("require_colons", self.require_colons),
            ("managed", self.managed),
            ("animated", self.animated),
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join("%s=%r," % i for i in attrs),
        )
