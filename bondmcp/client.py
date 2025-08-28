"""BondMCP API Client"""
import requests
import os
from typing import Dict, Any, Optional
from .exceptions import BondMCPError, AuthenticationError, APIError

class BondMCPClient:
    def __init__(self, api_key: Optional[str] = None, base_url: str = "https://api.bondmcp.com"):
        self.api_key = api_key or os.getenv("BONDMCP_API_KEY")
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        
        if self.api_key:
            self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})
    
    def health(self) -> Dict[str, Any]:
        """Check API health status"""
        response = self.session.get(f"{self.base_url}/health")
        return self._handle_response(response)
    
    def ask(self, question: str) -> Dict[str, Any]:
        """Ask a health-related question"""
        data = {"question": question}
        response = self.session.post(f"{self.base_url}/health/ask", json=data)
        return self._handle_response(response)
    
    def register(self, email: str, password: str, name: str) -> Dict[str, Any]:
        """Register a new user"""
        params = {"email": email, "password": password, "name": name}
        response = self.session.post(f"{self.base_url}/auth/register", params=params)
        return self._handle_response(response)
    
    def login(self, email: str, password: str) -> Dict[str, Any]:
        """Login user"""
        data = {"email": email, "password": password}
        response = self.session.post(f"{self.base_url}/auth/login", json=data)
        return self._handle_response(response)
    
    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """Handle API response"""
        if response.status_code == 401:
            raise AuthenticationError("Invalid API key or authentication failed")
        elif response.status_code >= 400:
            try:
                error_data = response.json()
                raise APIError(f"API Error: {error_data.get('detail', 'Unknown error')}")
            except ValueError:
                raise APIError(f"HTTP {response.status_code}: {response.text}")
        
        try:
            return response.json()
        except ValueError:
            return {"status": "success", "data": response.text}
