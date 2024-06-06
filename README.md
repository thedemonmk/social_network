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
    1. **Using default django serving utility**
        ```bash
        python manage.py runserver
        ```
        **OR**

    2. **Using docker**
        ```bash
        docker-compose up --build
        ```

7. **Access the API**

    Open your web browser and navigate to `http://127.0.0.1:8000/`.

## API Endpoints

- `POST /api/v1/signup/` - User signup
- `POST /api/v1/login/` - User login
- `GET /api/v1/users/` - Search users by email or name (authenticated)
- `POST /api/v1/friend-request/<user_id>/` - Send friend request (authenticated)
- `PUT /api/v1/friend-request/<request_id>/action/` - Accept or reject friend request (authenticated)
- `GET /api/v1/friends/` - List friends (authenticated)
- `GET /api/v1/friend-requests/` - List pending friend requests (authenticated)

## Notes

- The friend request rate limit is set to 3 requests per minute.
- You need to add sufficient data in database for pagination testing

## License

This project is licensed under the MIT License.
