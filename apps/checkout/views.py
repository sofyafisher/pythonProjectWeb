from django.shortcuts import render
from django.views import View


class Checkout(View):
    def get(self, request):
        return render(request, 'checkout/checkout.html')


# Create your views here.
