from time import sleep
from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('Websocket Connected ...',event)
        print('Channel Layer ...',self.channel_layer)
        print('Channel name ...',self.channel_name)
        async_to_sync(self.channel_layer.group_add)('Programmers',self.channel_name)
        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self,event):
        print('Message Received from Client ...',event)
        async_to_sync(self.channel_layer.group_send)('Programmers',{
            'type':'chat.message',
            'message':event['text'],
        })
        # for i in range(20):
        #     self.send({
        #         'type':'websocket.send',
        #         'text': str(i)
        #     })
        #     sleep(1)

    def chat_message(self,event):
        print('Event ...',event)
        self.send({
            'type': 'websocket.send',
            'text':event['message'],
        })

    def websocket_disconnect(self,event):
        print('Websocket Disconnected ...',event)
        raise StopConsumer()
