# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class MyIP(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    myipaddress = models.TextField()

    def __str__(self):
        return self.myipaddress + ' ' + str(self.created_date)