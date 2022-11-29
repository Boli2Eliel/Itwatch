from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:id>/', views.staff_detail, name='dashboard-staff-detail'),
    path('product/', views.product, name='dashboard-product'),
    path('update_items/<int:id>/', views.update_items, name='dashboard-updatedata'),
    path('delete_item/<int:id>', views.delete_item, name='deleteitem'),
    path('order/', views.order, name='dashboard-order'),

]