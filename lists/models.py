from django.db import models


class Item(models.Model):
    text = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('-text',)
