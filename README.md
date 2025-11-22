
<div align="center">

# 🚀 Full-Stack Portfolio Website
### Powered by Django REST Framework & Modern Vanilla JS

[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()
[![Backend](https://img.shields.io/badge/Backend-Django%20REST-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Frontend](https://img.shields.io/badge/Frontend-Vanilla%20JS-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)]()
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)]()

<br>

<p align="center">
  <b>A high-performance, single-page portfolio application architected to demonstrate <br> clean API consumption, responsive design, and secure backend logic.</b>
</p>

[View Live Demo](#) · [Report Bug](https://github.com/sinajokarr/Portfolio/issues) · [Request Feature](https://github.com/sinajokarr/Portfolio/issues)

</div>

---

## 📖 Overview

This repository contains the source code for my personal portfolio website. Unlike static templates, this project is a **full-stack application**. It features a robust **Django REST Framework (DRF)** backend that serves dynamic data (skills, projects, biography) to a custom-built **Vanilla JavaScript** frontend.

The goal was to showcase **"Backend Engineering"** capabilities even in a frontend-heavy project, utilizing optimized API endpoints, secure headers, and efficient data serialization.

## ✨ Key Features

* **🔌 Dynamic Content Management:** All content (Bio, Experience, Skills, Projects) is managed via the Django Admin Panel and served via API.
* **⚡ High-Performance Frontend:** Built with pure HTML5/CSS3/JS (No heavy frameworks like React/Vue) for maximum speed and SEO performance.
* **🎨 Modern UI/UX:** Features a "Dark Mode" aesthetic with Glassmorphism effects, CSS Grid layouts, and smooth scroll animations.
* **📱 Fully Responsive:** Optimized for Mobile, Tablet, and Desktop devices.
* **🔒 Secure Contact Form:** Integrated mailing system protected by backend validation.
* **🖼️ Bloom-Style Visuals:** Custom CSS implementation of grid overlays and image masking.

---

## 🛠️ Tech Stack

### Backend (The Core)
* **Framework:** Django 5.x
* **API:** Django REST Framework (DRF)
* **Database:** PostgreSQL (Production) / SQLite (Dev)
* **Utilities:** `django-cors-headers` (CORS Management), `Pillow` (Image Processing)

### Frontend (The Visuals)
* **Logic:** ES6+ Vanilla JavaScript (Fetch API, DOM Manipulation)
* **Styling:** Custom CSS3 (Variables, Flexbox, Grid, Animations)
* **Structure:** Semantic HTML5
* **Fonts:** Inter & Space Grotesk & Syne

---

## 🏗️ Architecture

The project follows a decoupled architecture where Django serves as an API provider and the HTML template acts as a consumer.

```mermaid
graph LR
    A[Client Browser] -- GET /api/ --> B[Django Backend]
    B -- JSON Data --> A
    A -- POST /contact/ --> B
    B -- SMTP Email --> C[Admin Email]
````

-----

## 🚀 Getting Started (Local Setup)

Follow these steps to run the project locally on your machine.

### Prerequisites

  * Python 3.8+
  * Git

### Installation

1.  **Clone the repository**

    ```bash
    git clone [https://github.com/sinajokarr/Portfolio.git](https://github.com/sinajokarr/Portfolio.git)
    cd Portfolio
    ```

2.  **Create a Virtual Environment**

    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Migrations**

    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser (for Admin Panel)**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Server**

    ```bash
    python manage.py runserver
    ```

7.  **Access the App**

      * Website: `http://127.0.0.1:8000/`
      * Admin Panel: `http://127.0.0.1:8000/admin/`

-----

## 🔌 API Endpoints

The frontend consumes the following endpoints exposed by DRF:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/profile/` | Fetches bio, name, and social links. |
| `GET` | `/api/skills/` | Retrieves list of technical skills & percentages. |
| `GET` | `/api/projects/` | Lists portfolio projects with images and links. |
| `GET` | `/api/timeline/` | Returns work experience history. |
| `POST` | `/api/contact/` | Handles contact form submissions. |

-----

## 👨‍💻 Author

**Sina Jokar**

  * **Role:** Backend Engineer | High-Performance API Architect
  * **Location:** Antalya, Türkiye
  * **Email:** [cnajokar11@yahoo.com](mailto:cnajokar11@yahoo.com)
  * **LinkedIn:** [linkedin.com/in/sinajokar](https://www.linkedin.com/in/sinajokar/)
  * **GitHub:** [@sinajokarr](https://github.com/sinajokarr)

-----

## 🤝 Contributing

Contributions, issues, and feature requests are welcome\!
Feel free to check the [issues page](https://www.google.com/url?sa=E&source=gmail&q=https://github.com/sinajokarr/Portfolio/issues).

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

-----

\<div align="center"\>
\<p\>Built with ❤️ and Python by Sina Jokar\</p\>
\</div\>
