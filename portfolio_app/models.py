from django.db import models

# Create your models here.

class portfolio(models.Model):
    name=models.CharField(max_length=255,null=True, blank=True)
    website_pic=models.ImageField(null=True, blank=True, upload_to= 'media/portfolio')
    category=models.CharField(max_length=255)
    website_url=models.CharField(max_length=255,null=True, blank=True)

    def __str__ (self):
        return self.name + '|'+str(self.category)+'|'+str(self.website_url)


class review(models.Model):
    name=models.CharField(max_length=255,null=True, blank=True)
    client_pic=models.ImageField(null=True, blank=True, upload_to= 'media/portfolio')
    post=models.CharField(max_length=255)
    description=models.TextField()

    def __str__ (self):
        return self.name + '|'+str(self.post)

    
       


