from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render
import string
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def index(request):
    params={'name':'mukesh','place':'nepal'}
    return render (request,'index.html',params)

def remove_punctuation(str1):
    removed_punctuation=''
    for i in str1:
        if i not in string.punctuation:
            removed_punctuation=removed_punctuation+i
    return removed_punctuation

def analyze(request):
    

    text=request.POST.get("text")
    text1=remove_punctuation(text)

    
    uppercase=request.POST.get("uppercase",'off')
    lowercase=request.POST.get("lowercase",'off')
    wordcount=request.POST.get("countword",'off')  
 


    if uppercase=='on':
        uppercased_text=text1.upper()
    else:
        uppercased_text="None"

    if lowercase=='on':
        lowercased_text=text1.lower()
    else:
        lowercased_text="None"

    if wordcount=='on':
         length=len(text1.split())
    else:
        length="NA"
    
    params={'analyzed_text':text1,'uppercase_text':uppercased_text,'lowercase_text':lowercased_text,'countword':length}
    return render(request,'analyze1.html',params)




