import pytest
from unittest.mock import Mock
from src.user_service import UserService

class TestUserService:
    def setup_method(self):
        self.mock_db = Mock()
        self.service = UserService(self.mock_db)
    
    # Existing tests (60% coverage baseline)
    def test_get_user_valid_id(self):
        self.mock_db.find_user.return_value = {"id": "123", "name": "John"}
        result = self.service.get_user("123")
        assert result == {"id": "123", "name": "John"}
    
    def test_get_user_empty_id(self):
        result = self.service.get_user("")
        assert result is None
    
    def test_create_user(self):
        self.mock_db.save_user.return_value = {"id": "456"}
        result = self.service.create_user("test@example.com", "Jane")
        assert result == {"id": "456"}
    
    # NOTE: validate_and_process_user is UNTESTED - this is our gap
# AI-GENERATED TESTS
def test_validate_user_data_required(self):
    with pytest.raises(ValueError, match="User data is required"):
        self.service.validate_and_process_user(None)

def test_validate_email_required(self):
    user_data = {"email": "invalid"}
    with pytest.raises(ValueError, match="Valid email is required"):
        self.service.validate_and_process_user(user_data)

def test_admin_override_success(self):
    user_data = {"email": "admin@test.com", "role": "admin"}
    result = self.service.validate_and_process_user(user_data, admin_override=True)
    assert result["status"] == "admin_created"

def test_admin_invalid_role(self):
    user_data = {"email": "test@test.com", "role": "user"}
    with pytest.raises(PermissionError, match="Invalid admin role"):
        self.service.validate_and_process_user(user_data, admin_override=True)

def test_user_already_exists(self):
    self.mock_db.user_exists.return_value = True
    user_data = {"email": "test@test.com", "name": "Test User"}
    with pytest.raises(ValueError, match="User already exists"):
        self.service.validate_and_process_user(user_data)