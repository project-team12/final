from django.shortcuts import render

def home(request):
    context={}
    return render(request,"home.html",context)
def input(request):
    return render(request, 'input.html',{})
