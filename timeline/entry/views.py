from django.shortcuts import render
from entry.models import *
from rest_framework import viewsets, filters, generics, response, schemas

from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from entry.serializers import *
from django.core.paginator import Paginator
import datetime
import json

#from django.views.generics import ListAPIView
# Create your views here.


@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Bookings API')
    return response.Response(generator.get_schema(request=request))


class UserViewSet(viewsets.ModelViewSet):
	"""
	A viewset for viewing and editing users 
	"""
	serializer_class = UserSerializer
	queryset = User.objects.all()

class TweetViewSet(viewsets.ModelViewSet):
	"""
	A viewset for viewing and editing tweets 
	"""
	serializer_class = TweetSerializer
	queryset = Tweet.objects.all()
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('date','user',)


@api_view(['GET'])
def tweet_date_list(request):
	"""
	API Call for tweet count on a date
	"""
	date_dict = {}
	date_counts = []
	def truncate(date):
		return date.strftime('%m/%d/%Y')

	tweets = Tweet.objects.all()
	for tw in tweets:
		tweet_date = truncate(tw.date)
		if tweet_date in date_dict:
			count = date_dict[tweet_date]
			date_dict[tweet_date] = count+1
		else:
			date_dict[tweet_date] = 0
	for key in date_dict:
		date_counts.append({"date": key, "count": date_dict[key]})
	return response.Response(date_counts)

@api_view(['GET'])
def tweet_date_content(request):
	"""
	API Call for tweets on a date 
	"""
	date_dict = {}
	def truncate(date):
		return date.strftime('%m/%d/%Y')
	def format_tweet(tw):
		return (tw.user.name,tw.tweet_detail)

	tweets = Tweet.objects.all()
	for tw in tweets:
		tweet_date = truncate(tw.date)
		formated_tweet = format_tweet(tw)
		if tweet_date in date_dict:
			tweets_list = date_dict[tweet_date]
			tweets_list.append(formated_tweet)
		else:
			date_dict[tweet_date] = [formated_tweet]
	return response.Response(date_dict)



def ISIS_Bargraph(request):
	"""
	Bargraph of tweets
	"""
	tweets = Tweet.objects.all()

	return render(request, "entry/isis-bargraph.html")

