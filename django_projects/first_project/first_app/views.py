from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic,Webpage,Users
# Create your views here.

def index(request):
    webpages_list =AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}

    return render(request, 'first_app/index.html', context=date_dict)

def help(request):
    my_dict = {'insert_me':"Hello! I'm from views.py! "}
    return render(request, 'first_app/help.html', context=my_dict)

def users(request):
    user_list =Users.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'first_app/users.html',context=user_dict)
