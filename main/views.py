from django.shortcuts import render
import pyshorteners
from django.contrib import messages


def url_shortener(request):
    try:
        short_url = ""
        url = ""
        if request.method == "POST":
            shortener = pyshorteners.Shortener()
            url = request.POST.get("url")
            short_url = shortener.tinyurl.short(url)
            messages.success(request, "Generated")
        return render(
            request, "url-shortener.html", {"short_url": short_url, "url": url}
        )
    except:
        return render(request, "url-shortener.html")
