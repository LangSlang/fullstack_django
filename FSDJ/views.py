from django.http import HttpResponse
from selenium import webdriver

def Home(request):
    browser= webdriver.Chrome()
    browser.get("https://www.yahoo.com/")
    # while (True):
    #     pass
    html = "<html><body>Hello</body></html>"
    return HttpResponse("hi")
