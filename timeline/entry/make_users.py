from datetime import datetime
import csv
from entry.models import *
path ="/Users/lisadeng/how-isis-uses-twitter/tweets.csv"
# exec(open("/Users/lisadeng/timeline/entry/make_users.py").read())
with open(path, 'rt', encoding="utf8") as f:
	reader = csv.reader(f)
	tweets = list(reader)
tweets.pop(0)
count=0
users = {}
clergymen = [ "Anwar Awlaki", "Ahmad Jibril", "Ibn Taymiyyah", "Abdul Wahhab",
			  "Hamza Yusuf", "Suhaib Webb", "Yaser Qadhi", "Nouman Ali Khan", "Yaqoubi"]

for t in tweets:
	count+=1
	username = t[1]
	
	try:
	#get the user object
		if len(User.objects.filter(username=username))==0:
		#if username not in users:
			person = User(name=t[0], username=t[1], description=t[2])
			person.save()
			users[username]=True

	except:
		print(username+ " " + str(count))
		print(t[1] + " "+ t[2])

		raise ValueError
