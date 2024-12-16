from django.contrib import admin
from .models import Course, Student, Comment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "enrolled_at", "course")
    search_fields = ("name", "email")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("course", "student", "created_at")
    search_fields = ("course__title", "student__name", "comment_text")
