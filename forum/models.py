from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class question(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True)
    slug = models.SlugField(null= True,blank= True,unique= True)
       

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

class answers(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    ans = models.ForeignKey(question,on_delete=models.CASCADE)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)


