from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse


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

from .forms import ReportRequestForm


class IndexView(CreateView):
    template_name = "index.html"
    form_class = ReportRequestForm

    def get_success_url(self):
        return f"{reverse('core:index')}#request"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            "Thanks — we'll run your clinic's report and email the PDF within five business days.",
        )
        return response