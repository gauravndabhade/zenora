import zenora
import testconfig

api = zenora.RESTAPI(token=testconfig.token, token_type="Bot")

channel = api.get_channel(testconfig.channel_id)


print(channel)

print(channel.delete())
