from channels.consumer import AsyncConsumer, SyncConsumer
from asgiref.sync import async_to_sync
import json

from channels.exceptions import StopConsumer

from products.models import Chat, Group


class MySyncConsumerDynamicGroup(SyncConsumer):

    def websocket_connect(self, event):
        self.group_name=self.scope['url_route']['kwargs']['groupName']
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.send({
            "type": "websocket.accept"
        })

    def websocket_receive(self, event):
        print(event)
        # data = json.loads(event['text'])
        data = event['text']
        group = Group.objects.get(name=self.group_name)
        chat = Chat(content=data, group=group)
        chat.save()
        # self.send({
        #     "type": "websocket.send",
        #     "text": data,
        # })
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'chat.message',
                'text': event['text']
            })

    def chat_message(self, event):
        print(event)
        self.send({
            'type': 'websocket.send',
            'text': event['text']
        })

    def websocket_disconnect(self, event):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )
        print("Websocket Disconnected", event)
        raise StopConsumer
