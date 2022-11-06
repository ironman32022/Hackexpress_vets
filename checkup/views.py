from django.shortcuts import render

from django.shortcuts import render
from django.core.files.storage import default_storage


from keras.preprocessing import image
# from tensorflow import Graph,Session
# from tensorflow import Session
import tensorflow as tf
import cv2
import os
import json
import numpy as np
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


from django.shortcuts import render
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
import numpy as np


#function to handle an uploaded file.
from .cnn import cnn


# Create your views here.

def index1(request):
    return render(request, 'checkup/checkup.html')

def predict(request):
    if request.method == 'POST' and  'cnnBtn' in request.POST:
        

        upload1 = request.FILES['upload1']
        fss = FileSystemStorage()
        file = fss.save(upload1.name, upload1)
        file_url = fss.url(file)
        print(file_url)
        img_path='static'+file_url

        
        classe = cnn(img_path)
        print(file)
        print(file_url)
        # print(classe)

        context={'classe':classe,'file_url':file_url}
    
        if classe == 'healthy':
            return render(request, 'checkup/home1.html', context)   
        
        else:
            return render(request, 'checkup/home1.html', context)   
    return render(request, 'checkup/home.html')  
