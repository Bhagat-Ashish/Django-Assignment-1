from django.http import HttpResponse

def product_view(request, category, product_id):
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Product Page</title>
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f4f4f9; /* Light grey background */
                font-family: Arial, sans-serif;
            }}
            .product-container {{
                background-color: #fff;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                width: 60%;
                text-align: center;
            }}
            h1 {{
                color: #4caf50; /* Green color for title */
                font-size: 2.5rem;
                margin-bottom: 20px;
            }}
            .product-details {{
                color: #333;
                font-size: 1.2rem;
                margin-top: 10px;
                font-weight: 500;
            }}
            .product-details span {{
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="product-container">
            <h1>Product Details</h1>
            <div class="product-details">
                <p><strong>Category:</strong> <span>{category}</span></p>
                <p><strong>Product ID:</strong> <span>{product_id}</span></p>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)
