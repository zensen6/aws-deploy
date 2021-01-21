from django.urls import path
from . import views as view

app_name="galleries"

urlpatterns = [
    path("search/", view.SearchView, name="search"),
    path("login/", view.LoginView.as_view(), name="login"),
    path("logout/", view.log_out, name="logout"),
]