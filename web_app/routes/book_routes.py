

from flask import Blueprint, jsonify, render_template, request, redirect
#From web_app.models import db, Book, parse_records
book_routes = Blueprint('book_routes',__name__)

@book_routes.route("/books,json")
def list_books():
    print('Visted the books page')
    books = [
        {"id":1, "title": "Book 1"},
        {"id":2, "title": "Book 2"},
        {"id":3, "title": "Book 3"},
    ]
    return render_template("book.html", books =books)

@book_routes.route("books/new")
def new_book():
    return render_template("new_book.html")

