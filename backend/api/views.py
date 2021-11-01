from functools import partial
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


from .serializers import TweetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.decorators import parser_classes

from .models import Tweet, Like

from django.contrib.auth.models import User


# Create your views here.


user1 = User.objects.get(username='soby')


@api_view(['GET'])
def home(request):
    api_urls = {
        'home': 'ss',
        'profile': 'saa',
        'tweet': 'fff',
        'register': 'ddd',
        'login': 'fff',
        'search': 'ddf'


    }
    return Response(api_urls)


@api_view(['GET'])
def tweetList(request):
    tweet = Tweet.objects.filter(author=user1)
    serializer = TweetSerializer(tweet, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def tweetDetail(request, pk):
    tweet = Tweet.objects.get(code=pk)
    serializer = TweetSerializer(tweet, many=False)

    return Response(serializer.data)


@api_view(['POST'])
@parser_classes([FormParser, MultiPartParser])
def tweetCreate(request):
    serializer = TweetSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
@parser_classes([FormParser, MultiPartParser])
def tweetLike(request, pk):
    tweet = Tweet.objects.get(code=pk)

    # check if user has liked the tweet before so next click unlikes it
    hasLiked = Like.objects.get(code=pk, likedBy=user1)
    if hasLiked:
        data = {"likes": tweet.likes - 1}
        Like.objects.get(likedBy=user1, tweetcode=pk).delete()
    else:
        data = {"likes": tweet.likes + 1}
        Like(likedBy=user1, tweetcode=pk)

    serializer = TweetSerializer(instance=tweet, data=data, partial=True)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def tweetDelete(request, pk):
    tweet = Tweet.objects.get(code=pk)
    tweet.delete()

    return Response('delete successful')
