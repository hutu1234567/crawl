# /usr/bin/python
# -*- coding:utf-8 -*-
from time import time

def logged(when):
    def log(flg,f,*args,**kargs):
        print( '''
            call %s:
                functions:%s
                args: %s kargs: %s'''
            % (flg,f,args,kargs)
        )
    def pre_logged(f):
        def wrapper(*args,**kargs):
            log("start",f,*args,**kargs)
            return f(*args,**kargs)
        return wrapper
    def post_logged(f):
        def wrapper(*args,**kargs):
            now = time()
            try:
                return f(*args,**kargs)
            finally:
                log("end",f,*args,**kargs)
                print ("time delta:%s" % (time()-now))
        return wrapper
    def round_logged(f):
        def wrapper(*args,**kargs):
            now = time()
            log("start",f,*args,**kargs)
            ret=object
            try:
                ret=f(*args,**kargs)
            finally:
                log("end", f, *args, **kargs )
                print ("time delta:%s" % (time()-now))
                return ret
        return wrapper
    try:
        return {"pre":pre_logged,"post":post_logged,"round":round_logged}[when]
    except KeyError as e:
        raise(ValueError(e),'must be "pre" or "post" or "round"')

    class a:
        def aa(self):
            self.__dict__.update()
#@logged("post")
@logged("round")
def hello(name):
    print("hello,",name)

if __name__ == '__main__':
    a="aaaa,bbbb,ccc"
    a1,a2,a3=a.split(",")
    print(a1,a2,a3)
    hello("world!")
'''
    等同于： hello = logged("post")(hello("world!"))
'''