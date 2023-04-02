from django.db import models

# Create your models here.
class ContentHeading(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Content(models.Model):
    heading = models.ForeignKey(ContentHeading, on_delete=models.CASCADE)
    content_name = models.CharField(max_length=15)
    def __str__(self):
        return self.content_name


class SideMenuContent(models.Model):
    name = models.CharField(max_length = 255)
    url = models.CharField(max_length = 500,blank=True)
    is_head = models.BooleanField(default=False)
    svg = models.CharField(max_length = 2000,blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name