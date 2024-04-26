from django.urls import path
from . import views
from .views import Userregisterview

urlpatterns=[
    path('', views.index, name='index'),
    path('del/<str:item_id>', views.remove, name="del"),
    path('updateitem/<int:tid>',views.updateitem,name='updateitem'),
    path('register',Userregisterview.as_view(),name='register'),
    path('login/',views.log_in,name='log_in'),
    path('logout',views.log_out,name='logout')
]
