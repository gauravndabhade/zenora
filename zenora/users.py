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
from zenora.utils.endpoints import *
from zenora.errors import InvalidUser, InvalidSnowflake


class PartialUser:
    """A partial user object for API response that doesn't give full info about user.

    :return: Zenora partial user object
    :rtype: zenora.users.PartialUser
    """

    __slots__ = ["data"]

    def __init__(self, data) -> None:
        try:
            if data["code"] == 10013:
                raise InvalidUser("User with specified snowflake doesn't exist.")
        except KeyError:
            pass
        try:
            if "user_id" in data:
                raise InvalidSnowflake("Invalid snowflake ID.")
        except KeyError:
            pass
        self.data = data

    @property
    def id(self) -> typing.Optional[int]:
        """Returns The snowflake ID of the user."""
        return self.data["id"]

    @property
    def username(self) -> typing.Optional[str]:
        """Returns the username of the user."""
        return self.data["username"]

    @property
    def discriminator(self) -> typing.Optional[int]:
        """Returns the user's discriminator."""
        return self.data["discriminator"]

    @property
    def avatar_url(self) -> typing.Optional[str]:
        """Returns the user's avatar url"""
        return CDN_URL + AVATAR_URL.format(self.id, self.data["avatar"])

    @property
    def flags(self) -> typing.Optional[int]:
        """Returns the user's public flags """
        return self.data["public_flags"]

    def __str__(self) -> typing.Optional[str]:
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("username", self.username),
            ("discriminator", self.discriminator),
            ("avatar_url", self.avatar_url),
            ("flags", self.flags),
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join("%s=%r" % i for i in attrs),
        )
