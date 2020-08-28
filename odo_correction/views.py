from django.shortcuts import render

def base_site(request):
    return render(request, 'odo_correction/base.html', {})

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request, 'odo_correction/upload.html')
