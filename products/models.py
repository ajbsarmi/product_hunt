from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Products class
class Product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to ='images/')
    icon = models.ImageField(upload_to ='images/')
    votes_total = models.IntegerField(default=1)
    #This is a way to connect multiple models inside the database
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    # This returns the title of the blog page in admin/blog/blog
    def __str__(self):
        return self.title
        
    #This limit the the number of the next in the body
    def summary(self):
        return self.body[:100]

    #This will only return the date in the blog page
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

# hunter