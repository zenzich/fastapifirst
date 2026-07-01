from fastapi import APIRouter

router = APIRouter(prefix="/books", tags=["Books"])

books = [None]

@router.get('/')
def get_all():
    return {
        "data": books,
    }