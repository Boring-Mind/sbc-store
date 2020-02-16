"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path  # , include
from store.apps.pages import views

urlpatterns = [
    path('', views.home_page_view, name='index'),
    
    path('admin/', admin.site.urls, name='admin'),
    
    path('about/', views.about_view, name='about'),
    path('blog/', views.blog_view, name='blog'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('contact/', views.contact_view, name='contact'),
    path('faq/', views.faq_view, name='faq'),
    path('restore_password/', views.restore_password_view, name='restore_pswd'),
    path('login/', views.login_view, name='login'),
    path('account/', views.my_account_view, name='account'),
    path('register/', views.register_view, name='register'),
    path('service/', views.service_view, name='service'),
    path('shop/', views.shop_view, name='shop'),
    path('single_product/', views.single_product_view),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('404/', views.page_not_found_view),

    # path('site/', include('site.urls')),
]
