from django.shortcuts import render
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "shop/index.html"

    def get_context_data(self, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
