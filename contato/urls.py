from django.conf.urls import url
from contato.views import ContatoSuccess,form


urlpatterns =[
    url(r'^contato/$', form, name='contato_form'),

    url(r'^contato/sucesso/$', ContatoSuccess.as_view(), name='contato_success'),
]
