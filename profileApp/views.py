from django.http import HttpResponse

def profile_view(request, username):
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Profile Page</title>
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #e6f7ff; /* Light blue background */
                font-family: Arial, sans-serif;
            }}
            h1 {{
                color: #4caf50 !important; /* Green color with !important to override any other styles */
                font-size: 3rem;
                text-align: center;
            }}
            .profile-container {{
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                text-align: center;
                width: 50%;
            }}
            .profile-container h1 {{
                color: #333;
                font-size: 2.5rem;
            }}
            .profile-container p {{
                color: #777;
                font-size: 1.2rem;
            }}
        </style>
    </head>
    <body>
        <div class="profile-container">
            <h1>Profile Page</h1>
            <p>Welcome to the profile of <strong>{username}</strong></p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)
