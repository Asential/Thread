from django.urls import path
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("topic/<path:url>/<str:topic>/", views.topic, name="topic"),
    path("comment/<path:url>/<str:topic>/", views.comment, name="comment"),
    path("reply/<path:url>/<str:topic>/<id>/", views.reply, name="reply"),
    
]
