from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(max_lenght=264)
    phone_no = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    stream = models.CharField(max_lenght="10")
    year = models.IntegerField()

    def __str__(self):
        return("{}, stream - {} ,year-{} ".format(self.name,self.stream,self.year))
