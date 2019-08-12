from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^regist/', views.regist, name='regist'),
    url(r'^userlist/', views.userlist, name='userlist'),
    url(r'^delete/', views.delete, name='delete'),
    url(r'^toadd/', views.toadd, name='toadd'),
    url(r'^add/', views.add, name='add'),
    url(r'^toupdate/', views.toupdate, name='toupdate'),
    url(r'^update/', views.update, name='update'),
    url(r'^chaxun/',views.chaxun,name='chaxun'),
    # 路由参数
    url(r'^testroute/(\d+)/',views.testroute),
]
