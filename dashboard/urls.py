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
    path('product_text/', views.product_text, name='product_text'),
    path('product_csv/', views.product_csv, name='dashboard-product_csv'),
    path('export_excel/', views.export_excel, name='dashboard-export_excel'),
    path('show_pdf/', views.show_pdf, name='dashboard-show_pdf'),
    path('export_pdf/', views.export_pdf, name='dashboard-export_pdf'),
    path('register/', views.register, name="user-register"),
    path('success/', views.success, name="success"),

]