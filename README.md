# 🎓 Academix – E-Learning & Academic Management Platform

![Academix Banner](https://img.shields.io/badge/Django-5.x-green?style=for-the-badge&logo=django)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)
![Made with ❤️ by Ayush](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F%20by%20Ayush-blueviolet?style=for-the-badge)

Academix is a powerful web-based academic platform built using **Django**, offering role-based dashboards and modern tools for students, teachers, and administrators. It simplifies education workflows, communication, and performance tracking — all in one beautiful and responsive interface.

---

## 🚀 Features

### 🧑‍🏫 Teacher Dashboard

- 👤 Manage profile
- 📹 Host or join live classes
- 📊 Mark and view attendance
- 📝 Upload marks
- 📁 Share notes and assignments
- 📢 Post announcements to selected students/sections

### 👨‍🎓 Student Dashboard

- 📜 Submit fee receipt and get approved
- 📚 View announcements, notes, assignments
- 📈 Track marks and attendance
- 🔔 Notification view (coming soon)

### 👨‍💼 Admin Panel

- 👩‍🏫 Manage teachers
- 🧑‍🎓 Manage students
- 🗂 Approve fee submissions
- 📢 Post announcements to entire departments or individuals
- 📊 Overview dashboard with metrics (planned)

---

## 🛠️ Tech Stack

| Frontend                      | Backend         | Database | Auth        | Styling                          |
| ----------------------------- | --------------- | -------- | ----------- | -------------------------------- |
| HTML, TailwindCSS, JavaScript | Django (Python) | MySQL    | Django Auth | Tailwind + Google Material Icons |

---

## 📸 Screenshots

> _Add screenshots or GIFs here if available._

---

## 🔧 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/academix.git
cd academix

# Create a virtual environment and activate it
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

```
