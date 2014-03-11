from django.db import models

# Create your models here.
BEER_CHOICES = (
	('D', 'Domestic'),
	('I', 'Import'),)

class Beer(models.Model):
	name		= models.CharField(max_length=200)
	slug		= models.SlugField(unique=True)
	brewery		= models.ForeignKey('Brewery')
	locality 	= models.CharField(max_length=1, choises=BEER_CHOICES)
	description	= models.TextField(blank=True)

	def __unicode__(self):
	    return self.name

class Brevery(models.Model):
	name		= models.CharField(max_length=200)
	slug		= models.SlugField(unique=True)
	description	= models.TextField(blank=True)

	def __unicode__(self):
	    return self.name

