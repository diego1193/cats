# Cat Breeds & Users API - Full Stack Application

A Full Stack application with FastAPI backend and modern frontend implementing cat breeds and user management functionality.

## Features

### Backend Features
- **Cat Breeds Management**: Get all breeds, search specific breeds, and retrieve breed details from TheCatAPI
- **User Management**: User registration, authentication, and management
- **Clean Architecture**: Follows SOLID principles and layered architecture
- **MongoDB Integration**: NoSQL database for user data
- **Docker Support**: Containerized application with MongoDB
- **Unit Tests**: Comprehensive test coverage
- **API Documentation**: Interactive Swagger documentation

### Frontend Features
- **User Authentication**: Register and login functionality with modern UI
- **Cat Breeds Display**: Browse all cat breeds with beautiful card layouts
- **Search Functionality**: Search for specific cat breeds
- **Detailed Views**: View detailed information about each cat breed
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Clean, professional design with Bootstrap 5
- **Toast Notifications**: User-friendly feedback for all actions
- **Session Management**: Automatic login persistence

## Architecture

The project follows Clean Architecture principles with the following layers:

- **Domain Layer** (`backend/app/core/`): Entities, repositories interfaces, and services
- **Infrastructure Layer** (`backend/app/infrastructure/`): Database and external API implementations
- **Presentation Layer** (`backend/app/presentation/`): Controllers, schemas, and API routes
- **Frontend Layer** (`frontend/`): HTML, CSS, JavaScript with Bootstrap 5

## API Endpoints

### Cat Breeds
- `GET /breeds/` - Get all cat breeds
- `GET /breeds/{breed_id}` - Get specific cat breed
- `GET /breeds/search` - Search cat breeds with query parameters

### Users
- `GET /user/` - Get all users
- `POST /user/` - Create new user
- `GET /user/login` - User authentication

**Note**: Username format for login is `firstname.lastname` (all lowercase). For example, if your name is "John Doe", your username would be `john.doe`.

## Setup

### Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Web browser (for frontend)

### Environment Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd prueba_tecnica
   ```

2. **Create Python virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

## Running the Application

### Option 1: Docker Compose (Recommended)

1. **Build and run with Docker Compose**
   ```bash
   cd backend
   docker-compose up --build
   ```

   This will start:
   - MongoDB on port 27017
   - FastAPI backend on port 8000

2. **Access the Frontend**
   
   Open the frontend in your browser using one of these methods:
   
   **Method 1: Direct File Access (Simplest)**
   - Navigate to the `frontend/` directory
   - Double-click on `index.html` to open it directly in your browser
   - The application will work with the file:// protocol

   **Method 2: Using Live Server (VS Code)**
   - Install Live Server extension in VS Code
   - Right-click on `frontend/index.html` and select "Open with Live Server"
   - Application will open at `http://localhost:5500` (or similar)

   **Method 3: Using Python HTTP Server**
   ```bash
   cd frontend
   python -m http.server 8080
   ```
   Then open `http://localhost:8080` in your browser.

   **Method 4: Using Node.js HTTP Server**
   ```bash
   npm install -g http-server
   cd frontend
   http-server -p 8080
   ```
   Then open `http://localhost:8080` in your browser.

### Option 2: Local Development

1. **Start MongoDB locally**
   ```bash
   docker run -d -p 27017:27017 --name mongodb mongo:7.0
   ```

2. **Set environment variables**
   ```bash
   export MONGODB_URL=mongodb://localhost:27017
   export DATABASE_NAME=catapp
   export CAT_API_KEY=live_JBT0Ah0Nt12iyl2IpjQVLDWjcLk0GQwf4zI9wBMfmfejKmcC31mOJp4yJz5TsOUP
   ```

3. **Run the backend**
   ```bash
   cd backend
   python main.py
   ```

4. **Serve the frontend**
   ```bash
   cd frontend
   python -m http.server 8080
   ```

## Access Points

- **Backend API**: `http://localhost:8000`
- **Frontend Application**: `http://localhost:8080` (or your chosen port)
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## User Authentication

### Registration
- Navigate to the frontend registration page
- Fill in all required fields (First Name, Last Name, Email, Password)
- After registration, your username will be automatically generated as `firstname.lastname` (all lowercase)

### Login
- Use your generated username format: `firstname.lastname` (all lowercase)
- Example: If you registered as "John Doe", login with username `john.doe`

## Testing

Run the unit tests:

```bash
cd backend
pytest
```

Run tests with coverage:

```bash
cd backend
pytest --cov=app tests/
```

## Project Structure

```
prueba_tecnica/
├── backend/                    # Backend application
│   ├── app/
│   │   ├── core/              # Domain layer
│   │   │   ├── entities/      # Domain entities
│   │   │   ├── repositories/  # Repository interfaces
│   │   │   └── services/      # Business logic
│   │   ├── infrastructure/    # Infrastructure layer
│   │   │   ├── database/      # MongoDB implementation
│   │   │   └── external/      # External APIs
│   │   └── presentation/      # Presentation layer
│   │       ├── controllers/   # API controllers
│   │       └── schemas/       # Request/Response schemas
│   ├── tests/                 # Unit tests
│   ├── main.py               # Application entry point
│   ├── requirements.txt      # Python dependencies
│   ├── Dockerfile           # Docker configuration
│   └── docker-compose.yml   # Docker Compose configuration
├── frontend/                  # Frontend application
│   ├── index.html           # Main HTML file
│   ├── styles.css           # Custom CSS styles
│   ├── script.js            # JavaScript functionality
│   └── README.md           # Frontend documentation
└── README.md               # This file
```

## Technologies Used

### Backend
- **FastAPI**: Modern web framework for building APIs
- **MongoDB**: NoSQL database with Motor async driver
- **Pydantic**: Data validation and settings management
- **httpx**: HTTP client for external API calls
- **pytest**: Testing framework
- **Docker**: Containerization
- **bcrypt**: Password hashing
- **TheCatAPI**: External API for cat breed data

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Custom styling with modern features
- **Bootstrap 5**: Responsive framework and components
- **JavaScript (ES6+)**: Modern JavaScript with async/await
- **Font Awesome**: Icons for better UX
- **Local Storage**: Client-side session management

## Contributing

1. Follow the existing code structure and Clean Architecture principles
2. Add unit tests for new features
3. Update documentation as needed
4. Use type hints throughout the codebase
5. Test frontend functionality across different browsers
6. Ensure responsive design works on all devices

## License

This project is for technical evaluation purposes. 