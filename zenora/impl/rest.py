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
import zenora
from zenora.base.rest import RESTAPI as REST
from zenora.impl.factory import Factory as model_factory
from zenora.impl.query import Query


class RESTAPI(REST):

    __slots__ = ["token", "token_type"]

    def __init__(self, token: str, token_type: str) -> None:
        self.token = token
        self.token_type = token_type

    def get_channel(self, snowflake: int) -> typing.Any:
        """Fetch Dicord Channel

        This has to be the channel snowflake ID


        Parameters
        ----------

        snowflake: int
                The channel ID of the specific channel you want to fetch

        Returns
        -------
        zenora.channels.GuildTextChannel
                Zenora guild text channel object

        zenora.channels.GuildVoiceChannel
                Zenora guild voice channel object

        zenora.channels.DMTextChannel
                Zenora DM text channel object
        """
        response = Query(self.token, self.token_type).channel(snowflake)
        return model_factory.parse_channel(response=response, app=self)

    def get_user(self, snowflake: int) -> typing.Any:
        """Fetch Dicord User

        This has to be the user's snowflake ID


        Parameters
        ----------

        snowflake: int
                The ID of the Discord User

        Returns
        -------
        zenora.users.User
                Zenora user object

        """
        response = Query(self.token, self.token_type).user(snowflake)
        return model_factory.parse_user(response=response, app=self)

    def get_current_user(self) -> typing.Any:
        """Fetch the current Dicord User


        Returns
        -------
        zenora.users.User
                Zenora user object

        """
        response = Query(self.token, self.token_type).current_user()
        return model_factory.parse_user(response=response, app=self)

    def modify_current_user(self, args: dict) -> typing.Any:
        """Modify current discord User


        Parameters
        ----------
        args: typing.Dict
                A dictionary containing the changes to the current user. This has to be either
                their username, avatar or both

        Example
        -------
        ```py
        >>> some_api_instance.modify_current_user({'username' : 'FroggyMan', 'avatar' : 'https://cdn.discordapp.com/avatars/753561575532658738/0cf89f88a3ba4e226c6f1c72a9242dd8.png'})

            User(id=753561575532658738, username=Zenora, discriminator=6423, avatar_url=https://cdn.discordapp.com/avatars/753561575532658738/380c68e7a6752e347ed875c2e11a05c4.png?size=1024,
            flags=0, mention=<@753561575532658738>, bot=True, mfa_enabled=True, locale=en-US, verified=True,)
        ```

        Returns
        -------
        zenora.users.User
                Zenora user object

        """
        if "avatar" in args:
            args["avatar"] = zenora.File(args["avatar"]).data
        response = Query(self.token, self.token_type).modify_me(args)
        return model_factory.parse_user(response=response, app=self)

    def leave_guild(self, snowflake: int) -> typing.Optional[None]:
        """Leave a Discord server (current user)

        Parameters
        ----------

        snowflake: int
                The ID of the Discord Server

        Returns
        -------
        code: int
            Code for response status. Will return 204 on success

        """

        response = Query(self.token, self.token_type).leave_guild(snowflake)
        return response