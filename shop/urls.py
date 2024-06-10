from django.urls import path

from shop.views import (
    IndexView,
    CategoryListView,
    CategoryDetailView,
    ItemDetailView
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("<str:category_name>/", CategoryDetailView.as_view(), name="category_detail"),
    path("<str:category_name>/<slug:slug>/", ItemDetailView.as_view(), name="item_detail"),
]

app_name = "shop"
