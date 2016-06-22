from django.db import models

# Create your models here.


class CourseData(models.Model):
        course_name = models.CharField(max_length = 100)
        course_platform = models.CharField(max_length = 100,blank = False, null = True)
        course_imag = models.FileField(null = True,blank = True)
        course_video_url = models.URLField(blank = True, null = True)
        course_homepage_url = models.URLField(blank = True, null = True)
        course_intro = models.TextField()

        tags = models.ManyToManyField('Tag', blank=True)
        def __str__(self):
            return self.course_name

class Tag(models.Model):
        name = models.CharField(max_length = 20)
        created_time = models.DateTimeField( auto_now_add=True)
        last_modified_time = models.DateTimeField(auto_now=True)
        def __str__(self):
            return self.name
