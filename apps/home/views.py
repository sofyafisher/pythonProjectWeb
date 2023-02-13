from django.shortcuts import render
from django.views import View
from apps.cart_shop.models import Product

class IndexShopView(View):
    def get(self, request):
        data = Product.objects.all()
        context = {'data': data}
        return render(request, 'home/index.html', context)

class AboutView(View):
    def get(self, request):
        return render(request, 'home/about.html')

class Contacts(View):
    def get(self, request):
        return render(request, 'home/contact.html')