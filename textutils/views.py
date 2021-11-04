# i have created this file - Manav aggarwal
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyse(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    removePunc = request.POST.get('removePunc', 'off')
    uppercaseEach = request.POST.get('uppercaseEach', 'off')
    lowercaseEach = request.POST.get('lowercaseEach', 'off')
    newLineRemover = request.POST.get('newLineRemover', 'off')
    ExtraSpaceRemover = request.POST.get('ExtraSpaceRemover', 'off')
    charCounter = request.POST.get('charCounter', 'off')
    print(djtext, removePunc)
    Punctations = '''!@#$%^&*()_{}[]''"":;.,?-/\|`~'''
    analysed = ""
    if removePunc == 'on':
        operations = "remove Punctutaions"
        for char in djtext:
            if char not in Punctations:
                analysed = analysed + char
        djtext = analysed
    elif (uppercaseEach == 'on'):
        analysed = ""
        operations = "Capitalize each character"
        for char in djtext:
            analysed = analysed + char.upper()
    elif (lowercaseEach == 'on'):
        analysed = ""
        operations = "Lowercase each character"
        for char in djtext:
            analysed = analysed + char.lower()
    elif (newLineRemover == 'on'):
        analysed = ""
        operations = "Every New Line Removed"
        for char in djtext:
            if (char != '\n' and char != '\r'):
                analysed = analysed + char
    elif (ExtraSpaceRemover == 'on'):
        analysed = ""
        operations = "Every Extra space is Removed"
        for index,char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index + 1] == ' '):
                analysed = analysed + char
    elif (charCounter == 'on'):
        analysed = ""
        count = 0
        for char in djtext:
            if(char != ' '):
                count += 1
                analysed = analysed + char
        operations = "The total number of char are:"
        params = {'removePunc': operations,"charCount":count, 'analyse_text': analysed}
        return render(request, 'analyse.html', params)

    else: 
        analysed = djtext

    params = {'removePunc': operations, 'analyse_text': analysed}
    return render(request, 'analyse.html', params)
