from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import SubscribeForm

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            send_mail(
                'Welcome to Our Newsletter',
                'Thank you for subscribing to our newsletter!',
                'your@example.com',  # Replace with your email
                [subscriber.email],
                fail_silently=False,
            )
            return redirect('success')
    else:
        form = SubscribeForm()
    return render(request, 'index.html', {'form': form})

def success(request):
    return render(request, 'success.html')