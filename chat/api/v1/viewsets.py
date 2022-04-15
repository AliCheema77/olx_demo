from rest_framework.views import APIView
from rest_framework.response import Response
from chat.api.v1.serializers import ChatSerializer, ChatGroupSerializer
from chat.models import Chat, ChatGroup
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
        username = post_id.user.username
        post_title = post_id.ad_title
        if serializer.is_valid(raise_exception=True):
            if username is not None and post_title is not None:
                chat_group = ChatGroup.objects.filter(buyer=buyer_id, seller=post_id.user, post=post_id).first()
                if chat_group is None:
                    chat_group = ChatGroup(username=username, post_title=post_title, buyer=buyer_id,
                                           seller=post_id.user, seller_image=post_id.user.image, post=post_id)
                chat_group.last_message = serializer.validated_data['message']
                chat_group.save()
            chats = Chat(post=post_id, buyer=buyer_id, message=serializer.validated_data['message'],
                         image=serializer.validated_data['image'])
            chats.save()
            return Response({'response': "message sent"}, status=status.HTTP_201_CREATED)
        return Response({'response': 'There is something wrong'})

    def delete(self, request, post_id=None, buyer_id=None):
        chats = Chat.objects.filter(post_id=post_id, buyer_id=buyer_id)
        if chats is not None:
            for chat in chats:
                chat.delete()
        post_id = Post.objects.get(id=post_id)
        buyer_id = User.objects.get(id=buyer_id)
        username = post_id.user.username
        post_title = post_id.ad_title
        chat_group = ChatGroup.objects.get(username=username, post_title=post_title, buyer_id=buyer_id)
        if chat_group is not None:
            chat_group.delete()
        return Response({"response": "Chat deleted"})


class ChatGroupView(APIView):
    serializer_class = ChatGroupSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, buyer_id=None):
        if buyer_id is not None:
            buyer_group = ChatGroup.objects.filter(buyer_id=buyer_id)
            serializer = self.serializer_class(buyer_group, many=True)
            return Response({'response': serializer.data}, status=status.HTTP_200_OK)
        return Response({'response': 'Buyer is id is missing.'}, status=status.HTTP_400_BAD_REQUEST)


