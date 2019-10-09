from twilio.rest import Client

class TwilioProvider():
    @classmethod
    def send_messagge (number):
        account_sid = ''
        auth_token = ''
        client = Client(account_sid, auth_token)
        message = client.messages \
                .create(
                     body="Este es un pinche aviso culero y urgentex",
                     from_='+16788661949',
                     to='+524612180322')
        return message.sid
