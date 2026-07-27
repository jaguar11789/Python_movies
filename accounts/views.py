import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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

@login_required
def mypage(request):

    profile = request.user.profile
    context = {'profile': profile}

    return render(request, 'accounts/mypage.html', context)

@login_required
def profile_update(request):

    profile = request.user.profile

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)

        if profile_form.is_valid():
            profile_form.save()

            request.user.email = request.POST.get('email')
            request.user.save()

            return redirect('accounts:mypage')

    else:
        profile_form = ProfileForm(instance=profile)

    context = {
        'profile': profile,
        'profile_form': profile_form
    }

    return render(request, 'accounts/profile_update.html', context)

@login_required
def password_update(request):

    if request.method == 'POST':

        data = json.loads(request.body)

        current_password = data.get('current_password')
        new_password     = data.get('password')

        if not request.user.check_password(current_password):

            return JsonResponse({
                'success': False,
                'message': '현재 비밀번호가 올바르지 않습니다.'
            })

        request.user.set_password(new_password)
        request.user.save()

        return JsonResponse({
            'success': True,
            'message': '비밀번호가 변경되었습니다.\n다시 로그인해 주세요.'
        })

    return render(request, 'accounts/password_update.html')

@login_required
def accounts_delete(request):

    if request.method == 'POST':
        data = json.loads(request.body)

        reason = data.get('reason')
        print('회원 탈퇴 사유:', reason)
        request.user.delete()

        return JsonResponse({
            'success': True,
            'message': '회원 탈퇴가 완료되었습니다.'
        })

    return JsonResponse({
        'success': False,
        'message': '잘못된 요청입니다.'
    }, status=400)