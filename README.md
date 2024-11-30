
---

# Course and Student Management System

This project is a **Course and Student Management System** built using the Django framework. It provides an intuitive web interface for managing courses and students, allowing administrators to create, update, and view courses and student details.

## Features

### Course Management
- Add new courses with details like:
  - Title
  - Description
  - Start date
  - End date
  - Maximum number of students
- View a list of all available courses with their respective details.

### Student Management
- Add new students with information such as:
  - First and last name
  - Email
  - Date of birth
  - Address
  - Gender
- View the complete list of students.

## Screenshots

### Course Management
![Course Management Screenshot](https://github.com/user-attachments/assets/a2784b5a-8a89-49e5-b46f-d716a81f0274)

### Student Management
![Student Management Screenshot](https://github.com/user-attachments/assets/cdda0d5d-2391-4072-8c5d-c8a0522c7168)

## Prerequisites

- Python 3.8+
- Django 4.0+
- A database (SQLite is configured by default)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**
   Open your browser and navigate to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## File Structure

```
project/
├── course_management/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   └── urls.py
├── student_management/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md
```

## Technologies Used

- **Backend Framework:** Django
- **Frontend:** HTML, CSS (with dark mode styling)
- **Database:** SQLite (default)

## Future Improvements

- Add search and filter functionality for courses and students.
- Implement authentication for administrators.
- Allow students to self-register for courses.

## Contributing

Contributions are welcome! Please fork this repository and create a pull request for any feature or bug fix.

## License

This project is licensed under the Astrum.

---
