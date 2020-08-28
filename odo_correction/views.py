from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .forms import ExcleForm
from .models import Excel


def base_site(request):
    return render(request, 'odo_correction/base.html')

def info(request):
    return render(request, 'odo_correction/info.html')

# def upload(request):
#     context ={}
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         fs = FileSystemStorage()
#         name = fs.save(uploaded_file.name, uploaded_file)
#         context['url'] = fs.url(name)
#     return render(request, 'odo_correction/upload.html', context)

def excle_list(request):
    files = Excel.objects.all()
    return render(request, 'odo_correction/excle_list.html', {'files':files})

def excle_upload(request):
    if request.method =='POST':
        form = ExcleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('excle_list')
    else:
        form = ExcleForm()

    return render(request, 'odo_correction/excle_upload.html', {'form':form})

def excle_delete(request, pk):
    if request.method == 'POST':
        file = Excel.objects.get(pk=pk)
        file.delete()
    return redirect('excle_list')
