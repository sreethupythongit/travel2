from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from taskapp.models import Place, Team


def demo(request):
    obj=Place.objects.all()
    team_obj=Team.objects.all()
    return render(request, 'index.html',{'results':obj,'team_result':team_obj})

# def demo_old(request):
#     return render(request, 'indexold.html')


# def home(request):
#     name = 'india'
#     return render(request, 'home.html', {'obj': name})
#
#
# def about(request):
#     return render(request, 'about.html')
#
#
# def contact(request):
#     return HttpResponse("hi i am contact page")
#
#
# def details(request):
#     return HttpResponse("hi i am details page")
#
#
# def thanks(request):
#     return render(request, 'thanks.html')
#
#
# def caluculate(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     add = x + y
#     sub = x - y
#     mul = x * y
#     div = x / y
#
#     return render(request, 'result.html', {'add': add, 'sub': sub, 'mul': mul, 'div': div})
