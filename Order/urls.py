from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("login", views.login_view, name="login"),
	path("sign_up", views.sign_up, name="sign_up"),
	path("order", views.order, name="order"),
	path("logout", views.logout_view, name="logout")
]

urlpatterns += staticfiles_urlpatterns()