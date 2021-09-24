from django.shortcuts import render

# Create your views here.


def entry_not_found(request, exception, template_name='404.html'):
    return render(request, template_name)


def permission_denied(request, exception, template_name='403.html'):
    return render(request, template_name)


def server_error(request, exception, template_name='500.html'):
    return render(request, template_name)


def bad_request(request, exception, template_name='400.html'):
    return render(request, template_name)
