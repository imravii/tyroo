# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def check_id(value):
    if(value[0]!='W' or value[1]!='P' or value[2]!='N' or value[3]!='-'):
        raise ValidationError(
            _('%(value)s is not a jira id'),
            params={'value':value},
        )
class Rule(models.Model):
    Swiggy = 0
    Netflix = 1
    Youtube = 2
    geeks = 3
    music = 4

    FifteenMin=0
    Hour=1
    Day=2
    scheduleTime=(

        # Every 15 minutes, Every hour, Every day at 12:00 AM
        ('Fifteen Min', 'Every 15 minutes'),
        ('Hourly', 'Every Hour'),
        ('Mid Day(Noon)', 'EveryDay'),
    )
    camps = (
        (Swiggy, 'Swiggy'),
        (Netflix, 'Netflix'),
        (Youtube, 'Youtube'),
        (geeks, 'geeks'),
        (music, 'music'),

    )
    Action_CHOICES = (
        ('Notify', 'Notify'),
    )
    Status_c = (
        ('Activated', 'Activated'),
        ('Deactivated', 'Deactivated'),
    )
    MEtric_Conditions=(
        ('eCPM` >= $5.00 AND `Impressions` >= 1000000', 'eCPM` >= $5.00 AND `Impressions` >= 1000000'),
        ('Spend` >= $1000.00 AND `eCPC` <=  $0.20', 'Spend` >= $1000.00 AND `eCPC` <=  $0.20'),
        ('`Clicks` >= 50000 AND `Installs` <= 100', '`Clicks` >= 50000 AND `Installs` <= 100'),
        ('`eCPI` >= $2.00 AND `Installs` >= 100', '`eCPI` >= $2.00 AND `Installs` >= 100'),

    )
    Rule_name = models.CharField(max_length=30)
    Campaigns=MultiSelectField(choices=camps, max_length=11)
    Schedule=models.CharField(max_length=100,blank=False, choices=scheduleTime)
    Conditions = models.CharField(max_length=100, blank=False,choices=MEtric_Conditions )
    Action= models.CharField(max_length=6, choices=Action_CHOICES, default='Notify')
    Status = models.CharField(max_length=15,choices=Status_c, default='Notify')

    def get_absolute_url(self):
        return reverse('home:index')
    def __str__(self):
        return '%s'% self.Rule_name