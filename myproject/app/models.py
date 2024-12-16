from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kurs nomi")
    description = models.TextField(verbose_name="Kurs tavsifi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Tahrirlangan vaqti")

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name="Talaba ismi")
    email = models.EmailField(unique=True, verbose_name="Email")
    enrolled_at = models.DateTimeField(auto_now_add=True, verbose_name="Ro‘yxatdan o‘tgan vaqt")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students", verbose_name="Kurs")

    def __str__(self):
        return self.name


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="comments", verbose_name="Kurs")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="comments", verbose_name="Talaba")
    comment_text = models.TextField(verbose_name="Izoh matni")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    def __str__(self):
        return f"{self.student.name} - {self.course.title}"
