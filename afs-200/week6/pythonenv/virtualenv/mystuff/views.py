from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.You have met you doom. Take your time since you'll be here for awhile. Make some food and get comfy, and kick up your feet. This is the last place you're ever gonna know. Put on a movie if you like, because it's boring too. Not really boring just hard to pick up the code and if you need a distraction here you go. But worry not, you'll be doing the darn thing in no time. Professional or not, someone is gonna look for you to build with them. You just need to hang in there. What does polls have to do with it, what's polls but a single source connection. If you can make it out alive then you might see the light yet, if you try. Just don't let nobody catch you or your goose is cooked. Keep your wits about you and a creative instict intact to do what you want in this infinate world of possibilities.</h1>")