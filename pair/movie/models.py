from django.db import models

# Create your models here.

class Review(models.Model):

    title = models.CharField(max_length = 80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    upadated_at = models.DateTimeField(auto_now = True)
    score = models.CharField(null=True, max_length=5)
    writer = models.CharField(null=True, max_length=10)