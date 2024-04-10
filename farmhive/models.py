from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Home(models.Model):
    top_home_image = models.ImageField(upload_to='farm_hive_home_images')
    title_of_content = models.CharField(max_length=120, default='Tech Farm Hub')
    short_content = models.CharField(max_length=255, default='Tech Farm Hub')

    def __str__(self) -> str:
        return self.title_of_content


class Departments(models.Model):
    name = models.CharField(max_length=50, default='Farm Hive')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}, {self.date_created}"

class SubDepartment(models.Model):
    departments = models.ForeignKey(Departments, on_delete=models.CASCADE)
    sub_department_name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
 
    def __str__(self) -> str:
        return self.sub_department_name


class DigitalFarms(models.Model):
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=150)
    title = models.CharField(max_length=255, default='Farm Hive')
    description = models.CharField(max_length=500)
    total_departments = models.IntegerField(default=0, blank=True)
    upload_video = models.FileField(upload_to='digifarms_images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at}, {self.department_name}"

@receiver(post_save, sender=DigitalFarms)
def increment_total_departments(sender, instance, created, **kwargs):
    if created:
        instance.total_departments = DigitalFarms.objects.count()
        instance.save()



class AboutFarmHive(models.Model):
    title = models.CharField(max_length=120)
    short_content = models.CharField(max_length=500)
    full_content = models.TextField()

    def __str__(self) -> str:
        return self.title
    

class VideoGellary(models.Model):
    title = models.CharField(max_length=150, default='Farm Hive')
    video = models.FileField(upload_to='farm_hive_vedos')
    created_at = models.DateTimeField(auto_now_add=True)


class Pictures(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title