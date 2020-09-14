import zenora
import test_config
import datetime

api = zenora.RESTAPI(
    "mfa.VH-D78ma0QrwyfZN7E_ahn7galRBqs5DKV9ZPQ4RvZs4JiiSLbtdiJoY2BneqqJrlCW_-4tdhz60Fz4vSC3b"
)

resp = api.get_current_user()

print(resp)