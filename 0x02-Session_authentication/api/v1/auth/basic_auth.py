#!/usr/bin/env python3
""" Module to manage API authentication
Basic Auth
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic Auth Class"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header for a
        Basic Authentication"""
        if authorization_header is None or not isinstance(
             authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        # Extract the Base64 part after 'Basic '
        base64_part = authorization_header[len('Basic '):]

        return base64_part

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """method returns decoded value of Base64 string"""
        if base64_authorization_header is None or not isinstance(
             base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_value = decoded_bytes.decode('utf-8')
            return decoded_value
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """returns the user email and password from the
        Base64 decoded value."""
        if decoded_base64_authorization_header is None or not isinstance(
             decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Use the class method to search for users based on email
        user = User.search({'email': user_email})

        if not user:
            return None

        user = user[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads Auth and retrieves the
        User instance for a request"""
        if request is None:
            return None

        authorization_header = self.authorization_header(request)
        base64_header = self.extract_base64_authorization_header(
             authorization_header)
        decoded_header = self.decode_base64_authorization_header(base64_header)
        user_email, user_pwd = self.extract_user_credentials(decoded_header)
        user = self.user_object_from_credentials(user_email, user_pwd)

        return user
