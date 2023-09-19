from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortenedURL
import random
import string

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_code = generate_short_code()
        shortened_url = ShortenedURL(original_url=original_url, short_code=short_code)
        shortened_url.save()
        return render(request, 'shortener/shortened.html', {'shortened_url': shortened_url})
    return render(request, 'shortener/index.html')

def expand_url(short_code):
    shortened_url = get_object_or_404(ShortenedURL, short_code=short_code)
    return redirect(shortened_url.original_url)

def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(30))
    return short_code
#It takes a request object and a short_code parameter from the URL.

#It uses the get_object_or_404 function to retrieve a ShortenedURL object with the specified short_code. If the object is not found (i.e., the short code doesn't exist in the database), it raises a 404 error.

#If a valid ShortenedURL object is found, the view redirects the user to the original URL associated with that object using redirect(shortened_url.original_url).

#This view is essential for expanding shortened URLs and redirecting users to the original destination when they access the shortened link.