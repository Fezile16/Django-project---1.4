from django.http import HttpResponse

def hello_world(request):
    html = """
    <html>
    <head>
        <title>Hello,t World!</title>
    </head>
    <body>
        <h1 style="color: blue;">Hello,r World!</h1>
        <p>Welcome to Django!</p>
    </body>
    </html>
    """
    return HttpResponse(html)