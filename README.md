📌 README.md — Mini Project Flask
🚀 Mini Project Flask – CRUD + Authentication + SQLite

Aplikasi ini adalah mini project menggunakan Flask, SQLite, dan HTML/CSS (pure).
Project ini memiliki fitur autentikasi dan CRUD lengkap untuk Products, Customers, dan Transactions, serta dashboard statistik sederhana.

Aplikasi ini dibuat untuk memenuhi kebutuhan tugas WAOWS6 – Day 1.

🌟 Fitur Utama
🔐 Autentikasi User (Wajib)

-Login

-Register

-Logout

📦 CRUD Products

-Tambah produk

-Lihat semua produk

-Hapus produk

-(Update opsional – tidak diwajibkan)

👤 CRUD Customers

-Tambah customer

-Lihat daftar customer

-Hapus customer

-(Update opsional)

💰 CRUD Transactions

-Tambah transaksi

-Menampilkan daftar transaksi

-Menghitung total transaksi otomatis

📊 Dashboard

-Total users

-Total produk

-Total customer

-Total transaksi

-Total penjualan hari ini

🗄 Teknologi yang Digunakan

-Python 3.14

-Flask

-Flask SQLAlchemy

-SQLite Database

-HTML + CSS custom (tanpa framework)

-Jinja2 Template Engine

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
-Login: <img width="2856" height="1502" alt="Screenshot 2025-11-23 002013" src="https://github.com/user-attachments/assets/9b551698-2d5e-47a3-a1d8-a146ef2e6f4b" />
-Register: <img width="2812" height="1504" alt="Screenshot 2025-11-23 002147" src="https://github.com/user-attachments/assets/d9c5f56e-034c-485b-8e3a-3e6bca44b98d" />
-Dashboard: <img width="2856" height="1511" alt="Screenshot 2025-11-23 002214" src="https://github.com/user-attachments/assets/4807a138-342f-47c1-932f-85b62f3b6160" />
-Product: <img width="2851" height="1499" alt="Screenshot 2025-11-23 002232" src="https://github.com/user-attachments/assets/a9c2f299-9c31-41a8-9131-01e4502a1dd3" />
-Customers: <img width="2816" height="1488" alt="Screenshot 2025-11-23 002810" src="https://github.com/user-attachments/assets/520f7c06-ae5a-4e75-a581-29a7c9b078a0" />
-Trasaction: <img width="2822" height="1491" alt="Screenshot 2025-11-23 002856" src="https://github.com/user-attachments/assets/61899ce4-d8b5-43a8-b94e-b225defe45ef" />

📌 Catatan

-Database otomatis dibuat saat aplikasi pertama dijalankan.

-Jika ingin reset database, hapus file app.db.

CRUD update bersifat opsional (sesuai instruksi tugas).

🏁 Kesimpulan
Project ini sudah memenuhi semua kriteria WAOWS Day 1:
✔ Autentikasi (Login, Register, Logout)
✔ CRUD (Products, Customers, Transactions)
✔ Terhubung database
✔ UI rapi dan modern
✔ Struktur folder bagus
✔ Tidak ada error


