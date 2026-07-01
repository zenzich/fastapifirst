from fastapi import APIRouter
from models import Book

router = APIRouter(prefix="/books", tags=["Books"])

books = [None]

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

    return {
        "data": new_book
    }