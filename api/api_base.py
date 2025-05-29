"""Base API client for FarmChat.

This module provides the base class for API clients with common functionality
for making HTTP requests and handling responses.
"""

import requests
from abc import ABC, abstractmethod

class BaseAPIClient(ABC):
    """Base class for API clients."""
    
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })
    
    @abstractmethod
    def get_data(self, parcel_id: str) -> dict:
        """Get data for a specific parcel.
        
        Args:
            parcel_id: The parcel identifier
            
        Returns:
            dict: The API response data
        """
        pass
    
    def _make_request(self, endpoint: str, params: dict = None) -> dict:
        """Make an HTTP request to the API.
        
        Args:
            endpoint: The API endpoint
            params: Query parameters
            
        Returns:
            dict: The API response
        """
        # TODO: Implement request handling with error management
        pass 