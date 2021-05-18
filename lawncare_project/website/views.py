from django.shortcuts import render
from . import models
from service import models as models_service


# def newletter(request):
#     newletter = request.POST.get('email')
#     retour = request.META.get('HTTP_REFERER')# Pour rediriger sur la meme page
#     models.Newletter.objects.create(email = newletter) # Pour enegister dans la base de donner
#     return redirect(retour,'index')

def index(request):
    banners = models.Banner.objects.filter(status=True)
    prestations = models_service.Prestation.objects.filter(status=True)
    abouts =  models.About.objects.filter(status=True)
    aboutoptions =models.OptionAbout.objects.filter(status=True)
    return render(request,'index.html',locals())

def about(request):
    
    return render(request,'about.html',)

def blog_single(request):
    
    return render(request,'blog-single.html',)

def blog(request):
    
    return render(request,'blog.html',)

def gallery(request):
    
    return render(request,'gallery.html',)

def contact(request):
    
    return render(request,'contact.html',)

def service(request):
    
    return render(request,'services.html',locals())
# Create your views here.
