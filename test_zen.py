"""

import zenora
import test_config
import datetime

api = zenora.RESTAPI(test_config.token, "Bot")

resp = api.leave_guild(652717519848603658)


print(resp)
"""
