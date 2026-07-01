from fastapi import APIRouter
from models import Book

router = APIRouter(prefix="/books", tags=["Books"])

books = []

@router.get('/')
def get_all():
    return {
        "data": books,
    }

@router.post('/')
def post_book(book: Book):
    new_book = {
        "user": '',
        "title": book.title,
        "text": book.text,
    }

    books.append(new_book)

    return {
        "data": new_book
    }