# 📝 Django Blog Site

A modern, full-featured blog platform built with Django, featuring user authentication, CRUD operations, and a beautiful
responsive interface.

## ✨ Features

### Core Functionality

- 🔐 **User Authentication** - Secure registration, login, and logout system
- ✍️ **Article Management** - Full CRUD (Create, Read, Update, Delete) operations for blog posts
- 📸 **Image Upload** - Support for article cover images
- 👤 **User Profiles** - Author attribution for all articles
- 🔒 **Permission Control** - Users can only edit/delete their own articles

### User Interface

- 🎨 **Modern Design** - Clean, professional interface with Tailwind CSS
- 📱 **Responsive Layout** - Mobile-friendly design that works on all devices
- 🌙 **Dark Theme** - Eye-friendly dark color scheme
- ⚡ **Fast & Smooth** - Optimized performance with smooth animations

### Additional Features

- 📊 **Admin Panel** - Django's powerful built-in admin interface
- 🖼️ **Media Handling** - Efficient image storage and serving
- 📝 **Article Summaries** - Optional short descriptions for articles
- 🔍 **SEO Friendly** - Clean URLs and proper meta tags

---

## 🛠️ Technologies Used

| Technology       | Purpose                |
|------------------|------------------------|
| **Django 4.x**   | Backend framework      |
| **Python 3.8+**  | Programming language   |
| **SQLite**       | Database (development) |
| **Tailwind CSS** | Frontend styling       |
| **Pillow**       | Image processing       |
| **HTML5/CSS3**   | Frontend structure     |

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Git
- Virtual environment tool (recommended)

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ZuhriddinRW/Django-Blog-Site.git
cd Django-Blog-Site
```

### 2. Create Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

Made with ⚡ using Django