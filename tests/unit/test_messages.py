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

# DOES NOT WORK IF pip uninstall zenora
# asd asdasd  adasdasd
import zenora
import unittest

api = zenora.RESTAPI("Token", "Bearer", testing=True)


class TestRESTAPI(unittest.TestCase):

    # Just trying Travis CI
    def setUp(self):
        """Setting up the data that will be used to check the values from the API mock"""
        self.id = 756739983158673418
        self.type = 0
        self.attachments = []
        self.content = "i forgot"
        self.author = {"id": 479287754400989217, "username": "Ahnaf"}

    def test_get_message(self):
        """Testing the get_channel method with specific ID and expected data

        Note: Make sure the ID is of a server text channel because we are mocking an API response with a guild text channel response.
        """
        print(api.get_current_user())
        channel = api.get_channel(753859569859690509)
        msg = channel.get_message(756739983158673418)
        print(msg)
        print(msg.channel)
        self.assertEqual(msg.content, self.content)
        self.assertEqual(msg.id, self.id)
        self.assertEqual(msg.author.username, self.author["username"])
        self.assertEqual(msg.attachments, self.attachments)


if __name__ == "__main__":
    unittest.main()
