from django.shortcuts import render
# from django.http import HttpResponse

# write unit and functional test to all of these views


def home_page_view(request):
	return render(request, 'index.html')

def about_view(request):
	return render(request, 'about-us.html')

def cart_view(request):
	return render(request, 'cart.html')

def checkout_view(request):
	return render(request, 'checkout.html')

def contact_view(request):
	return render(request, 'contact-us.html')

def faq_view(request):
	return render(request, 'faq.html')

def restore_password_view(request):
	return render(request, 'forgot-password.html')

def login_view(request):
	return render(request, 'login.html')

def my_account_view(request):
	return render(request, 'my-account.html')

def register_view(request):
	return render(request, 'register.html')

def shop_view(request):
	return render(request, 'shop.html')

def shop_list_view(request):
	return render(request, 'shop-list.html')

def product_view(request):
	return render(request, 'single-product.html')

def wishlist_view(request):
	return render(request, 'wishlist.html')

def page_not_found_view(request, exception=None):
	return render(request=request, template_name='404.html')
