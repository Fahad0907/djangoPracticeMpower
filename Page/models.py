from django.db import models
from Landing.models import User
# Create your models here.
class Page(models.Model):
    banner_image = models.ImageField(upload_to="images/")
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255,unique=True,blank=True,null=True)
    
    # def __str__(self) -> str:
    #     return self.title

class PageComponent(models.Model):
    richtext = models.TextField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
