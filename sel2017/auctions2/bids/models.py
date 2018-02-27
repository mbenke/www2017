from django.db import models

class Bid(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name