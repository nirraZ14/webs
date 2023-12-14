from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("service/<int:id>", views.service, name="service"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("blog", views.blog, name="blog"),
    path("about", views.about, name="about"),

]