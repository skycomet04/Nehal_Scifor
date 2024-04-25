from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="dashboard"),
    path('bookslot', views.bookingslot,name="bookslot"),
    path('addslot', views.addParkingSpace,name="addslot"),
    path('addvehicle', views.addVehicle,name="addvehicle"),
    path('availableslot', views.available_slots,name="availableslot"),
    path('av_bookslot/<int:sid>', views.bookingslot,name="av_bookslot"),
    path('viewvehicle', views.view_vehicles,name="viewvehicle"),
    path('viewparking', views.view_parkings,name="viewparking"),
    path('todayparking', views.todaybooking,name="todayparking"),
    path('viewspace', views.view_space,name="viewspace"),
    path('viewuser', views.view_user,name="viewuser"),
    path('generatepdf/<int:pid>', views.generate_pdf,name="generatepdf"),
    path('userdetail/<int:uid>', views.userdetail,name="userdetail"),
    path('parkdetail/<int:id>', views.parkingdetail,name="parkdetail"),
    path('spacedetail/<int:id>', views.spacedetail,name="spacedetail"),
    path('vehicledetail/<int:id>', views.vehicledetail,name="vehicledetail"),
    path('deleteparking/<int:pid>', views.deleteparking,name="deleteparking"),
    path('deletespace/<int:sid>', views.deletespace,name="deletespace"),
    path('deletevehicle/<int:vid>', views.deletevehicle,name="deletevehicle"),
    path('deleteuser/<int:uid>', views.deleteuser,name="deleteuser"),
    path('updateparking/<int:pid>', views.update_parking,name="updateparking"),
    path('updatespace/<int:sid>', views.update_space,name="updatespace"),
    path('updatevehicle/<int:vid>', views.update_vehicle,name="updatevehicle"),
    path('login',views.log_in,name="login"), 
    path('forgetpass',views.forget_password,name="forgetpass"), 
    path('register',views.register,name="register"),
    path('logout',views.log_out,name='logout')
]
