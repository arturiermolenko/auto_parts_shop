from django.urls import path

from shop.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]

app_name = "shop"
