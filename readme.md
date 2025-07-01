# EasyAds

EasyAds is a full-stack Django web application for posting and browsing classified advertisements. It supports user roles like buyers and sellers, ad wishlists, contact forms, and a secure login system. Built with scalability and clarity in mind, it follows Django best practices for organization and extensibility.

---

## Features
- Role based login system(customer, seller, admin)
- Post and manage ads (sellers)
- Browse classified ads (public)
- Add/remove ads to wishlist (users)
- Contact form with validation
- User authentication (signup/login/logout)
- Role-based access control for sellers
- Dynamic ad details page
- Static pages like About and Contact

---

## Tech Stack

- Backend: Django 5.2.3
- Frontend: HTML5, Bootstrap
- Database: MySQL
- Templating: Django Templates
- Authentication: Django's built-in auth system

---

## Installation
Fork it and get the link from github
### 1. Clone the repository

```bash
git clone https://github.com/<your-user-name>/easyads.git
cd easyads
```
### 2. Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate   # For Linux/macOS
# .venv\Scripts\activate    # For Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run migrations
```bash
python3 manage.py migrate   # For Linux/macOS
# python manage.py migrate  # For Windows
```
### 5. Start the development server
```bash
python3 manage.py runserver     # For Linux/macOS
# python manage.py runserver    # For Windows
```

Visit below link in your browser.
```bash
http://localhost:8000
```

---

## Default User Roles

You can create users using the Django admin:
```bash
python manage.py createsuperuser
```
Then login at: 
```bash
http://localhost:8000/admin
```

---

## Contact Form Example

The contact form is functional and includes backend validation. You can access it via a button or /contact/ route.


---

## Future Improvements

- Add image upload for ads
- Add pagination to listing pages
- Integrate real user messaging
- Improve SEO and accessibility
- Add testing and CI/CD setup

---

## License

This project is licensed under the MIT License.


---

## Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to change.


---

## Author

Sai Krishna Kotha