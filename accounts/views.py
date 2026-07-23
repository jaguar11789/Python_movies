from django.contrib.auth.models import User
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

        print("POST 데이터:", request.POST)
        print("폼 유효성:", profile_form.is_valid())
        print("폼 에러:", profile_form.errors)

        if profile_form.is_valid():
            username = request.POST.get('userId')
            password = request.POST.get('password')
            email    = request.POST.get('email')

            user = User.objects.create_user(
                username = username,
                password = password,
                email    = email
            )

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('accounts:login')

    else:
        profile_form = ProfileForm()

    context = {'profile_form': profile_form}

    return render(request, 'accounts/signup.html', context)