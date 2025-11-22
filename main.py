from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = "rahasia-aku"

# =========================
#  DATABASE CONFIG
# =========================
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# =========================
#  DATABASE MODELS
# =========================

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relasi ke detail transaksi
    details = db.relationship("TransactionDetail", backref="product", lazy=True)


class MallCustomer(db.Model):
    __tablename__ = "mall_customer"

    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    annual_income = db.Column(db.Integer)
    spending_score = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relasi ke transaksi
    transactions = db.relationship("Transaction", backref="customer", lazy=True)


class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("mall_customer.id"), nullable=False)
    transaction_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_amount = db.Column(db.Integer, default=0)
    payment_method = db.Column(db.String(50))

    # relasi ke detail
    details = db.relationship("TransactionDetail", backref="transaction", lazy=True)


class TransactionDetail(db.Model):
    __tablename__ = "transaction_details"

    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.Integer, db.ForeignKey("transactions.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    unit_price = db.Column(db.Integer, nullable=False, default=0)
    subtotal = db.Column(db.Integer, nullable=False, default=0)


# bikin tabel kalau belum ada
with app.app_context():
    db.create_all()

# =========================
#        ROUTES
# =========================

# ---------- DASHBOARD ----------
@app.route("/")
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))

    total_users = User.query.count()
    total_products = Product.query.count()
    total_customers = MallCustomer.query.count()
    total_transactions = Transaction.query.count()

    # hitung penjualan hari ini
    today = date.today()
    sales_today = (
        db.session.query(db.func.coalesce(db.func.sum(Transaction.total_amount), 0))
        .filter(db.func.date(Transaction.transaction_date) == today)
        .scalar()
    )

    return render_template(
        "home.html",
        total_users=total_users,
        total_products=total_products,
        total_customers=total_customers,
        total_transactions=total_transactions,
        sales_today=sales_today,
    )

# supaya link /dashboard di navbar tetap jalan
@app.route("/dashboard")
def dashboard():
    return redirect(url_for("home"))

# ---------- REGISTER ----------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        exists = User.query.filter_by(email=email).first()
        if exists:
            return "Email sudah digunakan!"

        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("register.html")

# ---------- LOGIN ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email, password=password).first()
        if user:
            session["user_id"] = user.id
            return redirect(url_for("home"))
        return "Email atau password salah!"

    return render_template("login.html")

# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login"))

# ---------- PRODUCTS ----------
@app.route("/products")
def products():
    if "user_id" not in session:
        return redirect(url_for("login"))

    all_products = Product.query.all()
    return render_template("products.html", products=all_products)

@app.route("/products/add", methods=["POST"])
def products_add():
    if "user_id" not in session:
        return redirect(url_for("login"))

    name = request.form["name"]
    price = int(request.form["price"])
    stock = int(request.form.get("stock", 0))

    new_product = Product(name=name, price=price, stock=stock)
    db.session.add(new_product)
    db.session.commit()

    return redirect(url_for("products"))

@app.route("/products/delete/<int:id>")
def products_delete(id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    # ambil produk
    product = Product.query.get_or_404(id)

    # 1) hapus dulu semua detail transaksi yang memakai produk ini
    details = TransactionDetail.query.filter_by(product_id=id).all()
    for d in details:
        db.session.delete(d)

    # 2) baru hapus produknya
    db.session.delete(product)
    db.session.commit()

    return redirect(url_for("products"))

# ---------- CUSTOMERS ----------
@app.route("/customers")
def customers():
    if "user_id" not in session:
        return redirect(url_for("login"))

    all_customers = MallCustomer.query.all()
    return render_template("customers.html", customers=all_customers)

@app.route("/customers/add", methods=["POST"])
def customers_add():
    if "user_id" not in session:
        return redirect(url_for("login"))

    gender = request.form["gender"]
    age = int(request.form["age"])
    income = int(request.form["annual_income"])
    score = int(request.form["spending_score"])

    new_customer = MallCustomer(
        gender=gender,
        age=age,
        annual_income=income,
        spending_score=score,
    )
    db.session.add(new_customer)
    db.session.commit()

    return redirect(url_for("customers"))

@app.route("/customers/delete/<int:id>")
def customers_delete(id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    # 1. ambil customer
    customer = MallCustomer.query.get_or_404(id)

    # 2. cari semua transaksi milik customer ini
    transactions = Transaction.query.filter_by(customer_id=id).all()

    for tx in transactions:
        # 2a. hapus dulu semua detail transaksi dari transaksi tsb
        for d in tx.details:
            db.session.delete(d)

        # 2b. baru hapus transaksi-nya
        db.session.delete(tx)

    # 3. terakhir, hapus customer
    db.session.delete(customer)
    db.session.commit()

    return redirect(url_for("customers"))

# ---------- TRANSACTIONS ----------
@app.route("/transactions")
def transactions_page():
    if "user_id" not in session:
        return redirect(url_for("login"))

    transactions = Transaction.query.all()
    customers = MallCustomer.query.all()
    products = Product.query.all()

    return render_template(
        "transactions.html",
        transactions=transactions,
        customers=customers,
        products=products,
    )

@app.route("/transactions/add", methods=["POST"])
def transactions_add():
    if "user_id" not in session:
        return redirect(url_for("login"))

    customer_id = int(request.form["customer_id"])
    product_id = int(request.form["product_id"])
    quantity = int(request.form["quantity"])

    product = Product.query.get_or_404(product_id)
    subtotal = product.price * quantity

    # buat transaksi
    new_transaction = Transaction(
        customer_id=customer_id,
        total_amount=subtotal,
        payment_method="Cash",
    )
    db.session.add(new_transaction)
    db.session.commit()

    # detail transaksi
    detail = TransactionDetail(
        transaction_id=new_transaction.id,
        product_id=product_id,
        quantity=quantity,
        unit_price=product.price,
        subtotal=subtotal,
    )
    db.session.add(detail)
    db.session.commit()

    return redirect(url_for("transactions_page"))

# =========================
#   RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)



