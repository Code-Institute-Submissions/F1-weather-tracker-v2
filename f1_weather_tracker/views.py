from django.shortcuts import render

# Create your views here.


def error_400(request, exception, template_name='400.html'):
    return render(request, template_name)


def error_403(request, exception, template_name='403.html'):
    return render(request, template_name)


def error_404(request, exception, template_name='404.html'):
    return render(request, template_name)


def error_500(request, template_name='500.html'):
    return render(request, template_name)
