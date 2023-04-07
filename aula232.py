from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, msg):
        self.msg = msg

    @abstractmethod
    def send(self) -> bool: ...


class SendSMS(Notification):
    def send(self) -> bool:
        print('Sending notification via SMS - ', self.msg)
        return True


class SendEmail(Notification):
    def send(self) -> bool:
        print('Sending notification via EMAIL - ', self.msg)
        return False


def alert(alert: Notification):
    notification_send = alert.send()

    if notification_send:
        print('Notification Ready')

    else:
        print('Notification ERROR')


test_sms = SendSMS('TEST SMS')
alert(test_sms)

test_email = SendEmail('TEST MAIL')
alert(test_email)
