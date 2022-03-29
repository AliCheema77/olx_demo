from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from rest_auth.registration.serializers import SocialLoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from users.api.v1.serializers import GoogleSocialLoginSerializer
from rest_auth.registration.views import SocialLoginView

User = get_user_model()


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = GoogleSocialLoginSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        response = super(GoogleLoginView, self).post(request, *args, **kwargs)
        serializer = GoogleSocialLoginSerializer(data=request.data)
        token = Token.objects.get(key=response.data['key'])
        user = User.objects.get(id=token.user_id)
        if serializer.initial_data:
            user.username = serializer.initial_data['username']
            user.image = serializer.initial_data['image']
            user.google_id = serializer.initial_data['google_id']
            user.save()
        return Response({'token': token.key, 'id': token.user_id, 'username': user.username,
                         "google_id": user.google_id, "image": user.image})


