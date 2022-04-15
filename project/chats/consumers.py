from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('Websocket Connected ...',event)
        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self,event):
        print('Message Received from Client ...',event)
        self.send({
            'type':'websocket.send',
            'text':'hi message from server'
        })

    def websocket_disconnect(self,event):
        print('Websocket Disconnected ...',event)
        raise StopConsumer()
