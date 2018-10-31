from django.db import models

# Create your models here.
class Polls(models.Model):
    """Profile status update"""

    name = models.CharField(max_length = 255)
    text = models.CharField(max_length = 255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the model as a string"""
        return self.name