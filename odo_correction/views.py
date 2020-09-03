from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ExcleForm
from .models import Excel



def base_site(request):
    return render(request, 'odo_correction/base.html')

def info(request):
    return render(request, 'odo_correction/info.html')

def excel_list(request):
    files = Excel.objects.all()
    return render(request, 'odo_correction/excel_list.html', {'files':files})

def excel_upload(request):
    if request.method =='POST':
        form = ExcleForm(request.POST, request.FILES)
        if form.is_valid():
            ex = request.FILES['file']
            if ex.name.lower().endswith(('.xlsx', '.xls', '.csv')):
                form.save()
                return redirect('excel_list')      
            else:
                messages.error(request, f'ERROR: Format of uploaded file: {ex.name} is NOT supported !')
    else:
        form = ExcleForm()
    return render(request, 'odo_correction/excel_upload.html', {'form':form})

def excel_correction(request, pk):
    ex = Excel.objects.get(pk=pk)
    ex.columns_check()
    if ex.file_content == True:
        df = ex.odo()
        ex.save_excel(df)
        ex.corrected = True
        ex.save()
        return redirect('excel_list')
    else:
        messages.error(request, f'ERROR: File: {ex.file.name} missing required column name(s) and was removed from DB.')
        ex.delete()
        return redirect('excel_list')

def excel_delete(request, pk):
    if request.method == 'POST':
        ex = Excel.objects.get(pk=pk)
        ex.delete()
    return redirect('excel_list')
