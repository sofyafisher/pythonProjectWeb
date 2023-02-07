from django.urls import path

from .views import CurrentDateView
from .views import IndexView
from .views import Hello


urlpatterns = [
   path('datetime/', CurrentDateView.as_view()),
   path('', IndexView.as_view()),
   path('hello/', Hello.as_view()),
]