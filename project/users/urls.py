from django.conf.urls import url
from . import views
from users.views import Welcome, Login_, Create_user, Register

urlpatterns = [
	url(r'^$', Welcome.as_view(), name='welcome'),
	url(r'^login$', Login_.as_view(), name='login'),
	url(r'^register$', Register.as_view(), name='register'),
	url(r'^create_user$', Create_user.as_view(), name='login'),

]
