# 🚀 FolioHub - Multi-User Portfolio Platform

A high-end, modern, and fully responsive multi-user portfolio platform built with **Django**, **Tailwind CSS**, and **Glassmorphism** design principles. Each user can manage their own professional presence with ease.

---

## 🌟 Project Overview
**FolioHub** is a sophisticated platform that allows multiple users to create, manage, and showcase their professional portfolios through a centralized, high-performance web application. Designed for freelancers, developers, and creative professionals, it offers a seamless blend of aesthetics and functionality.

---

## ✨ Key Features

### 👤 Multi-User Architecture
- **Unique Slugs**: Each user has their own dedicated portfolio page accessible via a clean, professional URL (e.g., `yourdomain.com/username`).
- **Profile Customization**: Users can personalize their bio, profile image, and social media links (LinkedIn, GitHub, Twitter).
- **Project Showcase**: Users can add multiple projects, each with its own title, description, and visibility toggle.

### 🔒 Admin & Data Isolation
- **Staff User Isolation**: A custom Django admin implementation ensures that staff users can **only see and edit their own** profiles and projects.
- **Role-Based Access**: Superusers maintain full oversight of the entire platform, while regular users have an isolated workspace.
- **Easy Management**: Add, update, or hide projects with a single click.

### 🎨 Premium UI/UX
- **Glassmorphism Design**: A modern aesthetic featuring frosted glass effects, subtle blurs, and elegant transparencies.
- **Responsive Layout**: Fully optimized for mobile, tablet, and desktop viewing.
- **Interactive Elements**: Smooth hover effects and floating animations powered by Tailwind CSS.

### ☁️ Serverless & Cloud Ready
- **Vercel Optimized**: Built to run on Vercel's high-speed serverless infrastructure.
- **Neon Postgres**: Integration with Neon for a persistent, scalable database.
- **Cloudinary Integration**: Persistent, high-speed storage for user profile images and project assets.
- **WhiteNoise Static Serving**: High-performance serving of CSS and JavaScript files in production.

---

## 🏗️ Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Django 5.1+, Python 3.12 |
| **Frontend** | Tailwind CSS, Glassmorphism UI |
| **Database** | Neon Postgres (Production), SQLite (Local) |
| **Storage** | Cloudinary (Media), WhiteNoise (Static) |
| **Deployment** | Vercel (Serverless Functions) |

---

## 📂 Project Structure

- **`core/`**: The heart of the application, containing the `Profile` and `Project` models, portfolio views, and admin customizations.
- **`portfolio_project/`**: Project-level settings, URLs, and WSGI/ASGI configurations.
- **`index.py`**: The main serverless entry point for Vercel, handling runtime migrations and application initialization.
- **`vercel.json`**: Configuration for Vercel deployments, defining runtimes and routing.
- **`requirements.txt`**: Complete list of Python dependencies for a stable environment.

---

## 🛠️ Deployment Instructions

Follow these steps to deploy your project to Vercel:

### 1. Push Your Code to GitHub
Ensure all your latest changes are pushed to your repository:
```bash
git add .
git commit -m "chore: finalize design and deployment preparation"
git push origin main
```

### 2. Connect to Vercel
- Log in to [Vercel](https://vercel.com/) with your GitHub account.
- Click **"New Project"**.
- Import the `Portfolio` repository.

### 3. Configure Environment Variables
Vercel requires specific variables to run your Django project securely. In the project settings, add:
- `DEBUG`: `False`
- `SECRET_KEY`: (A long, unique, and random string)
- `DATABASE_URL`: **IMPORTANT** Your managed Postgres connection string (e.g., from Supabase or Neon). 
- `ALLOWED_HOSTS`: `.vercel.app`
- `CLOUDINARY_CLOUD_NAME`: Your Cloudinary Cloud Name
- `CLOUDINARY_API_KEY`: Your Cloudinary API Key
- `CLOUDINARY_API_SECRET`: Your Cloudinary API Secret

> **⚠️ NOTE on Persistence**: Without a `DATABASE_URL`, Vercel will use a temporary SQLite database. For your data to stay permanent, you **must** connect a Postgres database. Similarly, for media files (images), you **must** provide Cloudinary credentials.

### 4. Build & Deploy
- Vercel will use the `index.py`, `vercel.json`, and `requirements.txt` to build and route your project.
- Click **"Deploy"** and wait for the process to finish.

### 5. Post-Deployment (Database & Media)
- **Migrations**: Handled automatically at startup via `index.py`.
- **Media Storage**: This project uses **Cloudinary** for permanent free media storage. 
  1. Create a free [Cloudinary](https://cloudinary.com/) account.
  2. Copy your **Cloud Name**, **API Key**, and **API Secret** from the Cloudinary Dashboard.
  3. Add them to your Vercel Environment Variables as shown above.

---

## 💻 Local Development

### Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```

### Admin Access
- **Superuser**: Full control over all data.
- **Staff Users**: Can only manage their own `Profile` and `Projects`.

---

Built with passion and Django. 🚀
