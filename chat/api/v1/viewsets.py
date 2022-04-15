from rest_framework.views import APIView
from rest_framework.response import Response
from chat.api.v1.serializers import ChatSerializer
from chat.models import Chat
from products.models import Post
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class ChatView(APIView):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, post_id=None, buyer_id=None):
        if post_id is not None and buyer_id is not None:
            chats = Chat.objects.filter(post_id=post_id, buyer_id=buyer_id)
            serializer = self.serializer_class(chats, many=True)
            return Response({'response': serializer.data}, status=status.HTTP_200_OK)
        return Response({'response': 'There is missing something'})

    def post(self, request, post_id=None, buyer_id=None):
        serializer = self.serializer_class(data=request.data)
        post_id = Post.objects.get(id=post_id)
        buyer_id = User.objects.get(id=buyer_id)
        if serializer.is_valid(raise_exception=True):
            chats = Chat(post=post_id, buyer=buyer_id, message=serializer.validated_data['message'],
                         image=serializer.validated_data['image'])
            chats.save()
            return Response({'response': "message sent"}, status=status.HTTP_201_CREATED)
        return Response({'response': 'There is something wrong'})
