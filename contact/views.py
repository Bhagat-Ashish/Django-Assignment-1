from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Index Page</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f8ff; /* Light blue background */
            }
            h1 {
                color: #98D8EF; /* Green color */
                font-family: Arial, sans-serif;
                font-size: 4rem; /* Increased font size */
            }
        </style>
    </head>
    <body>
        <h1>Contact Page</h1>
    </body>
    </html>
    """

    return HttpResponse(html)
