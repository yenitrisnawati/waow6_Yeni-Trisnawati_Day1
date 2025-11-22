📌 README.md — Mini Project Flask
🚀 Mini Project Flask – CRUD + Authentication + SQLite

Aplikasi ini adalah mini project menggunakan Flask, SQLite, dan HTML/CSS (pure).
Project ini memiliki fitur autentikasi dan CRUD lengkap untuk Products, Customers, dan Transactions, serta dashboard statistik sederhana.

Aplikasi ini dibuat untuk memenuhi kebutuhan tugas WAOWS6 – Day 1.

🌟 Fitur Utama
🔐 Autentikasi User (Wajib)

Login

Register

Logout

📦 CRUD Products

Tambah produk

Lihat semua produk

Hapus produk

(Update opsional – tidak diwajibkan)

👤 CRUD Customers

Tambah customer

Lihat daftar customer

Hapus customer

(Update opsional)

💰 CRUD Transactions

Tambah transaksi

Menampilkan daftar transaksi

Menghitung total transaksi otomatis

📊 Dashboard

Total users

Total produk

Total customer

Total transaksi

Total penjualan hari ini

🗄 Teknologi yang Digunakan

Python 3.8+

Flask

Flask SQLAlchemy

SQLite Database

HTML + CSS custom (tanpa framework)

Jinja2 Template Engine

📁 Struktur Proyek
project/
│── main.py
│── app.db
│── README.md
│
└── templates/
    ├── home.html
    ├── login.html
    ├── register.html
    ├── products.html
    ├── customers.html
    └── transactions.html
⚙️ Cara Install & Menjalankan Aplikasi
1️⃣ Clone Repository
git clone <url-repo-anda>
cd <nama-folder>
2️⃣ Buat Virtual Environment
python -m venv venv

Aktifkan:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

3️⃣ Install Dependencies
pip install flask flask_sqlalchemy

4️⃣ Jalankan Aplikasi
python main.py

Aplikasi berjalan di:
➡ http://127.0.0.1:5000/

🧱 ERD (Entity Relationship Diagram)

Berikut struktur ERD berdasarkan model database:
users
 - id
 - email
 - password
 - is_active
 - created_at

mall_customer
 - id
 - gender
 - age
 - annual_income
 - spending_score
 - created_at

products
 - id
 - name
 - price
 - stock
 - created_at

transactions
 - id
 - customer_id (FK)
 - transaction_date
 - total_amount
 - payment_method

transaction_details
 - id
 - transaction_id (FK)
 - product_id (FK)
 - quantity
 - unit_price
 - subtotal

Relasi:
1 Customer → banyak Transactions
1 Transaction → banyak TransactionDetails
1 Product → banyak TransactionDetails

Screenshot Aplikasi:

📌 Catatan

Database otomatis dibuat saat aplikasi pertama dijalankan.

Jika ingin reset database, hapus file app.db.

CRUD update bersifat opsional (sesuai instruksi tugas).

🏁 Kesimpulan

Project ini sudah memenuhi semua kriteria WAOWS Day 1:

✔ Autentikasi (Login, Register, Logout)
✔ CRUD (Products, Customers, Transactions)
✔ Terhubung database
✔ UI rapi dan modern
✔ Struktur folder bagus
✔ Tidak ada error


