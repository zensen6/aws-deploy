from django.urls import path
from users.views import InputLottery
app_name = "core"


urlpatterns = [
    path('gallery/', InputLottery.as_view(), name="gallery"),
]
