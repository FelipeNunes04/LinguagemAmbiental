from django.db import models

class Categoria(models.Model):
	nome = models.CharField(max_length = 100)

	def __str__(self):
		return self.nome

class Post(models.Model):
	titulo = models.CharField(max_length = 100)
	texto = models.TextField()
	criado = models.DateTimeField(auto_now = True)
	categoria = models.ForeignKey(Categoria)
	imagem = models.ImageField(upload_to = 'imagens')

	def __str__(self):
		return self.titulo
		
