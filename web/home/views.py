from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .form import DangKy
from .form import UploadForm
from django.http import  HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Post


def index(request):
    return render(request, 'index.html')
def album(request):
    data = {'Post': Post.objects.all().order_by("-date")}
    return render(request, 'album/album.html',data)
def dangky(request):
    form =DangKy()
    if request.method == 'POST':
        form = DangKy(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
     # chay het ham kiem tra hop le
    return render(request,'dangky/dangky.html',{'form':form})

def model_form_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UploadForm()
    return render(request, 'upload/upload.html', {
        'form': form
    })

