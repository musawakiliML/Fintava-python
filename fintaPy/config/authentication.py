import os

# Create Authentication Configuration Class
class AuthConfig:
    """Handles API authentication configuration."""
    def __init__(self):
        self.api_key = os.getenv("FINTAVA_API_KEY", "")
    
    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "accept": "application/json",
            "content-type": "application/json"
        }
