from django.db import models

# Create your models here.
class CourseDetail(models.Model):
    course_title = models.CharField(max_length=50)
    course_des = models.TextField()