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
	user = t[0]
	
	#get the user object
	if user not in users:
		person = User(name=user, username=t[1], description=t[2])
		person.save()




