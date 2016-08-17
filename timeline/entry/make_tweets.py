from datetime import datetime
from django.utils import timezone
import csv
import pytz
from entry.models import *
path ="/Users/lisadeng/how-isis-uses-twitter/tweets.csv"
# exec(open("/Users/lisadeng/timeline/entry/make_tweets.py").read())
with open(path, 'rt', encoding="utf8") as f:
	reader = csv.reader(f)
	tweets = list(reader)
tweets.pop(0)
count=0
users = {}
timezone.now()
for t in tweets:
	try:
		count+=1
		date = t[6]
		date_obj = datetime.strptime(date, '%m/%d/%Y %H:%M')
		date_obj = pytz.utc.localize(date_obj)
		date_obj = date_obj.date()
		detail = t[7]
		location = t[3]
		followers = int(t[4])
		status_number = int(t[5])
		username = t[1]
		user = User.objects.get(username=username)
		tweet = Tweet(user=user, date=date_obj, tweet_detail=detail,
			location=location, followers=followers,
			status_number=status_number)
		tweet.save()
	except:
		print(str(count)+" "+username)
		raise ValueError