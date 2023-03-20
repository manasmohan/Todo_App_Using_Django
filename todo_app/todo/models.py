from django.db import models

# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField(max_length=500,default='')
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


# class Register(models.Model):
#     username = models.CharField(max_length=150)
#     password = models.CharField(max_length=150)
#     email = models.EmailField(max_length=150)
#
# class Login(models.Model):
#     username = models.CharField(max_length=150)
#     password = models.CharField(max_length=150)