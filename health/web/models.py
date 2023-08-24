from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.utils import timezone

class Exercises(models.Model):
    id_name = models.IntegerField( primary_key=True)
    name_ko = models.CharField(max_length=50)
    name_en = models.CharField(max_length=25)
    dir = models.CharField(max_length=20)
    part = models.CharField(max_length=50)

    def __str__(self):
        return self.name_ko


# # accounts/models.py

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError("The Username field must be set")
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(username, password, **extra_fields)


# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=150, unique=True)
#     name = models.CharField(max_length=100)  # 추가 필드: 이름
#     registration_time = models.DateTimeField(default=timezone.now)  # 추가 필드: 회원가입 시간
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['name']

#     def __str__(self):
#         return self.username

    
