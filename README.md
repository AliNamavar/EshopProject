# EshopProject

## Short Description
EshopProject is an online store developed using Django. This platform allows managing products, orders, and users.

**Note:** The site is not fully completed yet, but all mentioned features have been implemented and are functioning correctly.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contribution](#contribution)
- [License](#license)
- [Contact](#contact)

## Features
- **Product Management:** Add, edit, and delete products with categories and images
- **Nested Categories:** Multi-level product categorization for better organization
- **Order Management:** View and manage user orders with shipping and payment status
- **Shopping Cart:** Add products to the cart and process orders
- **Price Filtering:** Filter products based on price range
- **User Panel:** Dedicated dashboard for users to manage orders, addresses, and personal information
- **Contact Page:** Users can send messages, and admins can manage received messages
- **Article Management:** Publish articles and news related to the store
- **Admin Panel:** A dedicated environment for admins to manage various sections of the store
- **Payment Gateway:** Support for online payments for seamless transactions
- **Responsive Design:** Fully responsive design for optimal viewing on different devices
- **Site Settings Management:** Ability to change general site settings via the admin panel
- **User Authentication:** Features include login, logout, password recovery, and email activation

## Prerequisites
Ensure the following dependencies are installed on your system:
- Python 3.x
- Django
- pip
- Virtualenv (optional but recommended)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AliNamavar/EshopProject.git
   cd EshopProject
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open your browser and go to `http://localhost:8000`.

## Usage
- **Product Management:** Add, edit, and delete products
- **Order Management:** View and handle user orders
- **Shopping Cart:** Users can add products to the cart and proceed with payment
- **Contact Page:** Users can reach out to the admin via a contact form
- **User Panel:** Manage personal information, orders, and addresses

## Project Structure
```
EshopProject/
├── account_module/
├── article_module/
├── contact_module/
├── eshop_project/
├── home_module/
├── order_module/
├── product_module/
├── site_module/
├── static/
├── templates/
├── uploads/
├── user_panel_module/
├── utils/
├── manage.py
└── requirements.txt
```

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Contact
For questions and suggestions, you can reach out via email at [alinamavar315@gmail.com].

