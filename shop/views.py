from django.shortcuts import get_object_or_404
from django.views import generic

from shop.models import Item, Category


class IndexView(generic.TemplateView):
    template_name = "shop/index.html"

    def get_context_data(self, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class CategoryListView(generic.ListView):
    model = Category
    context_object_name = "category_list"
    template_name = "shop/category_list.html"


class CategoryDetailView(generic.DetailView):
    model = Category
    context_object_name = "category"
    template_name = "shop/category_detail.html"
    paginate_by = 12

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = self.object.items.all()

        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Category, name=self.kwargs.get("category_name"))


class ItemDetailView(generic.DetailView):
    model = Item
    template_name = "shop/item_detail.html"
    context_object_name = "item"

    def get_object(self, queryset=None):
        category_name = self.kwargs.get("category_name")
        slug = self.kwargs.get("slug")
        return get_object_or_404(Item, slug=slug, category__name=category_name)
