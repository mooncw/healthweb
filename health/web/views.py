from django.shortcuts import render, redirect
from .models import Exercises
# from django.contrib.auth import get_user_model, get_user_model, authenticate, login
# from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def screen(request, id):
    exercise_data = Exercises.objects.get(name_en = id)
    return render(request, 'screen.html', {'exercise_data': exercise_data})

def testweb(request):
    return render(request, 'testweb.html')

def testweb2(request):
    return render(request, 'testweb2.html')

def testweb3(request):
    return render(request, 'testweb3.html')

# User1 = get_user_model()

# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         name = request.POST['name']

#         User1.objects.create_user(username=username, password=password, name=name)
#         return redirect('login')  # 회원가입 성공 시 로그인 페이지로 이동

#     return render(request, 'signup.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')  # 로그인 성공 시 홈 페이지로 이동

#     return render(request, 'login.html')


# @login_required
# def home(request):
#     return render(request, 'home.html')