from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse 
from django.urls import reverse
from .forms import *
import numpy as np
from PIL import Image
from .utils import convert

# Create your views here.
 

def upload_qr(request):
    form = QRForm()
    if request.method == 'POST':
        form = QRForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['image']
            pil_img = Image.open(image)
            cv_image = np.array(pil_img)
            data = convert(cv_image)
            print(data)
            form.save()
            return render(request,'App_QR/result.html', context={'data':data, 'image':image})
        else:
            form = QRForm()
    return render(request, 'App_QR/index.html', {'form': form})            

def success(request): 
    return HttpResponse('successfully uploaded')     