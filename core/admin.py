
from django.contrib import admin
from core.models import UserProfileInfo, User
from .views import *
from .models import Blog
admin.site.register(Blog)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(RecentWork)
admin.site.register(Client)
admin.site.register(Contact)

#Regiatering tittlefield

admin.site.register(aboutTitle)
admin.site.register(serviceTitle)
admin.site.register(portfolioTitle)
admin.site.register(testimonialTitle)
admin.site.register(contactTitle)
admin.site.register(adressTitle)
admin.site.register(FooterText)
admin.site.register(SlideImage)
#admin.site.register(UserProfileInfo)


@admin.register(UserProfileInfo)
class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'portfolio_site', 'profile_pic', 'job', 'o_date', 'd_date', 'fn', 'ln', 'ads', 'status')
    fields = ['user', 'portfolio_site', 'profile_pic', 'job', 'o_date', 'd_date', 'fn', 'ln', 'ads', 'status']
    search_fields = ["user__username", "job", "o_date", "d_date", "fn", "ln", "ads", "status"]





