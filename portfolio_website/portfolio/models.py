# portfolio/models.py

from django.db import models

# 1. 사용자 프로필 모델
class Profile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()  # 소개글
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    skill = models.CharField(max_length=100)
    # profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True) -> s3 X 
    # resume = models.FileField(upload_to='resumes/', blank=True, null=True)  # 이력서 파일 -> s3 x

    def __str__(self):
        return self.name, self.skill

# 2. 프로젝트 모델
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    skill = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField(blank=True, null=True)  # 프로젝트 URL

    def __str__(self):
        return self.title

# 3. 블로그/뉴스 모델
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def __str__(self):
        return self.title


