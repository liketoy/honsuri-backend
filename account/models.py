from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager): # 유저를 생성할 때 사용하는 Helper 클래스
    def create_user(self, email, name, nickname, phone_number, alcohol_amount, favorite_alcohol, favorite_food, favorite_combination, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name = name,
            nickname = nickname,
            phone_number = phone_number,
            alcohol_amount = alcohol_amount,
            favorite_alcohol = favorite_alcohol,
            favorite_food = favorite_food,
            favorite_combination = favorite_combination,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, nickname, password):
        user = self.create_user(
            email,
            password = password,
            name = name,
            nickname = nickname,
            phone_number = '',
            alcohol_amount = 0,
            favorite_alcohol = '',
            favorite_food = '',
            favorite_combination = '',
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser): 

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=40, unique=False)
    nickname = models.CharField(max_length=40, unique=True)
    phone_number = models.CharField(max_length=12, unique=False)

    alcohol_amount = models.FloatField(blank=True)
    favorite_alcohol = models.CharField(max_length=40, blank=True)
    favorite_food = models.CharField(max_length=40, blank=True)
    favorite_combination = models.CharField(max_length=40, blank=True)

    # photo = models.ImageField(upload_to="profile/image", default='user.py')
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'nickname']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    class meta:
        db_table = "user"