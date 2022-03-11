from django.core.exceptions import MiddlewareNotUsed

from django.shortcuts import redirect, render

from django.contrib.auth.models import User, auth

from django.contrib import messages

from django.http import JsonResponse

from .models import Diary


# Create your views here.

def register(request):

    if request.method =='POST':

        first_name = request.POST['first_name']

        last_name = request.POST['last_name']

        username = request.POST['username']

        email = request.POST['email']

        password = request.POST['password']

        print(email)

        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)

        user.save();

        print('success')

        return redirect('/')

    else:

        return render(request, 'diary/registration.html')


def login(request):

    if request.method =='POST':

        username = request.POST['username']

        password = request.POST['password']


        user = auth.authenticate(username=username,password=password)
        
        

        us = User.get_username
        

        if user is not None:
            

            # return redirect('display')

            # print(dir(request.session))

            request.session['user_id'] = user.id

            request.session['user_username'] = user.username

            user = request.session.get('session_key')

           

            return redirect('home')
            
            

        else:

            # messages.info(request, "Invalid Credentials")

            # # return redirect('')

            # return JsonResponse(

            #     {'success': False},

            #     safe=False

            # )

            return render(request, 'diary/login.html')


    else:

        return render(request, 'diary/login.html')


def home(request):

    user = request.session.get('user_username')

    userid = request.session.get('user_id')

    diary=Diary.objects.filter(userid=userid)
    

    return render(request, 'diary/home.html',{"users":user, "userid":userid, "diaries":diary})


def add(request):

    if request.method=='POST':

        title = request.POST['title']

        body = request.POST['body']

        userid = request.session.get('user_id')

        print(userid)

        diary=Diary.objects.create(title=title, body=body, userid=userid)

        return redirect('home')

    else:

        return render(request, 'diary/add.html')


def view(request):

    user = request.session.get('user_username')

    id=request.GET['id']
    diary=Diary.objects.filter(id=id)

    print(user) 
    

    return render(request, 'diary/view.html',{"diary":diary})