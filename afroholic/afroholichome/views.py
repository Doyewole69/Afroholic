from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import SubscribeForm
from django.conf import settings
from .models import Subscriber, upcomingproject1,upcomingproject2,news,merch1,merch2


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            with open('newsletter.txt', 'r') as f:
                email_content = f.read()
                
            email_content = email_content.format(name=subscriber.first_name)

            send_mail(
                'Welcome to Afroholic Family!x',
                email_content,
                settings.EMAIL_HOST_USER,  # Sender's email
                [subscriber.email],
                fail_silently=False,
            )
            return redirect('success')
    else:
        form = SubscribeForm()
        
    project1_list = upcomingproject1.objects.all()
    project2_list = upcomingproject2.objects.all()
    shop1_list = merch1.objects.all()
    shop2_list = merch2.objects.all()
    news_list = news.objects.all()

    context = {
        'form': form,
        'project1_list': project1_list,
        'project2_list': project2_list,
        'shop1_list': shop1_list,
        'shop2_list': shop2_list,
        'news_list': news_list,
    }    
    return render(request, 'index.html', context)

def success(request):
    return render(request, 'success.html')

def artistes(request):
    return render(request, 'artistes.html')

def olusegun(request):
    return render(request, 'olusegun.html')

def vennessa(request):
    return render(request, 'vennessa.html')

def leo9ice(request):
    return render(request, 'leo9ice.html')

def lin(request):
    return render(request, 'lin.html')

def skeffi(request):
    return render(request, 'skeffi.html')

def iceboiy(request):
    return render(request, 'iceboiy.html')

def chuma(request):
    return render(request, 'chuma.html')

def department(request):
    return render(request, 'department.html')