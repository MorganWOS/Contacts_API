from django.urls import path
from . import views


app_name = 'contacts'

urlpatterns = [
    path('contacts/', views.contact_list),
    path('contacts/<int:pk>/', views.contact_detail),
]
