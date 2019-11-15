import datetime

from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone


# from django.db.backends.mysql.base import DatabaseWrapper
# 改源码，datetime(6)改为datetime
# DatabaseWrapper.data_types['DateTimeField'] = datetime
from utils.model_tools import upload_to


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, phone=None):
        """
        Creates and saves a User with the given phone, email and password.
        """
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
            email=email,
            phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, phone=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(username,
                                password=password,
                                email=email,
                                phone=phone
                                )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(verbose_name="用户名", max_length=255, unique=True)
    password = models.CharField('password', max_length=128)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    phone = models.CharField(
        verbose_name='手机号码',
        help_text='手机号码',
        max_length=11,
        # validators=[MinLengthValidator(11, message="手机号仅能为11位")],
        # unique=True,
        blank=True,
        null=True,
        default='17706120671'
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=timezone.now)
    updated_time = models.DateTimeField(verbose_name="更新时间", auto_now=datetime.datetime.now)
    avatar = models.ImageField(upload_to=upload_to, default=u"image/avatar/default.png",
                               max_length=100, blank=True, null=True)
    # type = models.SmallIntegerField(
    #     choices=((1, '普通用户'), (2, 'VIP用户')),
    #     default=1
    # )

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):  # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        db_table = "users"
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['id']
