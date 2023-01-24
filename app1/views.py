from django.shortcuts import render
from app1.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    tn=input('Enter topic_name')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse('Topic is insert successfully')


def insert_webpage(request):
    tn=input('Enter topic_name')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    name=input('Enter name:')
    url=input('enter url: ')
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    return HttpResponse('Webpage data is Inserted')

def insert_accessrecord(request):
    tn=input('Enter topic_name')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    name=input('Enter name:')
    url=input('enter url: ')
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    date=input('Enter a date: ')
    A=AccessRecord.objects.get_or_create(name=W,date=date)[0]
    A.save()
    return HttpResponse('AccessRecords data is Inserted')
