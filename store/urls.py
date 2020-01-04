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
from django.urls import include, path
from store.apps.pages import views

urlpatterns = [
    path('', views.home_page_view),
    
    path('admin/', admin.site.urls),
    
    path('about/', views.about_view),
    path('blog/', views.blog_view),
    path('cart/', views.cart_view),
    path('checkout/', views.checkout_view),
    path('contact/', views.contact_view),
    path('faq/', views.faq_view),
    path('restore_password/', views.restore_password_view),
    path('login/', views.login_view),
    path('my_account/', views.my_account_view),
    path('register/', views.register_view),
    path('service/', views.service_view),
    path('shop/', views.shop_view),
    path('single_product/', views.single_product_view),
    path('wishlist/', views.wishlist_view),
    path('404/', views.page_not_found_view),

    # path('site/', include('site.urls')),
]
