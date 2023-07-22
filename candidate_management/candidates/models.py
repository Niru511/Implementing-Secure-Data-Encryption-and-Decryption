from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=20)
    adharnumber = models.TextField(blank=True, null=True)
    pannumber = models.TextField(blank=True, null=True)
    passportnumber = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"