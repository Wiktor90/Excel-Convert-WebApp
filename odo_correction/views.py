from django.shortcuts import render

def excel_upload(request):
    return render(request, 'odo_correction/base.html', {})
