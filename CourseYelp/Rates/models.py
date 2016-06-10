from django.db import models

# Create your models here.
class Course(models.Model):
    course_text = models.CharField(max_length=200)
    rating_date = models.DateTimeField('date rating')
    def __str__(self):
        return self.course_text

class Choice(models.Model):
    question = models.ForeignKey(Course, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    rates = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
