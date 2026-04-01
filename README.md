# 🚀 FolioHub - Multi-User Portfolio Platform

A high-end, modern, and fully responsive multi-user portfolio platform built with **Django**, **Tailwind CSS**, and **Glassmorphism** design principles. Each user can manage their own professional presence with ease.

---

## ✨ Key Features
- **Multi-User Architecture**: Every user gets a unique, isolated portfolio.
- **Premium Design**: Sophisticated glassmorphism aesthetic with floating animations.
- **Dynamic Slugs**: Access portfolios via clean URLs like `/username`.
- **Customizable**: Toggle project visibility and social links directly from the admin.
- **Data Isolation**: Strict permissions in the admin panel ensure users only see and edit their own content.

---

## 🛠️ Deployment Plan to Vercel

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
