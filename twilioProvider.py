from twilio.rest import Client

class TwilioProvider():
    @classmethod
    def send_messagge (number):
        account_sid = 'ACba644bc2e547cc465bd41308af429c10'
        auth_token = '12e3a371e7472fc4523ccd85fc4f01eb'
        client = Client(account_sid, auth_token)
        message = client.messages \
                .create(
                     body="Este es un pinche aviso culero y urgentex",
                     from_='+16788661949',
                     to='+524612180322')
        return message.sid
        
TwilioProvider().send_messagge()
