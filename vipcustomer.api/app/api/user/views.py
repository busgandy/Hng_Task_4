from fastapi import APIRouter, Depends, HTTPException, status
import jwt
from db.db import db_session
from api.user.schemas import UserSchema, APIKey, Signup, Login
from sqlalchemy.ext.asyncio import AsyncSession
from db.models.user import User
from api.user.authentication import token_generator, config_credentials, authorized_exception
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from api.user.services import UserService

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@router.post('/signup')
async def create_user(user:Signup):
    user_service = UserService()
    new_user = user_service.create_user(user)
    new_user = User(**user.dict())
    return new_user

@router.post('/login')
async def login(form_data: Login):
    user_service = UserService()
    res = await user_service.token_generator(form_data.email, form_data.password)
    user, token = res['user'], res['access_token']
    try:
        payload = jwt.decode(token, config_credentials['SECRET_KEY'], config_credentials['ALGORITHM'])
    except:
        raise authorized_exception
    return  {
                'user': {
                    'id' : user.id,
                    'email' : user.email,
                    'first_name' : user.first_name,
                    'last_name' : user.last_name
                },
                'access_token' : token,'token_type' : 'bearer'
            }


# async def get_current_user(token : str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, config_credentials['SECRET_KEY'], config_credentials['ALGORITHM'])
#         user = await User.get(id=payload.get('id'))
#     except:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail = 'Invalid Username or Password',
#             headers={"WWW-Authenticate":'Bearer'}
#         )
#     return await user

# @router.post('/login')
# async def login(user: UserSchema = Depends(get_current_user)):
#     return {
#         'status' : 'ok',
#         'data' : {
#             'email' : user.email, 'first_name' :user.first_name, 'last_name' : user.last_name,
#             'is_verified' : user.is_verified
#         }
#     }


# @router.get("/my_details/")
# def get_current_user(current_user: User):
#     return current_user


# @router.get("/key")

# async def get_user_api_key():
#     # Check Database if User id exist
#     # Depends on session user id

#     # If user exist get user APIkey
#     userAPIKey = APIKey(
#         key="3fa85f64-5740-2262-b3fc-2c963f36afa1",
#         user="3fa85f64-5740-2262-b3fc-2c963f36afa1",
#     )

#     # Send key string
#     return userAPIKey
