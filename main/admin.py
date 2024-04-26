from django.contrib import admin
from .models import *

admin.site.register(ChangeProjectHeaderImage)


@admin.register(SocialMediaLinks)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('facebook', 'twitter', 'linkedIn', 'google', 'instagram')

@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email_address', 'location', 'address')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('title', 'name_of_team_member', 'position', 'date_joined')

@admin.register(ChangeHeaderImages)
class HeaderImagesAdmin(admin.ModelAdmin):
    list_display = ('select_image', 'short_description', 'short_content')

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'date_published')
    search_fields = ('title', 'image', 'date_published')

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'content', 'date_created')
    search_fields = ('name', 'country', 'content', 'date_created')



@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
