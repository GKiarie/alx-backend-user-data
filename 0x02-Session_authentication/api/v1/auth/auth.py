#!/usr/bin/env python3
""" Module to manage API authentication
"""
from typing import List, TypeVar


class Auth:
    """Class to manage API auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns false-path"""
        # Return True if path is None
        if path is None:
            return True

        if not path.endswith('/'):
            path = path + '/'

        # Return True if excluded_paths is None or empty
        if not excluded_paths:
            return True

        # Make sure all paths in excluded_paths end with a /
        excluded_paths = [p if p.endswith('/') else
                          p + '/' for p in excluded_paths]

        # Check if path is in excluded_paths
        for excluded_path in excluded_paths:
            if path.startswith(excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Returns None - request"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None - request"""
        return None
