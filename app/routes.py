from flask import Blueprint, request, jsonify
from .models import Transaction
from .database import SessionLocal
from datetime import datetime

bp = Blueprint('routes', __name__)


@bp.route("/transactions", methods=["GET"])
def get_transactions():
    db = SessionLocal()
    transactions = db.query(Transaction).all()
    db.close()
    return jsonify([
        {
            "id": t.id,
            "description":t.description,
            "amount": t.amount,
            'category': t.category,
            "date": t.date.strftime("%Y-%m-%d")
        } for t in transactions
    ])

@bp.route("/transactions",methods=["POST"])
def add_transactions():
    
    data = request.get_json()
    db = SessionLocal()
    new_t = Transaction(
        description = data["description"],
        amount = data["amount"],
        category = data["category"],
        date = datetime.strptime(data["date"],"%Y-%m-%d")

    )
    db.add(new_t)
    db.commit()
    db.refresh(new_t)
    db.close()
    
    return jsonify({
        "id":new_t.id,
        "description":new_t.description,
        "amount": new_t.amount,
        "category": new_t.category,
        "date": new_t.date.strftime("%Y-%m-%d")
    })
