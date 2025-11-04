from django.db import models


class PageVisit(models.Model):
    path = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.path}: {self.timestamp} visits"
