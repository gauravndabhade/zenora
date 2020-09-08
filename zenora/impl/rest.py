import typing
from zenora.base.rest import RESTAPI as REST
#from zenora.utils.factory import factory as model_factory
from zenora.impl.query import Query


class RESTAPI(REST):

    __slots__ = ['token', 'token_type']

    def __init__(self, token: str, token_type: str) -> None:
        self.token = token
        self.token_type = token_type

    def get_channel(self, snowflake: int) -> None:
        """Fetch channels

        Parameters
        ----------

        snowflake: int
                The channel ID of the specific channel you want to fetch
        """
        response = Query(self.token, self.token_type).channel(snowflake)
        print(response)
        # return model_factory.parse_channel(response, snowflake)
