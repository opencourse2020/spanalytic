from django.contrib import admin

from .models import ReportRequest


@admin.register(ReportRequest)
class ReportRequestAdmin(admin.ModelAdmin):
    list_display = ["clinic_name", "city", "email", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["clinic_name", "city", "email", "website"]
    readonly_fields = ["created_at"]
