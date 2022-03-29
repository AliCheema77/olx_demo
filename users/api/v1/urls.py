from django.urls import path
from users.api.v1.viewsets import GoogleLoginView


urlpatterns = [

    path('google/', GoogleLoginView.as_view(), name='google_login'),
]
