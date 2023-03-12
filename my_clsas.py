class RemoteControl:
    def __init__(self, television, room) -> None:
        self.television = television
        self.room = room
    
    def forward_channel(self):
        print('Channel Forward')
    
    def back_channel(self):
        print('back channel')
        
    def escolher_channel(self, chanel):
        print('Change for channel: {}'.format(channel))

room_control = RemoteControl('samsung', 'room')
print(room_control.room)
print(room_control.television)
room_control.forward_channel()
room_control.escolher_channel(12)

room_control = RemoteControl('samsung','room')
print(room_control.room)
print(room_control.television)