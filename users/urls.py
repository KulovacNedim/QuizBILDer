from django.urls import path
from .views import RegisterView, UserInfo

app_name = 'users'

urlpatterns = [
    path('', UserInfo.as_view(), name="loggedin_user"),
    path('create/', RegisterView.as_view(), name="create_user"),
]