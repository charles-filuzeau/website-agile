from django.contrib import admin
from django.forms import TextInput, Textarea
# Register your models here.
from .models import Course, User, Formation, Inspiration, CourseReview, CourseInstance
from django.db import models
class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows':6, 'cols':100})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }



admin.site.register(Course, YourModelAdmin)
admin.site.register(User)
admin.site.register(Formation)
admin.site.register(Inspiration)
admin.site.register(CourseReview)
admin.site.register(CourseInstance)
