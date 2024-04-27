from django.urls import path
from hospital import views
urlpatterns = [
    path('',views.log_in,name='log_in'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('createdoctor',views.createdoctor,name='createdoctor'),
    path('createpatient',views.createpatient,name='createpatient'),
    path('createappointment',views.createappointment,name='createappointment'),
    path('deletepatient/<int:pid>',views.deletepatient,name='deletepatient'),
    path('deletedoctor/<int:did>',views.deletedoctor,name='deletedoctor'),
    path('deleteappoint/<int:aid>',views.deleteappoint,name='deleteappoint'),
    path('app_detail/<int:aid>',views.app_detail,name='app_detail'),
    path('doctor_detail/<int:did>',views.doctor_detail,name='doctor_detail'),
    path('patient_detail/<int:pid>',views.patient_detail,name='patient_detail'),
    path('updatepatient/<int:pid>',views.update_patient,name='updatepatient'),
    path('updatedoctor/<int:did>',views.updatedoctor,name='updatedoctor'),
    path('viewdoctor',views.viewdoctor,name='viewdoctor'),
    path('viewreceipt/<int:id>',views.viewinvoice,name='viewreceipt'),
    path('viewpatient',views.viewpatient,name='viewpatient'),
    path('viewappointment',views.viewappointment,name='viewappointment'),
    path('deletereceipt/<int:id>',views.delete_receipt,name='deletereceipt'),
    path('receipt',views.invoices,name='receipt'),
    path('generatereceipt/<int:id>',views.generateinvoice,name='generatereceipt'),
    path('logout',views.log_out,name='logout')
]