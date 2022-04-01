from src.users.entities.user import User
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session, current_app
from datetime import datetime, timedelta
import uuid, jwt

class ManageUsersUsecase:

    def __init__(self, users_repository):
        self.users_repository = users_repository

    def get_users(self):

        return self.users_repository.get_users()


    def create_user(self, data):

        user = self.users_repository.get_user_by_email(data["email"])
        #check if email already exists
        if user:
            raise ValueError(f"Email already exists.")

        #encrypt the given password
        data["password"] = generate_password_hash(data["password"])
        data["public_id"] = str(uuid.uuid4())

        user = User.from_dict(data)
        user = self.users_repository.create_user(user)

        return user

    def get_user(self, user_id):

        return self.users_repository.get_user(user_id)

    def update_user(self, user_id, data):

        user = self.get_user(user_id)

        if user:
            
            #check if password came as data to update then encrypt the new password
            if "password" in data:
                data["password"] = generate_password_hash(data["password"])

            user = self.users_repository.update_user(user_id, data)

            return user

        else:
            raise ValueError(f"User of ID {user_id} doesn't exist.")

    def login(self, data):
        email = data["email"]
        user = self.users_repository.get_user_by_email(email)
        
        #check than the email exists or the password is incorrect
        if not user or not check_password_hash(user.password, data["password"]):
            raise ValueError(f"Email or / and  password is incorrect.")
            
        session.clear()

        token = jwt.encode({
            'public_id': user.public_id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, current_app.secret_key)

        print("User", user.id)

        
        session["user_id"] = user.id
        session["token"] = token.decode('utf8')

        
        return {"token":token.decode("utf8")}

    def delete_user(self, user_id):

        user = self.get_user(user_id)

        if user:
            
            user = self.users_repository.hard_delete_user(user_id)

        else:
            raise ValueError(f"User of ID {user_id} doesn't exist or is already deleted.")
