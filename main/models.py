from django.db import models
from django.conf import settings


class ContactPage(models.Model):
    phone_number = models.IntegerField()
    email_address = models.EmailField()
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.email_address
    

class HeaderImages(models.Model):
    select_image = models.ImageField(upload_to='header_images', blank=False)
    short_description = models.CharField(max_length=150, blank=True)
    short_content = models.CharField(max_length=200, default='Tech Farm Hub')

    def __str__(self):
        return self.short_description
    
class FooterArea(models.Model):
    update_contact = models.CharField(max_length=15, unique=True, blank=False)
    address = models.TextField()
    work_hours = models.DateTimeField(auto_now_add=False)

class Partners(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    image = models.ImageField(upload_to='partners_image', null=False)

    def __str__(self):
        return self.name
    

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news_article_images', null=False)
    content = models.TextField()
    full_content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Projects(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    descirption = models.CharField(max_length=100)
    country = models.CharField(max_length=100, unique=False, blank=False, default='Ghana, Koforidua')
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name of Project {self.name} Country {self.country}'
    

class FarmProject(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='farmproject_images', blank=False)

    def __str__(self):
        return self.project.name


class MultimediaProject(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='multimediaproject_images', blank=False)

    def __str__(self):
        return self.project.name

  
class TechProject(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='techproject_images', blank=False)

    def __str__(self):
        return self.project.name

class Gellary(models.Model):
    image = models.ImageField(upload_to='gellary_images')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Search(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='course_pictures', null=True, blank=True)
    subscribers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subscribed_courses')
    
    def __str__(self):
        return self.title

class Module(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Videos(models.Model):
    title = models.CharField(max_length=100)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='course_videos')

    def __str__(self):
        return self.title
    

class Team(models.Model):
    TITLE = {
        ('mr', 'Mr'),
        ('mrs', 'Mrs'),
        ('ms', 'Ms')
    }

    title = models.CharField(max_length=10, choices=TITLE)
    name_of_team_member = models.CharField(max_length=100, unique=True)
    positon = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='team_member_images')
    short_content = models.CharField(max_length=255, blank=True, default='Tech Farm Hub')
    full_content = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title} - {self.name_of_team_member}"