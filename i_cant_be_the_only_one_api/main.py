from db import SessionLocal
from functions import add_user

session = SessionLocal()

try:
    user = add_user(
        db=session,
        username="jacob",
        email="jacob@email.com",
        password_hashed="jacob's conundrum"
    )

    print("User created:", user.Username)

except ValueError as e:
    print("Error:", e)

finally:
    session.close()