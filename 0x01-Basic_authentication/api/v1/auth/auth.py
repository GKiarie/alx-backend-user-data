#!/usr/bin/env python3
""" Module to manage API authentication
"""
from typing import List, TypeVar


class Auth:
    """Class to manage API auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns false-path"""
        return False

    def authorization_header(self, request=None) -> str:
        """Returns None - request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None - request"""
        return None
