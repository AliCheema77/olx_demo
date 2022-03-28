from django.urls import path
from users.api.v1.viewsets import GoogleLogin


urlpatterns = [

    path('google/', GoogleLogin.as_view(), name='google_login'),
]
