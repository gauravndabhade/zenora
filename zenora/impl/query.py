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
from zenora.utils.helpers import fetch, error_checker
from zenora.utils.endpoints import *


class Query:
    __slots__ = ["token", "token_type"]

    def __init__(self, token: str, token_type: str):
        self.token = token
        self.token_type = token_type

    def channel(self, snowflake: int) -> typing.Dict:
        """Implementation for the REST API query to get channels.

        Parameters:
        snowflake: int
                The channel ID of a Discord channel

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """
        data = fetch(
            BASE_URL + FETCH_CHANNEL.format(snowflake),
            headers={"Authorization": f"{self.token_type} {self.token}"},
        )
        error_checker(data)
        return data

    def user(self, snowflake: int) -> typing.Dict:
        """Implementation for the REST API query to get user.

        Parameters:
        snowflake: int
                The channel ID of a Discord channel

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """
        data = fetch(
            BASE_URL + FETCH_USER.format(snowflake),
            headers={"Authorization": f"{self.token_type} {self.token}"},
        )
        error_checker(data)
        return data

    def current_user(self) -> typing.Dict:
        """Implementation for the REST API query to get current user.

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """
        data = fetch(
            BASE_URL + FETCH_CURRENT_USER,
            headers={"Authorization": f"{self.token_type} {self.token}"},
        )
        return data