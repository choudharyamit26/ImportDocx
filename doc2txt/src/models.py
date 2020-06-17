from django.db import models

# Create your models here.
class Questions(models.Model):
    document = models.FileField(upload_to='media/', max_length = 100,null=True,blank=True)
    subject = models.CharField(max_length = 150,null=True,blank=True)
    question = models.CharField(max_length=10000)
    ques_image = models.CharField(max_length = 150,null=True,blank=True)
    option_a = models.CharField(max_length=1000)
    option_b = models.CharField(max_length=1000)
    option_c = models.CharField(max_length=1000)
    option_d = models.CharField(max_length=1000)
    ans = models.CharField(max_length = 150,null=True,blank=True)
    
