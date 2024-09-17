from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Project
from .forms import ProfileForm, ProjectForm  # Profile과 Project 생성을 위한 폼들

# 포트폴리오 메인 페이지
def portfolio_main(request):
    profile = get_object_or_404(Profile)  # Profile이 없으면 404를 띄움
    projects = Project.objects.all()  # 모든 프로젝트 가져오기
    context = {
        'profile': profile,
        'projects': projects,
    }
    return render(request, 'portfolio/main.html', context)

# 포트폴리오 생성 페이지
def portfolio_create(request):
    if request.method == 'POST':
        # profile_form = ProfileForm(request.POST)
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            # profile_form.save()
            project_form.save()
            return redirect('portfolio_main')  # 생성 후 메인 페이지로 리다이렉트
    else:
        # profile_form = ProfileForm()
        project_form = ProjectForm()
    
    context = {
        # 'profile_form': profile_form,
        'project_form': project_form,
    }
    return render(request, 'portfolio/create.html', context)

# 포트폴리오 수정 페이지
def portfolio_update(request, id):
    profile = get_object_or_404(Profile, id=id)  # Profile이 없으면 404
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('portfolio_main')
    else:
        profile_form = ProfileForm(instance=profile)
    
    context = {
        'profile_form': profile_form,
    }
    return render(request, 'portfolio/update.html', context)
