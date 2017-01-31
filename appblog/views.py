from django.conf import settings
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.core.mail import EmailMessage

from .models import Post

class PostListView(ListView):
	template_name = u'post/listar.html'
	paginate_by = 4

	def get_queryset(self):
		post = Post.objects.all().order_by('-criado')
		return post


class PostDetailView(DetailView):
	model = Post
	template_name = "post/detalhe.html"

class Sobre(TemplateView):
	template_name = "sobre.html"











