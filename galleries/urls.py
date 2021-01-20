from django.urls import path
from . import views as view

app_name="galleries"

urlpatterns = [
    path("<int:pk>/", view.GalleryView.as_view(), name="detail"),
    path("search/", view.SearchView, name="search"),
    path("login/", view.LoginView.as_view(), name="login"),
    path("logout/", view.log_out, name="logout"),
]