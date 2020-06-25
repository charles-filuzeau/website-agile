from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.course_name


class User(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.user_name


class Formation(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    seats = models.IntegerField(default=0)
    location = models.CharField(max_length=50)
    date = models.DateTimeField('date of the formation')
    def __str__(self):
        return str(self.course) + " " + str(self.teacher) + " " + str(self.location)
