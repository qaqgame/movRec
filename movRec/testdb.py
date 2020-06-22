from django.http import HttpResponse
from TestModel.models import Test


# operate database
def testdb(request):
    test1 = Test(name='haha')
    test1.save()
    return HttpResponse("<p>数据添加成功</p>")