from django.shortcuts import render, redirect
from .models import Exercises
# from django.contrib.auth import get_user_model, get_user_model, authenticate, login
# from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'web/index.html')

# def index2(request):
#     return render(request, 'web/index2.html')

def screen(request, id):
    exercise_data = Exercises.objects.get(name_en = id)
    return render(request, 'web/screen.html', {'exercise_data': exercise_data})

# def screen2(request, id):
#     exercise_data = Exercises.objects.get(name_en = id)
#     return render(request, 'web/screen2.html', {'exercise_data': exercise_data})

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