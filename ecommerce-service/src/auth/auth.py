from functools import wraps

from flask import g, current_app, request, session

import jwt

from src.frameworks.db.sqlalchemy import SQLAlchemyClient

from src.sellers.entities.seller import Seller

def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return {"message": "Need to be logged to do this action"}
        
        return view(**kwargs)
        
    return wrapped_view


def load_logged(user):

        if user is None:
            g.user = None
        else: 
            g.user = user


def token_required(f):
    @wraps(f)
    def decorated(**kwargs):
        token = None
        print("request", request.headers)
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            
        if not token:
            return { "message": "Token is missing !!"}
        try:
            data = jwt.decode(token, current_app.secret_key)
            
        except:
            return { "message": "Token is invalid !!"}
        # returns the current logged in users contex to the routes
        return  f(**kwargs)

    return decorated


def admin_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user.role == "Seller User" and g.user.role != "Marketplace User" and (view.__name__ == "get_seller" or view.__name__ == "update_seller"):
            return view(**kwargs)
        if g.user.role == "Marketplace Administrator":
            return view(**kwargs)
        return {"message": "Only Marketplace Administartor can do this action"}
        
    return wrapped_view


def only_seller(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        sqlalchemy_client = SQLAlchemyClient()

        with sqlalchemy_client.session_factory() as session_db:
            is_seller = session_db.query(Seller).filter_by(user_seller_id=session.get('user_id')).first()
            
        if g.user.role == "Seller User" and is_seller:
            return view(**kwargs)
        return {"message": "Only Seller User can do this action"}
        
    return wrapped_view