from django.http import HttpResponse
from django.shortcuts import render # import render function to render html templates
# from urls to here.
def process_services(request):
    context = {
        'title': 'Services',
        'heading': 'Our Services',
        'description': 'We offer a range of services to meet your needs.',
        'image': 'img/services.jpg',
        'page_title': 'Services | CST Web Solutions',
        'page_description': 'We offer a range of services to meet your needs.',
        'page_keywords': 'web development, web design, web hosting, e-commerce, mobile app development, web maintenance, SEO, content writing, social media marketing, branding, web analytics, web security, web programming, web design, web development, web hosting, e-commerce, mobile app development, web maintenance, SEO, content writing, social media marketing, branding, web analytics, web security, web programming',
    }
    # return HttpResponse("This is the process_services view.")
    return render(request, 'services.html',context)