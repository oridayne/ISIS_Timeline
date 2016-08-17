from django.db import models
from timeline.settings import DATE_INPUT_FORMATS
# Create your models here.
SENT = (("Positive", "Positive"),
					 ("Negative", "Negative"),
					 ("Neutral", "Neutral"))

class Clergy(models.Model):
	"""
	ISIS Clergymen
	"""
	name = models.TextField(max_length=140)
	def __str__(self):
		return self.name

class User(models.Model):
	"""
	User 
	"""
	name = models.CharField(max_length = 400)
	username = models.CharField(max_length = 400, unique=True)
	description = models.TextField()
	
	def __str__(self):
		return self.name
	
class Tweet(models.Model):
	"""
	Tweets from the user
	"""
	date = models.DateField('date')
	tweet_detail = models.TextField(max_length=140)
	location = models.CharField(max_length=200)
	followers = models.IntegerField(default=0)
	status_number = models.IntegerField(default=0)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	sentiment = models.CharField(max_length=15, choices = SENT, default = "Neutral")
	mentioned_clergy = models.ManyToManyField(Clergy)

	def __str__(self):
		return self.user.name + "::: " + self.tweet_detail
