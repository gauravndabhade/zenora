import zenora
import testconfig
import datetime

api = zenora.RESTAPI(
    "mfa.VH-D78ma0QrwyfZN7E_ahn7galRBqs5DKV9ZPQ4RvZs4JiiSLbtdiJoY2BneqqJrlCW_-4tdhz60Fz4vSC3b"
)

resp = api.create_dm(351794468870946827)

print(resp)
