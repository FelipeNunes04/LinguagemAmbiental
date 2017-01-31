from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from appblog.views import PostListView, PostDetailView, Sobre

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', PostListView.as_view(), name = "listar-post"),
    url(r'^post/(?P<pk>\d+)/$',PostDetailView.as_view(), name = "detalhe-post"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^sobre/$', Sobre.as_view(), name = "sobre"),
    url(r'', include('contato.urls')),

]
