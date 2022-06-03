from django.urls import path
from store.views import(
    home,
    store_home,
    DepartmentListView,
    department_detail_view,
    CategoryListView,
    category_detail_view,
    StoreProductListView,
    StoreProductDetailView
)

from store.views import *


urlpatterns = [
    path('',home, name='home'),
    #about_us
    path('about/',about_us, name='about_us'),
    #all_blog
    path('all-blog/',all_blog, name='all_blog'),
    #all_product
    path('all-product/',all_product, name='all_product'),
    #blog
    path('blog/',blog, name='blog'),
    #cart
    path('cart/',cart, name='cart'),
    #contact
    path('contact/',contact, name='contact'),
    #crystal_directory
    path('crystal-directory/',crystal_directory, name='crystal_directory'),
    #order_history
    path('order-history/',order_history, name='order_history'),
    #single_blog
    path('single-blog/',single_blog, name='single_blog'),
    #single_category
    path('single-category/',single_category, name='single_category'),
    #single_product
    path('single-product/',single_product, name='single_product'),
    #single_department
    path('single-department/',single_department, name='single_department'),
    path('<slug:store_slug>/',store_home,name='store-home'),
    path('<slug:store_slug>/product/',StoreProductListView.as_view(),name='store-product-list'),
    path('store/product/<int:pk>/', StoreProductDetailView.as_view(),name='store-product-detail'),
    path('shop/department/', DepartmentListView.as_view(),name='department-list'),
    path('shop/department/<slug:dept_slug>/',department_detail_view,name='department-detail'),
    path('shop/category/', CategoryListView.as_view(),name='category-list'),
    path('shop/category/<slug:cat_slug>/',category_detail_view,name='category-detail'),
  
]
