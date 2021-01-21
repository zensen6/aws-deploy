from django.urls import path
from users.views import InputLottery
app_name = "core"


urlpatterns = [
    path("", InputLottery.as_view(), name="lottery"),
]
