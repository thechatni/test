from django.shortcuts import render
from django.contrib.sessions.models import Session

from django.http import JsonResponse, HttpResponse
import json


def home(request):
    request.session['one'] = 0
    return render(request, 'home.html')


def three(request):
    if (request.POST):
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak:")
            audio = r.listen(source)
        try:
            text1 = r.recognize_google(audio)
            output = " " + text1
        except sr.UnknownValueError:
            output = "Please press record when you are ready to speak"
        except sr.RequestError as e:
            output = "Could not request results; {0}".format(e)

        context = {}
        context['out'] = output
        return HttpResponse(json.dumps(context))
    context = {}
    context['out'] = output
    return HttpResponse(json.dumps(context))
