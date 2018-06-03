class MsgReq(object):

    def test(self, content):
        from pb import message_pb2
        from pb import header_pb2
        msg = message_pb2.Message()
        msg.ParseFromString(content)
        # print content
        # print '123'
        # header = header_pb2.Header()
        # header.ParseFromString(content)
        # print header.length
        print msg.player.id
        print msg.player.name
        print msg.content

