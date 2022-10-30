from django.contrib import admin
from course.models import CourseDetail

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    details_display = [ 'course_title','course_des' ]

admin.site.register(CourseDetail,ServiceAdmin)
