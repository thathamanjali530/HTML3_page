from django.shortcuts import render

# Create your views here.
def firstapp2(request):
    return render(request,'firstapp2.html')
def secondapp2(request):
    return render(request,'secondapp2.html')