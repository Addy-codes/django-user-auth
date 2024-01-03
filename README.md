# Django User Authentication System

This project is a Django-based web application implementing a user authentication system. It provides basic functionalities for user registration, login, logout, and profile management.

## Features

- **User Registration**: Allows new users to create an account by providing a username, email, password, and confirming the password.
- **User Login**: Users can log in using either their username or email along with their password.
- **Dashboard**: After a successful login, users are redirected to a simple dashboard displaying a welcome message with their username.
- **User Profile**: A basic profile page displaying user information. This page is accessible only to logged-in users.
- **Logout Functionality**: Users can log out of the application, which redirects them back to the login page.
- **Built-in Authentication**: Uses Django's built-in authentication system for handling user registration, login, and logout processes.
- 

## Snapshots

Below are some snapshots of the application in action:

### Login Page

![image](https://github.com/Addy-codes/django-user-auth/assets/72205091/11357d04-8273-42fe-8f4d-0c0010117fdf)



### Sign Up / Register Page
![image](https://github.com/Addy-codes/django-user-auth/assets/72205091/8668b4ec-23f2-4845-a344-212d3bbeb203)


### Home Page

![image](https://github.com/Addy-codes/django-user-auth/assets/72205091/bd584212-2ba9-4c03-bf6a-102538dfd821)


### Profile Page

![image](https://github.com/Addy-codes/django-user-auth/assets/72205091/c2a5dc82-2790-4803-9bbd-b8cc6f967136)



## Installation and Setup

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Setting up the project

1. **Clone the Repository** (if you haven't already)

    ```bash
    git clone https://github.com/Addy-codes/django-user-auth.git
    cd user-auth
    ```

2. **Set up a Python Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Database Migrations**

    Before running the application, you need to create the necessary database tables:

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser**

    To access the admin panel, create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**

    Start the Django development server:

    ```bash
    python manage.py runserver
    ```

7. **Access the Application**

    Open your web browser and go to [http://localhost:8000/](http://localhost:8000/) to view the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
