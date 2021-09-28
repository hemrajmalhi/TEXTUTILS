from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return render(request, 'index.html')

def analyze(request):
    djtext=request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    ExtraSpaceRemove = request.POST.get('ExtraSpaceRemove', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc=='on':
        punctuations ='''@!{}()[]\/|"<>'~`#$%^&*:;.,?'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'remove punctuation', 'analyzed_text':analyzed}
        djtext=analyzed

    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Uppercase', 'analyzed_text':analyzed}
        djtext = analyzed

    if(newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed=analyzed+char
        params={'purpose':'newlineremover', 'analyzed_text':analyzed}
        djtext = analyzed

    if(ExtraSpaceRemove=='on'):
        analyzed =""
        for index, char in enumerate(djtext):
            if not (djtext[index] ==" " and djtext[index+1] ==" "):
                analyzed=analyzed+char
        params={'purpose':'ExtraSpaceRemove', 'analyzed_text':analyzed}
        djtext = analyzed

    if (charcount == 'on'):
        analyzed=0
        for char in djtext:
            if char!=" ":
                analyzed+=1

        params = {'purpose': 'charcount', 'analyzed_text': analyzed}
    if(removepunc!='on' and newlineremover!='on' and fullcaps!='on' and ExtraSpaceRemove!='on' and charcount  !="on" ):
        return HttpResponse("ERROR")

    return render(request, 'analyze.html', params)



