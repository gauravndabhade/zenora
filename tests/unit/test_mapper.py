import zenora
from zenora.impl.mapper import ChannelMapper
import unittest


class testChannelMapper(unittest.TestCase):

    # Just trying Travis CI
    def setUp(self):
        """Setting up the data that will be used to check the values from the API mock"""
        self.response = {
            "id": "753859569859690509",
            "last_message_id": "754623102561812511",
            "type": 0,
            "name": "general",
            "position": 4,
            "parent_id": "753859569859690506",
            "topic": None,
            "guild_id": "753859568764977194",
            "permission_overwrites": [],
            "nsfw": False,
            "rate_limit_per_user": 0,
        }
        self.app = {}

    def test_map(self):
        c = ChannelMapper.map(self.response, self.app)
        self.assertTrue(int(c.id) == int(self.response["id"]))


if __name__ == "__main__":
    unittest.main()
