from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import *

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tweets', views.TweetViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^isis-bargraph/$', views.ISIS_Bargraph, name="bargraph"),
    url(r'^tweet-count/$', views.tweet_date_list, name="tweet-count")
]

