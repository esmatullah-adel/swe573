# SWE573 Course Project

The **SWE573 Course Project** is a web application designed to assist individuals in identifying unknown or puzzling objects through community collaboration. Developed as part of the Software Development Practice (SWE573) course, this project leverages the principles of software engineering to address real-world problems in a user-friendly, engaging, and collaborative way.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Database Setup](#database-setup)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **User Authentication**: Secure registration and login system.
- **Profile Management**: Personalized user profiles.
- **Object Posting**: Post images or descriptions of unidentified objects.
- **Commenting System**: Interact with posts through comments, suggestions, or insights.
- **Advanced Search Functionality**: Enhanced search capabilities, ensuring accurate and efficient querying of mystery object data.
- **Geolocation Feature**: Integrated Google Maps API for setting object locations directly within the application.
- **Responsive Design**: Optimized for accessibility and usability across devices.

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Other Tools**: 
  - Requirements managed via `pip` and `requirements.txt`
  - Deployed on a VPS (Virtual Private Server)

## Installation

### Prerequisites

- Python 3.x
- PostgreSQL
- Pip (Python package installer)
- Virtual Environment (optional but recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/esmatullah-adel/swe573.git
   cd swe573
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies if prefer to not use docker:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and configure the following:
   ```env
   DATABASE_URL=postgres://<username>:<password>@<host>:<port>/<database>
   SECRET_KEY=<your-django-secret-key>
   DEBUG=True
   GOOGLE_MAPS_API_KEY=<your_own_google_map_api_key>
   ```

5. Run database migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server if prefer to not use docker:
   ```bash
   python manage.py runserver
   ```

7. If you prefer to use docker, first install docker desktop from https://www.docker.com/products/docker-desktop/. After installation, run docker desktop and then run the following commands:
   ```bash
   docker-compose build
   docker-compose up -d
   ```

## Usage

1. Navigate to `http://127.0.0.1:8000` in your web browser.
2. Register for an account or log in.
3. Create a post by uploading an image or providing a description of the unidentified object.
4. Interact with other users through comments and suggestions.

## Database Setup

This project uses **PostgreSQL** as its database backend. Ensure that your PostgreSQL server is running and that the database specified in the `DATABASE_URL` environment variable is properly configured.

For example, to create a database named `mystery_objects`:

```sql
CREATE DATABASE mystery_objects;
CREATE USER username WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE mystery_objects TO username;
```

Replace `username` and `password` with your PostgreSQL credentials.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project does not currently have a license. If you plan to contribute or use the code, please contact the repository owner for permissions.

## Acknowledgments

- **Instructor and Course**: Software Development Practice (SWE573)
- **University**: Istanbul Boğaziçi University
- **Community**: Thanks to everyone who collaborates and shares their insights on mysterious objects!
