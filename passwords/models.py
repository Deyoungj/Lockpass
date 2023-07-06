from django.db import models
from django.utils import timezone
from users.models import User




class Passwords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=100)
    site_password = models.CharField(max_length=200)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date_added',)
        verbose_name_plural = 'passwords'


    def __str__(self):
        return self.site_name