from django.shortcuts import render
from django.http import HttpResponse
from . models import place
from . models import object



def demo(request):

    obj=place.objects.all()
    obj1=object.objects.all()

    return render(request,'index.html',{'result':obj,'result1':obj1})



#def about(request):
    #return render(request,'about.html')

#def contact(request):
    #return HttpResponse("this is contact")

#def form(request):
   # return render(request,'form.html')

#def addition(request):
   # x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #z=x+y
    #return render(request,'result.html',{'result':z})
