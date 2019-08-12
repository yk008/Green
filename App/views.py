import datetime


from django.core.paginator import Paginator, Page
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App.models import Emp, User


def login(request):
    datanow = datetime.datetime.now()
    if request.method == 'GET':
        error_msg = request.session.get('error_msg')
        context = {
            'datanow':datanow,
            'error_msg':error_msg

        }
        request.session.flush()
        return render(request,'login.html',context=context)
    elif request.method == 'POST':
        # 获取login页面文本框里的name和password
        name = request.POST.get('name')
        password = request.POST.get('password')
        print(name,password)

        # 这返回的是一个<QuerySet>类型 就是个集合对象
        # 从数据库表中查询账号name 判断数据库中的name是否与页面中输入的name相等
        users = User.objects.filter(u_name=name)

        # 如果user大于0的话就是账号存在 然后就检测密码
        if users.count() > 0:
            # users返回的是一个queryset 集合对象 所以要加[0]
            # users[0]表示从数据库中查找第一个符合user的账号来判断与之对应的密码
            # 因为没做账号查重功能 所以可以注册相同的user
            if users[0].u_password == password:
                return redirect(reverse('app:userlist'))
            else:
                request.session['error_msg'] = '密码错误'
                return redirect(reverse('app:login'))
                # return HttpResponse('账号或密码错误')

        else:
            request.session['error_msg'] = '账号不存在'
            return redirect(reverse('app:login'))
            # return HttpResponse('账号或密码错误')

    return redirect(reverse('app:login'))

# django中文件的反向解析reverse('axf:login')
# return redirect(reverse('axf:login'))


def regist(request):
    if request.method == 'GET':
        return render(request, 'regist.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = User()

        user.u_name = name
        user.u_password = password

        user.save()

        return redirect(reverse('app:login'))

    return redirect(reverse('app:regist'))






def userlist(request):
    # 获取当前系统时间
    datanow = datetime.datetime.now()
    page = request.GET.get('page',1)
    per_page = request.GET.get('per_page',5)
    emps = Emp.objects.all()
    # name = Emp.objects.get('name')
    # Paginator对象 在django中  可以实现页码
    p = Paginator(object_list=emps,per_page=per_page)
    # 要遍历每一页的数据
    p_page = p.page(page)
    context={
        'p': p,
        'p_page': p_page,
        'datanow': datanow,
    }

    return render(request,'userlist.html',context=context)




def delete(request):
    id = request.GET.get('id')
    emp = Emp.objects.get(pk=id)
    emp.delete()
    return redirect(reverse('app:userlist'))


def toadd(request):
    return render(request,'add.html')


def add(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    salary = request.POST.get('salary')
    print(name,age,gender,salary)

    emp = Emp()
    emp.name = name
    emp.gender = gender
    emp.age = age
    emp.salary = salary
    emp.save()
    return redirect(reverse('app:userlist'))


def toupdate(request):
    datanow = datetime.datetime.now()
    id = request.GET.get('id')
    emp = Emp.objects.get(pk=id)
    context = {
        'emp':emp,
        'datanow':datanow,
    }
    print(id)
    return render(request,'update.html',context=context)


def update(request):
    id = request.POST.get('id')
    emp = Emp.objects.get(pk=id)

    name = request.POST.get('name')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    salary = request.POST.get('salary')

    emp.name = name
    emp.gender = gender
    emp.age = age
    emp.salary = salary
    emp.save()
    return redirect(reverse('app:userlist'))


def testroute(request,a):
    print(a)
    return HttpResponse('哈哈哈')


def chaxun(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    salary = request.POST.get('salary')
    print(name,gender,age,salary)

    users = Emp.objects.filter(Emp.name.__contains__("%" + name.strip() + "%") if name is not None else "%",
                             Emp.gender.__contains__("%" + gender.strip() + "%") if gender is not None else "%",
                             Emp.age.__gt__("%" + age.strip() + "%") if age is not None else "%",
                             Emp.salary.__gt__("%" + salary.strip() + "%") if salary is not None else "%")
    
    

    return redirect(reverse('app:userlist'),users=users)