from django.urls import path
from . import views

urlpatterns = [
    path('',views.showcase, name='showcase'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('about/', views.about, name='about'),
    #path('product/<int:producto_id>/', views.productDetails, name='details'),
    path('course/<int:course_id>/', views.courseDetails, name='details'),
    path('login/', views.auth_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.auth_logout, name='logout'),
    path('customer/<int:customer_id>/', views.profile, name='profile'),
    path('customer/update/profile/', views.create_update_profile, name='create_update_profile'),
    path('customerlist/', views.customer_list, name='customer_list'),
    path('customercreate/', views.customer_create, name='customer_create'),
    path('customerupdate/<int:customer_id>/', views.customer_update, name='customer_update'),
    path('customerdelete/<int:customer_id>/', views.customer_delete, name='customer_delete'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('tracking/', views.track_orders, name='track_orders'),
    path('tracking/<str:tracking_id>/', views.track_order, name='track_order'),
    path('review/<str:product_id>/', views.review_order, name='review_order'),
    path('orders/', views.view_orders, name='view_orders'),
    path('order/<int:product_id>/<int:order_id>/claim/', views.claim_product, name='claim_product'),
    path('add-to-cart/<int:course_id>/', views.add_to_cart, name='add_to_cart'),
    path('create_course/',views.create_course, name='createCourse'),
    path('edit_course/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
]

