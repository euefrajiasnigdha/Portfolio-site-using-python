from django.views.generic import TemplateView
from .models import *
from django.shortcuts import render
from core.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



from django.shortcuts import render, get_object_or_404
from .models import Blog



def home(request):
    return render(request, 'home.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'core/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given.Please Back to the Login page and Try again!")
    else:
        return render(request, 'core/login.html', {})







class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['services'] = reversed(Service.objects.all())
        context['works'] = RecentWork.objects.all()
        context['clients'] = Client.objects.all()
        context['contact'] = Contact.objects.first()
        context['contactT'] = contactTitle.objects.first()
        context['aboutT'] = aboutTitle.objects.first()
        context['clientsT'] = testimonialTitle.objects.first()
        context['servicesT'] = serviceTitle.objects.first()
        context['portfolioT'] = portfolioTitle.objects.first()
        context['addressT'] = adressTitle.objects.first()
        context['footer'] = FooterText.objects.first()
        context['slideimage'] = SlideImage.objects.first()





        return context


def allblogs(request):
    blogs = Blog.objects
    return render(request, 'core/allblogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blogdetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'core/detail.html', {'blog': blogdetail})