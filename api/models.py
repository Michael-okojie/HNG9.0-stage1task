from django.db import models


class Person(models.Model):
    slackUsername = models.CharField(max_length=20)
    backend = models.BooleanField(default=True)
    age = models.IntegerField(null=False)
    bio = models.CharField(max_length=120)

    def __str__(self):
        return self.slackUsername
