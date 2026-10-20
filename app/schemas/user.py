from pydantic import BaseModel, Field, ConfigDict

class UserCreate(BaseModel):
    phone_number: str = Field(pattern="^\+993\d{8}$", description="Phone number in the format +993XXXXXXXX", examples=["+99361123456"])
    password: str = Field(min_length=6, max_length=72)
    full_name: str = Field(min_length=2, max_length=100)

class UserLogin(BaseModel):
    phone_number: str = Field(pattern="^\+993\d{8}$", description="Phone number in the format +993XXXXXXXX", examples=["+99361123456"])
    password: str

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    phone_number: str
    full_name: str
    is_admin: bool