from fastapi import APIRouter


router = APIRouter(
    prefix='/health'
)


@router.get('/get')
async def health():
    return {'response': 'healthy'}
