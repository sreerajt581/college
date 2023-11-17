from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)


    def __str__(self):
        return '{}'.formate(self.username)

class Register(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self):
        return '{}'.formate(self.username)
class Department(models.Model):
    name=models.CharField(max_length=100,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'
    def __str__(self):
        return '{}'.format(self.name)

class Course(models.Model):
    name=models.CharField(max_length=100,unique=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    class Meta:
        ordering=('name',)
        verbose_name='course'
        verbose_name_plural='courses'
    def __str__(self):
        return '{}'.format(self.name)