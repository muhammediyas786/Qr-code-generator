from django.shortcuts import render
from .models import Qr,background
import merge_and_texting.python as python

# Create your views here.


def home(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        link_from = request.POST.get('link_from')
        holder_status = request.POST.get('holder_status')
        
        link_from = str(link_from)
        link_from = link_from.upper()
        
        qr_code = Qr.objects.create(link=link,link_from=link_from,holder=holder_status)
        qr_code.save()

        Id = qr_code.id
        
        python.code_generating(qr_code.link,Id)
        python.merging(Id)
        python.Texting(Id,holder_status,link_from)

        image = '/image'+str(Id)+'.jpg'
        qr_code = Qr.objects.filter(id=Id).update(image=image)

        final_result = Qr.objects.filter(id=Id)

        return render(request, 'index.html',{'qr_code':final_result})




    return render(request,'index.html')