import uuid
import time

name = "test_name"
namespace = "test_namespace"

# print(uuid.uuid1() ) # 带参的方法参见Python Doc
# print(uuid.uuid3( namespace, name ))
# print(uuid.uuid4())
# print(uuid.uuid5( namespace, name ))

if __name__ == '__main__':
    t=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

    print (t)