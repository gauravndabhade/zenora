import zenora
import testconfig

api = zenora.RESTAPI(token=testconfig.token, token_type="Bot")

channel = api.get_channel(753859569859690509)


msg = channel.get_message(756748477316202626)
print("Message: ", msg)
print("Message Channel: ", msg.channel)
