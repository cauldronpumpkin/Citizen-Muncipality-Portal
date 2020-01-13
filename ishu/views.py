from django.shortcuts import render , get_object_or_404, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from .models import  Product
from .forms import Product_Form
import rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response


def homepage(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html", {})

def citizenpage(request, *args, **kwargs):
    print(request.user)
    obj = {
        'list': [1,2,3]
    }
    return render(request, "detail.html", obj)

def form12(request):
    form = Product_Form(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "detail.html", context)

def delete(request, myid):
    obj = get_object_or_404(Product, id=myid)
    # if request.method == 'POST':
    obj.delete()
    return redirect('../')
    context = {
        "object":obj
    }
    return render(request, "delete.html", context)

def product_view(request):
    return render(request, "count.html", {})

def json_api(request):
    obj =  {
        'Price': 100,
        'Grade': 'A',
    }
    return JsonResponse(obj)

class ChartsData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        queryset = Product.objects.all()
        context = {
            "object_list": queryset
        }
        rows, cols = (4, 4) 
    
        # method 2a 
        l1 = [0,0,0,0]
        l2 = [0,0,0,0]
        l3 = [0,0,0,0]
        l4 = [0,0,0,0]
        for instance in queryset:
            if(instance.locality == 'kharghar'):
                if(instance.title == 'aids'):
                    l1[0] += 1
                elif(instance.title == 'malaria'):
                    l1[1] += 1
                elif(instance.title == 'dengue'):
                    l1[2] += 1
                elif(instance.title == 'loose motions'):
                    l1[3] += 1
            elif(instance.locality == 'thane'):
                if(instance.title == 'aids'):
                    l2[0] += 1
                elif(instance.title == 'malaria'):
                    l2[1] += 1
                elif(instance.title == 'dengue'):
                    l2[2] += 1
                elif(instance.title == 'loose motions'):
                    l2[3] += 1
            elif(instance.locality == 'dadar'):
                if(instance.title == 'aids'):
                    l3[0] += 1
                elif(instance.title == 'malaria'):
                    l3[1] += 1
                elif(instance.title == 'dengue'):
                    l3[2] += 1
                elif(instance.title == 'loose motions'):
                    l3[3] += 1
            elif(instance.locality == 'andheri'):
                if(instance.title == 'aids'):
                    l4[0] += 1
                elif(instance.title == 'malaria'):
                    l4[1] += 1
                elif(instance.title == 'dengue'):
                    l4[2] += 1
                elif(instance.title == 'loose motions'):
                    l4[3] += 1

        lab = ['aids','malaria','dengue','loose motions']
        loc = ['kharghar','thane','dadar','andheri']
        #print(request.user)
        data =  {
            'label': lab,
            'local': loc, 
            'kharghar': l1,
            'thane': l2,
            'dadar': l3,
            'andheri': l4,
        }
        return Response(data)
