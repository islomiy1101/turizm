from django.shortcuts import render
from .models import Customer
def index(request):
    data=Customer.objects.all()
    context={
        'data':data
    }
    return render(request,'index.html',context)

def single_page(requuest,pk):
    print(pk)
    data=Customer.objects.get(id=pk)
    context = {
        'data': data
    }
    data.custom_id="%05i" % (pk,)
    data.url=f'http://127.0.0.1:8000/customer/{pk}/'
    data.save()
    return render(requuest,'single_page.html',context)