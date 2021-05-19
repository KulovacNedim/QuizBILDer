from django.urls import path
from .views import RegisterView

app_name = 'users'

urlpatterns = [
    path('create/', RegisterView.as_view(), name="create_user"),
]