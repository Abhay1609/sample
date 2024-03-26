from django.contrib.auth.models import User, Group
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string
import os

def get_image_path(instance, filename):
    return os.path.join(instance.__class__.__name__, filename)

class Student(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    dob = models.DateField()
    studentNumber = models.IntegerField()
    email=models.CharField(max_length=20)
    picture = models.ImageField(upload_to=get_image_path)
    mobile = models.CharField(max_length=10)
    detail = models.OneToOneField('StudentDetails', on_delete=models.CASCADE)
    batch = models.ForeignKey('Batch', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    isDeleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Create a user with random password and assign to group
        username = f"student_{self.studentNumber}"
        password = get_random_string(length=10)
        print(password)
        user = User.objects.create_user(username=username, password=password)
        user.groups.add(self.group)
        user.save()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    dob = models.DateField()
    email=models.CharField(max_length=10)
    EmpId = models.IntegerField()
    picture = models.ImageField(upload_to=get_image_path)
    mobile = models.CharField(max_length=10)
    detail = models.OneToOneField('TeacherDetails', on_delete=models.CASCADE)
    batch = models.ForeignKey('Batch', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE )
    isDeleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Create a user with random password and assign to group
        username = f"teacher_{self.EmpId}"
        password = get_random_string(length=10)
        user = User.objects.create_user(username=username, password=password)
        user.groups.add(self.group)
        user.save()

    def __str__(self):
        return self.name

class StudentDetails(models.Model):
    address = models.CharField(max_length=20)
    pincode = models.IntegerField()
    # Add field also here for student number
    state = models.CharField(max_length=10)
    fatherName = models.CharField(max_length=50)
    motherName = models.CharField(max_length=50)
    aadhar = models.CharField(max_length=20)
    fatherPhone = models.CharField(max_length=20)
    motherPhone = models.CharField(max_length=20)
    fatherPicture = models.ImageField(upload_to=get_image_path)
    motherPicture = models.ImageField(upload_to=get_image_path)
    isDeleted = models.BooleanField(default=False)

class TeacherDetails(models.Model):
    address = models.CharField(max_length=20)
    pincode = models.IntegerField()
    state = models.CharField(max_length=10)
    fatherName = models.CharField(max_length=50)
    motherName = models.CharField(max_length=50)
    aadhar = models.CharField(max_length=20)
    fatherPhone = models.CharField(max_length=20)
    motherPhone = models.CharField(max_length=20)
    fatherPicture = models.ImageField(upload_to=get_image_path)
    motherPicture = models.ImageField(upload_to=get_image_path)
    experience = models.CharField(max_length=100)
    qualification = models.CharField(max_length=10)
    isMarried = models.BooleanField()
    # Add field of emp id here
    partnerName = models.CharField(max_length=100, blank=True)
    partnerPhone = models.CharField(max_length=20, blank=True)
    partnerPicture = models.ImageField(upload_to=get_image_path, blank=True)
    isDeleted = models.BooleanField(default=False)

    def clean(self):
        if self.isMarried and not self.partnerName:
            raise ValidationError("Partner's name is required for married teacher.")
        if self.isMarried and not self.partnerPhone:
            raise ValidationError("Partner's phone number is required for married teacher.")

    def __str__(self):
        return self.aadhar

class Batch(models.Model):
    course = models.CharField(max_length=30)
    year = models.IntegerField()
    session = models.CharField(max_length=10)
    semester = models.IntegerField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    subjects = models.ManyToManyField('Subject')
    branch=models.ManyToManyField('Branch')
    isDeleted = models.BooleanField(default=False)


    def __str__(self):
        return self.course

class Role(models.Model):
    
    name = models.ForeignKey(Group, on_delete=models.CASCADE )
    permissions = models.ManyToManyField('Permission')

    def __str__(self):
        return self.permissions

class Permission(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=10)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
class Subject(models.Model):
    subject = models.CharField(max_length=100)
    subCode = models.CharField(max_length=70)
    maxClass = models.IntegerField()
    hasExam = models.BooleanField(default=True)
    credit = models.IntegerField()
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
class Branch(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
