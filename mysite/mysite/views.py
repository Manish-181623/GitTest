from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


# def about(request):
#     return HttpResponse("Hello About")


def analyze(request):
    # Get The Text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
   
    # Check which checkbox is on
    if removepunc == "on":
     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
     analyzed = ""
     for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
     params = {'purpose': "Removed Punctuations", 'analyzed_text': analyzed}
     # Analyze Text
     return render(request, 'analyze.html', params)

    elif fullcaps=="on":
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.upper()
        params = {'purpose': "Changed To UPPERCASE", 'analyzed_text': analyzed}
        # Analyze Text
        return render(request, 'analyze.html', params)

    elif newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char!="\n":
                analyzed = analyzed + char
        params = {'purpose': "Removed New Line", 'analyzed_text': analyzed}
        # Analyze Text
        return render(request, 'analyze.html', params)
    
    elif extraspaceremover=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)


    else:
        return HttpResponse('Error')

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")


# def spaceremove(request):
#     return HttpResponse("space remover back")

# def charcount(request):
#     return HttpResponse("charcount ")
