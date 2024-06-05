# Social Networking API

This project is a social networking API built with Django Rest Framework. It provides functionalities for user login/signup, searching users, sending/accepting/rejecting friend requests, listing friends, and listing pending friend requests.

## Installation

### Prerequisites

- Python 3.12+
- Virtualenv (optional but recommended)

### Steps

1. **Clone the repository**

    ```bash
    git clone https://github.com/thedemonmk/social_network.git
    cd social_network
    ```

2. **Create and activate a virtual environment**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the required packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**

    ```bash
    python manage.py runserver
    ```

7. **Access the API**

    Open your web browser and navigate to `http://127.0.0.1:8000/`.

## API Endpoints

- `POST /signup/` - User signup
- `POST /login/` - User login
- `GET /users/` - Search users by email or name (authenticated)
- `POST /friend-request/<user_id>/` - Send friend request (authenticated)
- `PUT /friend-request/<request_id>/action/` - Accept or reject friend request (authenticated)
- `GET /friends/` - List friends (authenticated)
- `GET /friend-requests/` - List pending friend requests (authenticated)

## Notes

- The friend request rate limit is set to 3 requests per minute.

## License

This project is licensed under the MIT License.
