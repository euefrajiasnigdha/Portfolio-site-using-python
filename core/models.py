from django.db import models

from django.db import models
from django.contrib.auth.models import User


# About Model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"



# Service Model
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service name")
    #description = models.TextField(verbose_name="About service")
    area = models.TextField(verbose_name="Working Area")
    Charge = models.CharField(max_length=10,verbose_name="Charges")
    image = models.ImageField(upload_to="services")
    def __str__(self):
        return self.name

    def area_as_list(self):
        return self.area.split(',')



# Recent Work Model
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title


# Client model
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client name")
    description = models.TextField(verbose_name="Client say")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name

#contact info
class Contact(models.Model):
    description = models.TextField(verbose_name="Contact/Address info")

    def __str__(self):
        return self.description

#All Tittles

class aboutTitle(models.Model):
    name = models.CharField(max_length=100, verbose_name="Enter About Title")

    def __str__(self):
        return self.name

class serviceTitle(models.Model):
    name = models.CharField(max_length=100, verbose_name="Enter Service Title")

    def __str__(self):
        return self.name

class portfolioTitle(models.Model):
    name = models.CharField(max_length=100, verbose_name="Enter Portfolio Title")

    def __str__(self):
        return self.name

class testimonialTitle(models.Model):
    name = models.CharField(max_length=100, verbose_name="Enter Testimonial Title")

    def __str__(self):
        return self.name

class adressTitle(models.Model):
    name = models.CharField(max_length=100, verbose_name="Enter Address bar Title")

    def __str__(self):
        return self.name



class contactTitle(models.Model):
    name = models.CharField(max_length=100, verbose_name="Contact Title")

    def __str__(self):
        return self.name


class FooterText(models.Model):
    name = models.CharField(max_length=100, verbose_name="Add Footer Text")

    def __str__(self):
        return self.name

class SlideImage(models.Model):
    name1 = models.CharField(max_length=100, verbose_name="Images name 1")
    description1 = models.CharField(max_length=100, verbose_name="Images Description")
    image1 = models.ImageField(upload_to="slideimage")
    name2 = models.CharField(max_length=100, verbose_name="Images name 2")
    description2 = models.CharField(max_length=100, verbose_name="Images Description 2")
    image2 = models.ImageField(upload_to="slideimage")
    name3 = models.CharField(max_length=100, verbose_name="Images name 3")
    description3 = models.CharField(max_length=100, verbose_name="Images Description 3")
    image3 = models.ImageField(upload_to="slideimage")


    def __str__(self):
        return self.name1



class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    job = models.CharField(max_length=100, verbose_name="Service Name")
    o_date = models.CharField(max_length=100, verbose_name="Date of Order")
    d_date = models.CharField(max_length=100, verbose_name="Estimated Completion Date")
    fn = models.CharField(max_length=100, verbose_name="First name")
    ln = models.CharField(max_length=100, verbose_name="Last name")
    ads = models.CharField(max_length=100, verbose_name="Phone")

    status = models.CharField(max_length=100, verbose_name="Current Status")




    def __str__(self):
        return self.user.username


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    update_at = models.TextField(null=True, blank=True)
    Developing_at = models.TextField(null=True, blank=True)
    Piloting_at = models.TextField(null=True, blank=True)
    Debug_at = models.TextField(null=True, blank=True)
    Ready_at = models.TextField(null=True, blank=True)

   # update = models.CharField(max_length=300, verbose_name="update")

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title