from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from .form import ProfileForm

def logout_view(request):
    logout(request)

    return redirect('index')

def signup(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)

        if profile_form.is_valid():
            username = request.POST.get('userId')
            password = request.POST.get('password')
            email    = request.POST.get('email')

        # 아이디 중복 확인
        if profile_form.is_valid():
            if User.objects.filter(username=username).exists():
                context = {
                    'profile_form': profile_form,
                    'error': '이미 사용 중인 아이디입니다.'
                }
                return render(request, 'accounts/signup.html', context)

            user = User.objects.create_user(
                username = username,
                password = password,
                email    = email
            )

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            context = {'signup_success': True}

            return render(request, 'accounts/signup.html', context)

    else:
        profile_form = ProfileForm()

    context = {'profile_form': profile_form}

    return render(request, 'accounts/signup.html', context)

def check_username(request):
    username = request.GET.get('username')

    exists = User.objects.filter(username=username).exists()

    return JsonResponse({'exists': exists})