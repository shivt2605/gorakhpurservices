from django.db import models
from response.models import Response

# Create your models here.

class Meeting(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    meeting = models.DateTimeField(null=True, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    
