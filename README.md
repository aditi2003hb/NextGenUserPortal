# 📝 FastAPI User Registration System

A simple, beginner-friendly **User Registration** backend built using **FastAPI** + **SQLite**, with a clean HTML frontend UI.  
This project is perfect for learning FastAPI, Pydantic, SQLAlchemy ORM, and how to build a working full-stack backend app locally.

---

## 🌟 Features

- ✅ Register a user with:
  - First Name
  - Age
  - Permanent String Code
  - State
  - Country
- ✅ Data is stored in a local SQLite database
- ✅ Beautiful HTML form UI
- ✅ Jinja2 rendering
- ✅ Clean project structure
- ✅ Fully working on `localhost:8000`

---

## 📸 UI Preview

![User Registration UI](./6e473de2-be0f-4455-aadb-92672433c93a.png)

---

## 🚀 Technologies Used

- **[FastAPI](https://fastapi.tiangolo.com/)**
- **SQLite** (via SQLAlchemy ORM)
- **Pydantic** for validation
- **Jinja2** for HTML rendering
- **HTML + CSS** frontend

---

## 🛠️ Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/aditi2003hb/fastapi_user_registration.git
cd fastapi_user_registration

# 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate        # On Windows
# or
source venv/bin/activate     # On Linux/macOS

# 3. Install dependencies
pip install fastapi sqlalchemy pydantic jinja2 hypercorn

# 4. Run the application using Hypercorn
hypercorn app.main:app --reload
```

---

## 🔗 Access the App

Once the server is running, go to:

```
http://127.0.0.1:8000
```

You’ll see the user registration form.

---

## 🗃️ Project Structure

```
fastapi_user_registration/
│
├── app/
│   ├── main.py                # FastAPI app entrypoint
│   ├── models.py              # SQLAlchemy models
│   ├── schemas.py             # Pydantic schemas
│   ├── database.py            # DB connection setup
│   ├── templates/             # HTML files (Jinja2)
│   │   ├── index.html         # Form page
│   │   └── success.html       # Success page
│
├── 6e473de2-be0f-4455-aadb-92672433c93a.png   # Screenshot image for README
├── README.md
└── requirements.txt
```

---

## 🙋‍♀️ Author

**Aditi H. ([@aditi2003hb](https://github.com/aditi2003hb))**  
📧 CSE Student | AI Enthusiast | Python + FastAPI Developer

---

## 📃 License

This project is open source and available under the [MIT License](LICENSE).
