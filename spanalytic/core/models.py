from django.db import models


class ReportRequest(models.Model):
    """A prospect asking for the free AI-visibility report — not yet a paying Client."""

    clinic_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    website = models.URLField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.clinic_name} ({self.email})"
