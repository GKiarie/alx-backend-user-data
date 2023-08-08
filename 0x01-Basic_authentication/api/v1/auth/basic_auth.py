#!/usr/bin/env python3
""" Module to manage API authentication
Basic Auth
"""
from api.v1.auth.auth import Auth


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
