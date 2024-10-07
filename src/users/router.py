from fastapi import APIRouter

router = APIRouter(prefix='/users', tags=['Users'])


@router.get('/')
async def get_test_user_data():
    return {'name': 'test', 'surname': 'testovich'}
