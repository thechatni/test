from django.shortcuts import render
from django.contrib.sessions.models import Session
import speech_recognition as sr

def home(request):

    request.session['wrong'] = 0
    return render(request,'home.html')


def narration(request):

    return render(request,'narration.html')

def speech_to_text(request):
    data = request.POST.get('record')
    wrong = request.session.get('wrong')
    import speech_recognition as sr
    word1 = 'Jeep'
    judge = 'OK'
    context = {}
    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        text1 = r.recognize_google(audio)
        if word1 in text1:
            judge = "Hmm, I see"
        else:
            judge = "Yeah, not sure about that"
            wrong=wrong+1
        output = " " + text1
    except sr.UnknownValueError:
        output = "Please press record when you are ready to speak"
    except sr.RequestError as e:
        output = "Could not request results; {0}".format(e)
    context['data'] = output
    context['judge'] = judge
    request.session['wrong'] = wrong
    return render(request,'speech_to_text.html',context)

def two(request):
    data = request.POST.get('record')
    wrong = request.session.get('wrong')
    import speech_recognition as sr
    word2 = 'blue'
    judge = 'OK'
    context = {}
    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        text1 = r.recognize_google(audio)
        if word2 in text1:
            judge = "Hmm, I see"
        else:
            judge = "Yeah, not sure about that"
            wrong=wrong+1
        output = " " + text1
    except sr.UnknownValueError:
        output = "Please press record when you are ready to speak"
    except sr.RequestError as e:
        output = "Could not request results; {0}".format(e)
    context['data'] = output
    context['judge'] = judge
    request.session['wrong'] = wrong
    return render(request,'two.html',context)

def three(request):
    data = request.POST.get('record')
    wrong = request.session.get('wrong')
    import speech_recognition as sr
    word3 = '1962'
    judge = 'OK'
    context = {}
    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        text1 = r.recognize_google(audio)
        if word3 in text1:
            judge = "Hmm, I see"
        else:
            judge = "Yeah, not sure about that"
            wrong=wrong+1
        output = " " + text1
    except sr.UnknownValueError:
        output = "Please press record when you are ready to speak"
    except sr.RequestError as e:
        output = "Could not request results; {0}".format(e)
    context['data'] = output
    context['judge'] = judge
    request.session['wrong'] = wrong
    
    return render(request,'three.html',context)

def decision(request):
    data = request.POST.get('record')
    wrong = request.session.get('wrong')
    import speech_recognition as sr
    if(wrong>=2):
        final = "I don't believe you are telling the truth. You are now a prime suspect!"
    else:
        final = "Yep, your answers check out. Sorry for disturbing you. You're free to go"
    context = {}
    context['final'] = final
    
    return render(request,'decision.html',context)
