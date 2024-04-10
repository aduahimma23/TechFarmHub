from django.contrib import admin
from .models import (ContactPage, HeaderImages, Partners, NewsArticle, Projects, FarmProject, MultimediaProject, TechProject,
                     Gellary, Search, Department, Course, Module, Videos)

@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email_address', 'location', 'address')

@admin.register(HeaderImages)
class HeaderImagesAdmin(admin.ModelAdmin):
    list_display = ('select_image', 'short_description', 'short_content')

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'date_published')
    search_fields = ('title', 'image', 'date_published')

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'content', 'date_created')
    search_fields = ('name', 'country', 'content', 'date_created')

@admin.register(FarmProject)
class FarmProjectAdmin(admin.ModelAdmin):
    list_display = ('project', 'image')

@admin.register(MultimediaProject)
class MultimediaProjectAdmin(admin.ModelAdmin):
    list_display = ('project', )

@admin.register(TechProject)
class TechProjectAdmin(admin.ModelAdmin):
    list_display = ('project', )

@admin.register(Gellary)
class GellaryAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'description', 'uploaded_at')

@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'created_at', 'instructor', 'department')

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('title', 'module')

