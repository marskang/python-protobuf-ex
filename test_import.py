# -*- coding: utf-8 -*-

import message_pb2
import player_pb2

#player =  player_pb2.Player()


msg = message_pb2.Message()

player = msg.player

player.id = 1
player.name = '张三'


msg.content = 'hello world'

data = msg.SerializeToString()

m = message_pb2.Message()

m.ParseFromString(data)

print m.content
print m.player.id
print m.player.name
