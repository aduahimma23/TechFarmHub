from django.db import models
from django.conf import settings

class SocialMediaLinks(models.Model):
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedIn = models.URLField(blank=True, null=True)
    google = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.facebook, self.twitter, self.linkedIn, self.google, self.instagram


class ContactPage(models.Model):
    phone_number = models.IntegerField()
    email_address = models.EmailField()
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.email_address
    

class ChangeHeaderImages(models.Model):
    image = models.ImageField(upload_to='header_images', blank=False)
    description = models.CharField(max_length=150, blank=True)
    content = models.CharField(max_length=200, default='Tech Farm Hub')

    def __str__(self):
        return self.description


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
    logo = models.ImageField(upload_to='partners_image', null=False)
    content = models.CharField(max_length=255)

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
    
class ChangeProjectHeaderImage(models.Model):
    name = models.CharField(max_length=20, blank=False, default='Project Name')
    image = models.ImageField(upload_to='project_header_image', blank=True)
    short_content = models.CharField(max_length=120, blank=True)

    def __str__(self) -> str:
        return self.name
    

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
    position = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='team_member_images')
    bio = models.TextField()
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
    

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Section(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name_of_course = models.CharField(max_length=150, unique=True, blank=False)
    videofile = models.FileField(upload_to="tech_hive_videos", unique=True)
    description = models.CharField(max_length=255, unique=True, blank=False)
    cate_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name_of_course
    
class FarmhiveGallery(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    image_file = models.ImageField(upload_to='gallery', blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class MultimediahiveGallery(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    image_file = models.ImageField(upload_to='gallery', blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
class TechhiveGallery(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    image_file = models.ImageField(upload_to='gallery', blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    

class FarmHive(models.Model):
    departments = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True, blank=False)
    videofile = models.FileField(upload_to='farm_hive', unique=True, blank=False)
    description = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class MultimediaHive(models.Model):
    departments = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True, blank=False)
    videofile = models.FileField(upload_to='farm_hive', unique=True, blank=False)
    description = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class TechHive(models.Model):
    departments = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True, blank=False)
    videofile = models.FileField(upload_to='farm_hive', unique=True, blank=False)
    description = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class Prices(models.Model):
    tech_hive_price = models.ForeignKey(TechHive, on_delete=models.CASCADE)
    farm_hive_price = models.ForeignKey(FarmHive, on_delete=models.CASCADE)
    multimedia_hive_price = models.ForeignKey(MultimediaHive, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=6, blank=False)
    currency = models.CharField(max_length=3)
    date_created = models.DateField(auto_now_add=True)

class Promotions(models.Model):
    name = models.CharField(max_length=255)
    is_promotion_active = models.BooleanField(default=False)
    get_amount = models.ForeignKey(Prices, on_delete=models.CASCADE)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    
    def calculate_discounted_amount(self):
        if self.is_promotion_active:
            discount_amount = self.get_amount.amount - (self.get_amount.amount * self.discount_percentage / 100)
            return discount_amount
        else:
            return self.get_amount

class Locations(models.Model):
    country = models.CharField(max_length=255, unique=True, blank=False)
    country_flag = models.ImageField(upload_to='country_flags')
    city = models.CharField(max_length=255, unique=True, blank=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.country, self.city, self.date_created
