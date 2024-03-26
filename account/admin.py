from django.contrib import admin
from .models import Student, Teacher, StudentDetails, TeacherDetails, Batch, Role, Subject, Department,Permission,Branch

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(StudentDetails)
admin.site.register(TeacherDetails)
admin.site.register(Batch)
admin.site.register(Role)
admin.site.register(Subject)
admin.site.register(Department)
admin.site.register(Branch)
admin.site.register(Permission)


