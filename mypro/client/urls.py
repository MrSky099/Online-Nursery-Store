from django.urls import path
from . import views
urlpatterns = [
    # path('client_header/',views.client_header),
    path('home/',views.home),
    path('register/',views.register),
    path('login/',views.login),
    path('logout/',views.logout),
    path('about/',views.about),
    path('contact/',views.contact),
    path('portfolio/',views.portfolio),
    path('shop/',views.shop),
    path('cart/',views.cart),
    path('add_to_cart/',views.add_to_cart),
    path('checkout/',views.checkout),
    path('shop_details/<int:id>/',views.shop_details),
    path('cart_del/<int:id>/',views.cart_del),
    path('order_summary/',views.order_summary),
]
