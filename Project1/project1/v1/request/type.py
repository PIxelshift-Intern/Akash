from pydantic import BaseModel, EmailStr

class Login(BaseModel):
    """
    This class is used to validate the login request
    """
    username: str
    # optionally email 
    # email: str
    password: str
    def __str__(self):
        return self.username
    
class Register(BaseModel):
    """
    This class is used to validate the register request
    """
    username: str
    password: str
    email: EmailStr
    def __str__(self):
        return self.username
    
class User(BaseModel):
    """
    This class is used to validate the user object
    """
    username: str
    email: EmailStr
    created_at: str
    updated_at: str
    Verified: bool
    total_files: int
    def __str__(self):
        return self.username
    
class File_request(BaseModel):
    """
    This class is used to validate the file object
    """
    id: str
    name: str
    def __str__(self):
        return self.id

class Email_Verification(BaseModel):
    """
    This class is used to validate the email verification object
    """
    email: EmailStr
    def __str__(self):
        return self.email
    
class Create_File(BaseModel):
    """
    This class is used to validate the create file request
    """
    user_id: int
    file_name: str
    def __str__(self):
        return self.file_path