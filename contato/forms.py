# -*- coding: utf8 -*-

from django import forms


class ContatoForm(forms.Form):
	nome = forms.CharField(
		label = "Nome",
		max_length = 100,
		widget = forms.TextInput(
			attrs = {
				'placeholder': 'Nome',
				'required': 'required',
				'class': 'form-control'
			}
		)
	)
	email = forms.EmailField(
		label = "Email",
		max_length = 100,
		widget = forms.TextInput(
			attrs = {
				'placeholder': 'Email',
				'required': 'required',
				'class': 'form-control'
			}
		)
	)
	assunto = forms.CharField(
		label = "Assunto",
		max_length = 80,
		widget = forms.TextInput(
			attrs = {
				'placeholder': 'Assunto',
				'required': 'required',
				'class': 'form-control'
			}
		)
	)
	mensagem = forms.CharField(
		label = "Mensagem",
		max_length = 200,
		widget = forms.Textarea(
			attrs = {
				'placeholder': 'Mensagem',
				'required': 'required',
				'class': 'form-control'
			}
		)
	)

