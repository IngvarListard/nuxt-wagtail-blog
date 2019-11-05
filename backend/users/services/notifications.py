from django.conf import settings
from django.core.mail import send_mail

from backend.core.service import Service


class SendUserPassword(Service):
    SUBJECT = 'Пароль Junior\'s Journey'
    HOST = settings.EMAIL_HOST_USER

    def __init__(self, email: str, password: str):
        self.password = password
        self.email = email

    def execute(self):
        message = (
            'Ваш новый пароль на ресурсе '
            'Junior\'s Journey: \n'
            f'<strong>{self.password}</strong>'
        )
        send_mail(self.SUBJECT, message, self.HOST, [self.email])
