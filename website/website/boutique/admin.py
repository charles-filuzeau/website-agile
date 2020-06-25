from django.contrib import admin

# Register your models here.
from .models import Course, User, Formation, Inspiration

admin.site.register(Course)
admin.site.register(User)
admin.site.register(Formation)
admin.site.register(Inspiration)
