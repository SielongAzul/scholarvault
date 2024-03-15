from django.db import models

# Create your models here.


class Scholarships(models.Model):
    scholarship_name =  models.CharField(max_length=50)
    scholarship_provider_name = models.CharField(max_length=50)
    eligibility = models.TextField(null = True, blank = True)
    requirements = models.TextField()
    created = models.DateTimeField(auto_now_add = True)

def __str__(self):
            return self.scholarship_name