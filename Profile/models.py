from django.db import models
from Landing.models import User
# Create your models here.

class Profile(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    image = models.ImageField(upload_to="images/")

    def __str__(self) -> str:
        return str(self.age)