from fastapi import APIRouter
from schemas.book import BookCreate

router = APIRouter(prefix="/books", tags=["Books"])

books = []

@router.get('/')
def get_all():
    return {
        "data": books,
    }

@router.post('/')
def post_book(book: BookCreate):
    new_book = {
        "user": '',
        "title": book.title,
        "text": book.text,
    }

    books.append(new_book)

    return {
        "data": new_book
    }

