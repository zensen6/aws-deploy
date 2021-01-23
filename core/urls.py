from django.urls import path
from users.views import InputLottery, LoginView, log_out, SignUpView
app_name = "core"


urlpatterns = [
    path('', InputLottery.as_view(), name="gallery"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/',log_out, name="logout"),
    path('signup/', SignUpView.as_view(), name="signup"),
]
