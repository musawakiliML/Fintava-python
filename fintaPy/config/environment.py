# Base Urls for API

class Environment:
    """Handles environment configuration."""
    SANBOX_URL = "https://dev.fintavapay.com/api/dev"
    PRODUCTION_URL = "https://live.fintavapay.com/api/dev"
    
    def __init__(self, use_sandbox: bool = True):
        self.base_url = self.SANBOX_URL if use_sandbox else self.PRODUCTION_URL
        
    def get_base_url(self) -> str:
        return self.base_url