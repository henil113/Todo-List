from django.db import models

# Create your models here.

class duty(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.title
