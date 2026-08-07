from django import forms

from .models import ReportRequest


class ReportRequestForm(forms.ModelForm):
    class Meta:
        model = ReportRequest
        fields = ["clinic_name", "city", "website", "email"]
        widgets = {
            "website": forms.URLInput(attrs={"placeholder": "https://"}),
        }
