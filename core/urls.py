from django.urls import path
from galleries.views import HomeView
from users.views import InputLottery
app_name = "core"


urlpatterns = [
    path("", HomeView.as_view(), name="front"),
    path("lottery/", InputLottery.as_view(), name="lottery"),
]
