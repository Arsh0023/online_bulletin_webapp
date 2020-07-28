from django.db import models

# Create your models here.

class student(models.Model):
    stream_choices = (
    ('CSE','CSE'),
    ('ECE','ECE'),
    ('Mechanical','Mechanical'),
    ('Civil','Civil'),
    )

    year_choices = (
    (1,"1st year"),
    (2,"2nd year"),
    (3,"3rd year"),
    (4,"4th year"),
    )
    name = models.CharField(max_length=264)
    phone_no = models.CharField(max_length=13,unique=True)
    email = models.EmailField(unique=True)
    stream = models.CharField(max_length=10,choices = stream_choices)
    year = models.IntegerField(choices=year_choices)

    def __str__(self):
        return("{}, stream - {} ,year-{} ".format(self.name,self.stream,self.year))
