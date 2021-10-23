from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


from .serializers import TweetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.decorators import parser_classes

from .models import Tweet

from django.contrib.auth.models import User


# Create your views here.


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
    user1 = User.objects.get(username='soby')
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


# class tweetCreate(ListAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer

#     def post(self, request, *args, **kwargs):
#         file = request.data['file']
#         image = Tweet.objects.create(image=file)
#         return HttpResponse('uploaded')
