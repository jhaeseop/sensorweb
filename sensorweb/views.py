from django.http import JsonResponse
from django.shortcuts import render
from .models import sensors


# Create your views here.

def index(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    print(f'x_forwarded_for = {x_forwarded_for}')
    if x_forwarded_for:
        request_ip = x_forwarded_for.split(',')
        print(f'ip:HTTP_X_FORWARDED_FOR = {request_ip}')
    else:
        request_ip = request.META.get('REMOTE_ADDR')
        print(f'ip:REMOTE_ADDR = {request_ip}')
    return render(request, 'sensorweb/main.html')

def sensor(request):
    # AJAX 요청 처리 또는 템플릿 렌더링
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        data = sensors.objects.order_by('-time')[:60]
        return JsonResponse({'data': list(data.values())})
    else:
        return render(request, 'sensorweb/table_chart.html')  # 템플릿 렌더링



def pages_view(request, num_page):
    return render(request, f'samples/sample{num_page}.html')

def sub_view(request, n_page, n_sect):
    return render(request, f'sub/{n_page}_{n_sect}.html')

def file_upload(request):
    return render(request, 'fileupload/fileupload.html')

