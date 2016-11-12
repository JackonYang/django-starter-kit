# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager,
)


class MyUserManager(BaseUserManager):
    def _create_user(self, phone, password, **extra_fields):
        '''
        Creates and saves a User with the given data
        '''
        if not phone:
            raise ValueError('Users must have a phone number')

        user = self.model(
            phone=self.normalize_email(phone),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        return self._create_user(phone, password, **extra_fields)


class MyUser(AbstractBaseUser):
    S_REGISTERING = 1
    S_PENDING_REVIEW = 5
    S_NORMAL = 11
    S_SLEEPING = 21
    S_BANNED = 99

    STATUS_CHOICES = (
        (S_REGISTERING, u'注册中'),
        (S_PENDING_REVIEW, u'待审核'),
        (S_NORMAL, u'正常'),
        (S_SLEEPING, u'休息中'),
        (S_BANNED, u'已禁用'),
    )

    nick_name = models.CharField(u'昵称', max_length=256, blank=True)

    status = models.IntegerField(u'状态', choices=STATUS_CHOICES, default=S_REGISTERING)

    # 1. must have a single unique field that can be used for identification purposes
    # 2. provide a way to address the user in a short and long form
    phone = models.CharField(u'手机号码', max_length=50, unique=True, db_index=True)
    is_staff = models.BooleanField(u'系统管理员', default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone'
    # A list of the field names that will be prompted for when creating a user via the createsuperuser management command.
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = u'用户账号系统'
        verbose_name_plural = verbose_name

    @property
    def is_active(self):
        return self.status != self.S_BANNED

    def get_full_name(self):
        return '%s(%s)' % (self.nick_name, self.phone)

    def get_short_name(self):
        # return username field
        return self.phone

    def __unicode__(self):
        return self.get_short_name()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
