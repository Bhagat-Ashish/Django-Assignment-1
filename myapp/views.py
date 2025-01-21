from django.shortcuts import render
from django.http import HttpResponse

def index(request):
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
                flex-direction: column;
                height: 100vh;
                margin: 0;
                background-color: #f0f8ff; /* Light blue background */
                font-family: Arial, sans-serif;
            }
            h1 {
                color: #4caf50; /* Green color */
                font-size: 3rem; /* Increased font size */
                margin-bottom: 30px;
            }
            .links {
                margin-bottom: 30px;
            }
            .links a {
                margin: 0 15px;
                text-decoration: none;
                color: #007bff;
                font-size: 1.5rem;
                font-weight: 500;
            }
            .links a:hover {
                text-decoration: underline;
                color: #0056b3;
            }
            form {
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-top: 20px;
                width: 100%;
                max-width: 400px;
            }
            label {
                margin-bottom: 10px;
                font-size: 1.3rem;
                color: #333;
            }
            input {
                padding: 12px;
                width: 100%;
                font-size: 1rem;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 8px;
                box-sizing: border-box;
                outline: none;
            }
            input:focus {
                border-color: #4caf50;
            }
            button {
                padding: 12px 25px;
                font-size: 1.2rem;
                background-color: #4caf50;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the Index Page</h1>
        
        <div class="links">
            <a href="/home/">Home</a>
            <a href="/contact/">Contact</a>
        </div>
        
        <form id="profileForm">
            <label for="username">Enter Username:</label>
            <input type="text" id="username" name="username" placeholder="Enter your username">
            <button type="button" onclick="navigateToProfile()">Go to Profile</button>
        </form>
        
        <form id="productForm">
            <label for="category">Enter Category:</label>
            <input type="text" id="category" name="category" placeholder="Enter product category">
            <label for="product_id">Enter Product ID:</label>
            <input type="number" id="product_id" name="product_id" placeholder="Enter product ID">
            <button type="button" onclick="navigateToProduct()">Search Product</button>
        </form>

        <script>
            // Function to navigate to profile page with the entered username
            function navigateToProfile() {
                const username = document.getElementById('username').value;
                if (username) {
                    window.location.href = `/profile/${username}/`;
                } else {
                    alert('Please enter a username.');
                }
            }

            // Function to navigate to product page with the entered category and product ID
            function navigateToProduct() {
                const category = document.getElementById('category').value;
                const productId = document.getElementById('product_id').value;
                if (category && productId) {
                    window.location.href = `/products/${category}/${productId}/`;
                } else {
                    alert('Please enter both category and product ID.');
                }
            }
        </script>
    </body>
    </html>
    """
    return HttpResponse(html)
