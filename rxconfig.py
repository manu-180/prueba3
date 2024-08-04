import reflex as rx

config = rx.Config(
    app_name="prueba3",
    api_url="https://api.baackend.com/",
    cors_allowed_origins = [
        "http://localhost:3000/",
        "https://baackend.com/"
    ]
)