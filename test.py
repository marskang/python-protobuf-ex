# -*- coding: utf-8 -*-

import person_pb2

per = person_pb2.person()

per.id = 2
per.name = 'hello world'
print per.SerializeToString()


# p1 = 


