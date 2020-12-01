from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='web'

urlpatterns=[
	path('', views.main, name='main'),
	path('<str:page>', views.menu, name='menu'),
	path('<str:page>/<int:post_pk>', views.detail_post, name='detail_post'),
	path('<str:page>/<int:post_pk>/<str:name>/input', views.input_information_post_password, name='input_information_post_password'),
	path('<str:page>/<int:post_pk>/<str:name>', views.edit_information, name='edit_information'),
	path('<str:page>/new', views.new_information_post, name='new_information_post'),
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
