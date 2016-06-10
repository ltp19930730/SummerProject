from django.db import models

# Create your models here.
class CourseData(models.Model):
        course_name = models.CharField(max_length = 100)
        course_platform = models.CharField(max_length = 100,blank = False, null = True)
        course_video_url = models.URLField(blank = True, null = True)
        course_homepage_url = models.URLField(blank = False, null = True)
        course_intro = models.TextField()

        def __str__(self):
            return self.course_name
