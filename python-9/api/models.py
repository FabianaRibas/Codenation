from django.db import models
from django.core.validators import (MinLengthValidator, validate_ipv4_address)


class User(models.Model):
    name = models.CharField('Name', max_length=50)
    last_login = models.DateTimeField('Last login', auto_now=True)
    email = models.EmailField('Email')
    password = models.CharField(
        'Password',
        max_length=50,
        validators=[MinLengthValidator(8)]
    )

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField('Name', max_length=50)
    status = models.BooleanField('Status', default=False)
    env = models.CharField('Env', max_length=20)
    version = models.CharField('version', max_length=5)
    address = models.GenericIPAddressField(
        'Address',
        max_length=39,
        validators=[validate_ipv4_address]
    )

    def __str__(self):
        return self.name


class Event(models.Model):
    OPTIONS_LEVEL = (
        ('c', 'CRITICAL'),
        ('d', 'DEBUG'),
        ('e', 'ERROR'),
        ('w', 'WARNING'),
        ('i', 'INFO'),
    )

    level = models.CharField(max_length=20, choices=OPTIONS_LEVEL)
    data = models.TextField('Data')
    arquivado = models.BooleanField('Arquivado', default=False)
    date = models.DateField('Date', auto_now=True)

    agent = models.ForeignKey('Agent', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.level


class Group(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name


class GroupUser(models.Model):
    group = models.ForeignKey('Group', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)
