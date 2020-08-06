from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.user_name

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200, default="Scrum Alliance Training")
    logo = models.CharField(max_length=200, default="scrum.png")
    json = models.CharField(max_length=20000, null=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.course_name


class Formation(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    seats = models.IntegerField(default=0)
    location = models.CharField(max_length=50)
    date = models.DateField('date of the formation')
    def __str__(self):
        return str(self.course) + " " + str(self.teacher) + " " + str(self.location)

class Inspiration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=500)
    pub_date = models.DateField()
    def __str__(self):
        return str(self.title) + ' ' + str(self.user)

class CourseReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=500)
    pub_date = models.DateField('date published')
    def __str__(self):
        return str(self.title) + ' ' + str(self.user) + ' | ' + str(self.course.course_name)

class CourseInstance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    location = models.CharField(max_length=500)
    image_name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.course) + ' ' + str(self.date)
