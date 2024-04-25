from django.db import models
from django.conf import settings

class HomeLinks(models.Model):
    address = models.CharField(max_length=100, blank=False)
    contact = models.CharField(max_length=15, blank=False)
    facebook_loink = models.URLField()
    x_link = models.URLField()
    linked_in_link = models.URLField()
    google_link = models.URLField()
    instagram_link = models.URLField()


class ContactPage(models.Model):
    phone_number = models.IntegerField()
    email_address = models.EmailField()
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.email_address
    

class ChangeHeaderImages(models.Model):
    select_image = models.ImageField(upload_to='header_images', blank=False)
    short_description = models.CharField(max_length=150, blank=True)
    short_content = models.CharField(max_length=200, default='Tech Farm Hub')

    def __str__(self):
        return self.short_description


class About(models.Model):
    title = models.CharField(max_length=120, blank=False, unique=True)
    image = models.ImageField(upload_to='about_images')
    content = models.TextField(max_length=2000, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class FooterArea(models.Model):
    update_contact = models.CharField(max_length=15, unique=True, blank=False)
    address = models.TextField()
    work_hours = models.DateTimeField(auto_now_add=False)


class Partners(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    image = models.ImageField(upload_to='partners_image', null=False)
    short_content = models.CharField(max_length=255)

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
    videofile = models.FileField(upload_to='project_video', blank=False, default='')
    country = models.CharField(max_length=100, unique=False, blank=False, default='Ghana, Koforidua')
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name of Project {self.name} Country {self.country}'
    

class Search(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

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
    

class Services(models.Model):
    name_of_service = models.CharField(max_length=100, blank=False, unique=True)
    content = models.CharField(max_length=255, blank=False, unique=True)
    full_content = models.TextField(max_length=2000, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name_of_service
    

class Techhive(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Courses(models.Model):
    department = models.ForeignKey(Techhive, on_delete=models.CASCADE)
    name_of_course = models.CharField(max_length=150, unique=True, blank=False)
    videofile = models.FileField(upload_to="tech_hive_videos", unique=True)
    description = models.CharField(max_length=255, unique=True, blank=False)
    cate_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name_of_course
    