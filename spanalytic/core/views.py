from django.shortcuts import render


from django.views.generic import (
    UpdateView,
    RedirectView,
    CreateView,
    View,
    TemplateView,
    DetailView,
    ListView,
    DeleteView,
)

class IndexView(TemplateView):
    template_name = "index.html"