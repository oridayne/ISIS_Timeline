# ISIS_Timeline
For the Kaggle Post: https://www.kaggle.com/kzaman/how-isis-uses-twitter

I wanted to put my skills from previous internships to use, so I decided that I'd try them out on this dataset.

I've used Postgres + Django + D3 (The stack I used in my previous internship).

While it may be overkill, I just wanted to practice using the tech. The added UI, and built in search and filtering though is very handy.
I hope that data scientists who are not as programming savvy will be able to use these visualizations and UI to help enhance their data analytics. 

This is my first personal project on Github! So apologies if I commit anything that is very messy or not meta.

To get started: 
1. Make sure you have the requirements
2. You'll need to load in the users and tweets into the postgres database. Check out make_users.py and make_tweets.py.
3. cd into timeline (where manage.py is stored) These next few instructions are for those non-django users
4. python manage.py runserver
5. http://127.0.0.1:8000/entry/swag/#/ To view the endpoints  http://127.0.0.1:8000/admin to see the Admin UI :D
6. NOTE: Only GET is supported for now. I currently have no need to make the other endpoints, so I didn't bother.

Additional Note:
I haven't done any testing, and I know that's not great software engineering. But right now I'm really interested in doing some other things with this dataset so I'll put that on the backburners for now.
