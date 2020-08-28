from django.db import models

# Create your models here.
class Excel(models.Model):
    country = models.CharField(default= "", max_length = 20)
    file = models.FileField(upload_to ='excel')

    def __str__(self):
        return self.file.name
    
    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)