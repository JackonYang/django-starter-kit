# -*- coding: utf-8 -*-
import random
from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager,
)


def get_random_email_error():
    return random.randint(1, 999999)


def get_random_phone_error():
    return random.randint(1, 999999)


class UserManager_(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        '''
        Creates and saves a User with the given data
        '''
        if not username:
            raise ValueError('Users must have a username number')

        user = self.model(
            username=self.normalize_email(username),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        return self._create_user(username, password, **extra_fields)


class User_(AbstractBaseUser):
    S_REGISTERING = 1
    S_PENDING_REVIEW = 11
    S_NORMAL = 21
    S_BANNED = 99

    STATUS_CHOICES = (
        (S_REGISTERING, u'注册中'),
        (S_PENDING_REVIEW, u'待审核'),  # 代码控制是否生效
        (S_NORMAL, u'正常'),
        (S_BANNED, u'已禁用'),
    )

    nick_name = models.CharField(u'昵称', max_length=256, blank=True)

    status = models.IntegerField(u'状态', choices=STATUS_CHOICES, default=S_NORMAL)

    # RFC 2821 places a 256 character limit on the forward-path. But a path is defined as
    # Path = "<" [ A-d-l ":" ] Mailbox ">"
    # So the forward-path will contain at least a pair of angle brackets in addition to the Mailbox.
    # This limits the Mailbox (i.e. the email address) to 254 characters.
    email = models.CharField(max_length=254, default='', blank=True)
    email_error = models.IntegerField(default=get_random_email_error)

    mobile = models.CharField(max_length=50, default='', blank=True)
    mobile_error = models.IntegerField(default=get_random_phone_error)

    # 1. must have a single unique field that can be used for identification purposes
    # 2. provide a way to address the user in a short and long form

    # 可能存 email, 所以，长度为 254
    username = models.CharField(u'username', max_length=244, unique=True, db_index=True)
    is_staff = models.BooleanField(u'系统管理员', default=False)

    objects = UserManager_()

    USERNAME_FIELD = 'username'
    # A list of the field names that will be prompted for when creating a user via the createsuperuser management command.
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = u'用户账号系统'
        verbose_name_plural = verbose_name

        unique_together = (
            ('email', 'email_error'),
            ('mobile', 'mobile_error'),
        )

    @property
    def is_active(self):
        return self.status != self.S_BANNED

    def get_full_name(self):
        return '%s(%s)' % (self.username, self.nick_name)

    def get_short_name(self):
        # return username field
        return self.username

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
