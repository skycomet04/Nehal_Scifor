from django.urls import path
from . import views
urlpatterns=[
    path('fetch_data',views.SaveData.as_view(),name='fetch_data'),
    path('display_data',views.viewStock.as_view(),name='display_data')
]
