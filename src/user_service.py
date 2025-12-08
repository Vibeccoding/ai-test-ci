# Baseline service with existing functionality
class UserService:
    def __init__(self, db_client):
        self.db = db_client
    
    def get_user(self, user_id):
        """Existing function with tests"""
        if not user_id:
            return None
        return self.db.find_user(user_id)
    
    def create_user(self, email, name):
        """Existing function with tests"""
        user = {"email": email, "name": name}
        return self.db.save_user(user)
    
    # NEW UNTESTED FUNCTION - This is our change set
    def validate_and_process_user(self, user_data, admin_override=False):
        """New function with branches - UNTESTED"""
        # Branch 1: Input validation
        if not user_data:
            raise ValueError("User data is required")
        
        # Branch 2: Email validation
        if not user_data.get("email") or "@" not in user_data["email"]:
            raise ValueError("Valid email is required")
        
        # Branch 3: Admin override path
        if admin_override:
            return self._process_admin_user(user_data)
        
        # Branch 4: Regular user processing
        if len(user_data.get("name", "")) < 2:
            raise ValueError("Name must be at least 2 characters")
        
        return self._process_regular_user(user_data)
    
    def _process_admin_user(self, user_data):
        # Error path 1: Admin processing can fail
        if user_data.get("role") != "admin":
            raise PermissionError("Invalid admin role")
        return {"id": "admin_123", "status": "admin_created"}
    
    def _process_regular_user(self, user_data):
        # Error path 2: Regular processing can fail
        if self.db.user_exists(user_data["email"]):
            raise ValueError("User already exists")
        return {"id": "user_456", "status": "created"}