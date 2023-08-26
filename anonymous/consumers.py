import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Messages

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('test')
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name  
        
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        print('test1')
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        print('test2')
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
    
        # If message is empty don't send it
        if not message: return

        # Sender
        username = self.scope["user"].username
        finalMessage = (username + ': ' + message)
        
        # Save message in database
        Messages.objects.create(room_name = self.room_name, message = finalMessage)
        
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": finalMessage}
        )

    # Receive message from room group
    def chat_message(self, event):
        print('test3')
        message = event["message"]
        username = self.scope["user"].username
        # Send message to WebSocket
        self.send(text_data=json.dumps({'message': message,
        "username": username}))