from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import twitter
def get_tweets():
    """
    returns twitter feed with settings as described below, contains all related twitter settings
    """
    api = twitter.Api(consumer_key='j1sMcd6ZR0E48CugL5K7IYggr',
                      consumer_secret='xdxZJMjfmWDx13O03xdT1rkzPfKW443QDgPltsseN7cQYycOMv',
                      access_token_key='767445413599252480-motroziXYvzUPkD8y98S1Yg2uI7kyzJ',
                      access_token_secret='TY1MNxV0Ye7QoawsK852Sn5iE2GsZRDbj75NVALAF2Ct6')

    return api.GetUserTimeline(screen_name='stenkacziu', exclude_replies=True, include_rts=False)  # includes entities

def index(request):
    return HttpResponse("Hello, world. You're at the twit index.")    