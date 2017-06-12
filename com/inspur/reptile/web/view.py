#from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    content={}
    content["hello"]="Hello Guest!"
    content["name"]="xiaxue"
    content["grade"]=[1,2,3,4]
    return render(request,"hello.html",content)
    #return HttpResponse("hello world!"+request[0])

def test(a,b,**c):
    print(a)
    print(b)
    print(c)
if __name__ == '__main__':
    test(1,2,d=3,e=4)