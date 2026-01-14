# 📦 Product Inventory CRUD Application

A simple and clean Django CRUD application for managing product inventory. Built as a learning project to master Django fundamentals and database operations.

## 📸 Screenshots

<img width="1920" height="1080" alt="user_view" src="https://github.com/user-attachments/assets/609be4d5-5d64-481c-b16f-060d40e687a0" />
<img width="1920" height="1080" alt="admin_view" src="https://github.com/user-attachments/assets/ede6f300-2076-47fe-9b9c-59f7958bb2ba" />
<img width="1920" height="1080" alt="edit_view" src="https://github.com/user-attachments/assets/1e59d2d7-7b65-4614-ac9a-2f552dcd1d5b" />
<img width="1920" height="1080" alt="delete_view" src="https://github.com/user-attachments/assets/3f5ce010-01fe-412c-82d9-39e0292eaa86" />

## ✨ Features

- ✅ **Create** - Add new products with details and images
- 📖 **Read** - View all products in an organized table
- ✏️ **Update** - Edit existing product information
- 🗑️ **Delete** - Remove products from inventory
- 👀 **User View** - Read-only product display for customers
- 🔐 **Admin Panel** - Full CRUD operations for administrators
- 🖼️ **Image Upload** - Add product images for better visualization

## 🚀 Quick Start

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd Django_3
```

### 2️⃣ Set up virtual environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up the database
```bash
# Run migrations
python manage.py migrate

# Create admin user (optional but recommended)
python manage.py createsuperuser
```

### 5️⃣ Run the development server
```bash
python manage.py runserver
```

🎉 **Open your browser and visit:** `http://127.0.0.1:8000/`

## 🛠️ Technologies Used

| Technology | Version |
|------------|---------|
| Python     | 3.12    |
| Django     | 6.0.1   |
| Database   | SQLite  |
| Image Processing | Pillow |

## 📁 Project Structure
```
Django_3/
├── app/                    # Main Django application
│   ├── templates/          # HTML templates
│   ├── migrations/         # Database migrations
│   ├── models.py          # Product model
│   ├── views.py           # Business logic
│   ├── forms.py           # Product forms
│   └── urls.py            # URL routing
├── media/                  # Uploaded product images
├── project/                # Django project settings
│   └── settings.py        # Configuration
├── requirements.txt        # Python dependencies
└── manage.py              # Django management script
```

## 🎯 Learning Outcomes

This project helped me understand:
- Django MVT (Model-View-Template) architecture
- Database operations with Django ORM
- Form handling and validation
- File uploads and media management
- URL routing and view functions
- Template rendering and inheritance

## ⚠️ Note

This is a **learning project** created for educational purposes. The `SECRET_KEY` is exposed in `settings.py` for simplicity. In production environments, always use environment variables for sensitive data.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](#license) file for details.

## 🤝 Contributing

Feel free to fork this project and experiment with it! Suggestions and improvements are welcome.

## 📧 Contact

**Om Bhosle** 

---

⭐ If you found this helpful, consider giving it a star!
```ILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
