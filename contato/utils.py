# -*- coding: utf8 -*-

from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


def enviar_email(from_email, to, name, subject, template, tags):
    """Envia o email com o email do destinatário
    assunto e mensagem, renderizando-o usando a partir
    de um arquivo separado
    """

    # Gera a mensagem
    message = render_to_string(template, tags)

    # Envia a mensagem
    send_mail(subject=settings.EMAIL_SUBJECT_PREFIX + " " + subject,
        message=message,
        from_email=from_email,
        recipient_list=[to])
