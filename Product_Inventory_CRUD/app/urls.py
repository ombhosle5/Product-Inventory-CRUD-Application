from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_view, name='product_view'),
    path("view/",views.product_list , name='product_list'),
    path('create/', views.create_product, name='create_product'),
    path('<int:pk>/update/', views.update_product, name='update_product'),
    path('<int:pk>/delete/', views.delete_product , name='delete_product'),

]
