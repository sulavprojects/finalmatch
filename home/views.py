from msilib.schema import Font
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .models import Fonts
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

def main(request):
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    allfonts = Fonts.objects.filter(publish = True)
    p = Paginator(allfonts, 5)
    page = request.GET.get('page')
    fontsfinal = p.get_page(page)
   

    context = {'fontsfinal': fontsfinal, 
                #'footer': footer, 
                'copyright': copyright,
                'websitedata': websitedata
                
    
    }
         
    return render(request , 'index.html',context)



def allfonts(request):
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    allfonts = Fonts.objects.filter(publish = True)
    p = Paginator(allfonts, 2)
    page = request.GET.get('page')
    fontsfinal = p.get_page(page)
    

    context = {'fontsfinal': fontsfinal,
               'title': 'all fonts',
               'websitedata': websitedata, 
                
    }

    return render(request , 'allfonts.html',context)





def fonts_details(request, slug):

    #snippet = get_object_or_404(snippet, slug=slug)

     
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    allfonts = Fonts.objects.order_by('-Total_downloads')
    title = Fonts.objects.filter(slug = slug).first()
    
    context = {
        'allfonts': allfonts[:2],
        'title': title,
        'websitedata': websitedata, 
        'copyright': copyright,
        
        
    }
    try:
        fonts_obj = Fonts.objects.filter(slug = slug).first()
        context['fonts_obj'] = fonts_obj
    except Exception as e:
        print(e) 

        
        
    return render(request , 'fonts_details.html' , context)
