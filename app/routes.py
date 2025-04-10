from flask import Blueprint, request, jsonify
from .models import Transaction
from .database import SessionLocal
from datetime import datetime, timedelta
import calendar

bp = Blueprint('routes', __name__)


@bp.route("/transactions", methods=["GET"])
def get_transactions():
    db = SessionLocal()
    query = db.query(Transaction)
    category = request.args.get("category")
    if category:
        query = query.filter(Transaction.category == category)
    
    month = request.args.get("month")
    if month :

        try:
            start_date = datetime.strptime(month,"%Y-%m")
            last_day = calendar.monthrange(start_date.year,start_date.month)[1]
            end_date = start_date.replace(day=last_day)

            query = query.filter(Transaction.date >= start_date,Transaction.date <= end_date)
        except ValueError:
            return jsonify({"error": "Invalid Date Format, YYYY-MM"}),400
    transactions = query.all()
    db.close()
    return jsonify([
        {
            "id": t.id,     
            "description": t.description,
            "amount": t.amount,
            'category': t.category,
            "date": t.date.strftime("%Y-%m-%d")
        } for t in transactions
    ])


@bp.route("/transactions", methods=["POST"])
def add_transactions():

    data = request.get_json()
    db = SessionLocal()
    new_t = Transaction(
        description=data["description"],
        amount=data["amount"],
        category=data["category"],
        date=datetime.strptime(data["date"], "%Y-%m-%d")

    )
    db.add(new_t)
    db.commit()
    db.refresh(new_t)
    db.close()

    return jsonify({
        "id": new_t.id,
        "description": new_t.description,
        "amount": new_t.amount,
        "category": new_t.category,
        "date": new_t.date.strftime("%Y-%m-%d")
    })


@bp.route("/summary", methods=["GET"])
def get_summary():

    db = SessionLocal()

    income = db.query(Transaction).filter(Transaction.amount > 0).all()
    expense = db.query(Transaction).filter(Transaction.amount < 0).all()

    total_income = sum(t.amount for t in income)
    total_expense = sum(t.amount for t in expense)
    balance = total_income + total_expense

    db.close()

    return jsonify(
        {
            "total_income": round(total_income, 2),
            "total_expense": round(total_expense, 2),
            "balance": round(balance, 2)
        }
    )

# @bp.route
