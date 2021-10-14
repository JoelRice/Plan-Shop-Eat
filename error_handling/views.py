from django.shortcuts import render


def error_404(request, exception):
    data = {}
    return render(request, 'error_404.html', data)


def error_500(request):
    data = {}
    return render(request, 'error_500.html', data)


"""
reference : 
https://www.youtube.com/watch?v=NgHvfxkEKhQ
https://pythoncircle.com/post/40/designing-custom-404-and-500-error-pages-in-django/
https://pythoncircle.com/post/564/displaying-custom-404-error-page-not-found-page-in-django-20/
"""
