import typing
import datetime


class GuildTextChannel:

    __slots__ = ['data']

    def __init__(self, data) -> None:
        self.data = data

    @property
    def id(self) -> typing.Optional[int]:
        """Returns The snowflake ID of the channel."""
        return self.data['id']

    @property
    def name(self) -> typing.Optional[str]:
        """Returns the name of the channel."""
        return self.data['name']

    @property
    def position(self) -> typing.Optional[int]:
        """Returns the position of the channel."""
        return self.data['position']

    @property
    def guild_id(self) -> typing.Optional[int]:
        """Returns the snowflake ID of the channel's guild."""
        return self.data['guild_id']

    @property
    def topic(self) -> typing.Optional[str]:
        """Returns the topic of the channel."""
        return self.data['topic']

    @property
    def is_nsfw(self) -> typing.Optional[bool]:
        """Returns the name of the channel."""
        return self.data['nsfw']

    @property
    def last_message_id(self) -> typing.Optional[int]:
        """Returns the snowflake ID of the last message of the channel."""
        return self.data['last_message_id']

    @property
    def rate_limit_per_user(self) -> datetime.timedelta:
        """Returns the rate limit per user of the channel."""
        return self.data['rate_limit_per_user']

    @property
    def permission_overwrites(self) -> datetime.timedelta:
        """Returns the permission overwrites of the channel."""
        return self.data['permission_overwrites']

    @property
    def parent_id(self) -> datetime.timedelta:
        """Returns the snowflake ID of the parant category of the channel."""
        return self.data['parent_id']

    def __str__(self):
        """String representation of the model."""
        return f"GuildTextChannel(id={self.id}, name={self.name}, position={self.position}, guild_id={self.guild_id}, topic={self.topic}, is_nsfw={self.is_nsfw}, last_message_id={self.last_message_id}, rate_limit_per_user={self.rate_limit_per_user}, permission_overwrites={self.permission_overwrites}, parent_id={self.parent_id})"
