import zenora
import testconfig

api = zenora.RESTAPI(token=testconfig.token, token_type="Bot")

channel = api.get_channel(755758557869244446)


print(channel)

print(channel.delete())
