from django.db import models

# Create your models here.
class CourseData(models.Model):
        course_name = models.CharField(max_length = 100)
        course_intro = models.TextField()

        def __str__(self):
            return self.course_name
