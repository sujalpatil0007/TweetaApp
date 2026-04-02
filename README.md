# 🐦 TweetaApp - Django Tweet Application

TweetaApp is a simple social media-style web application built using **Django**.
Users can create, edit, delete, and search tweets, along with authentication features like login, logout, and registration.

---

## 🚀 Features

* 🔐 User Authentication (Login, Logout, Register)
* 📝 Create, Edit, Delete Tweets
* 🔍 Search Tweets (by content and username)
* 🖼️ Image Upload in Tweets
* 👤 User-specific tweet control (only owner can edit/delete)
* 📱 Responsive UI using Bootstrap

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, Bootstrap
* **Database:** SQLite
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
TweetaApp/
│── chaiheadq/        # Main project folder
│── tweet/            # App containing tweet logic
│── templates/        # HTML templates
│── static/           # Static files (CSS, images)
│── manage.py
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/sujalpatil0007/TweetaApp.git
cd TweetaApp
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install django
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start server

```bash
python manage.py runserver
```

---

## 🌐 Usage

* Open browser: `http://127.0.0.1:8000/tweet/`
* Register a new user
* Login and start posting tweets 🚀

---

## 🔐 Environment Variables (IMPORTANT)

Make sure to keep your `SECRET_KEY` safe.
Do NOT expose it in public repositories.

---

## 📸 Screenshots

(Add your project screenshots here)

---

## 📌 Future Improvements

* ❤️ Like button
* 💬 Comments system
* 👤 User profile page
* 🌐 Deployment (Render / Railway / Vercel)

---

## 🙌 Author

**Sujal Patil**

GitHub: https://github.com/sujalpatil0007

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
