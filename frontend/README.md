# Cat Breeds Frontend Application

A modern, responsive frontend application for the Cat Breeds & Users API built with HTML, CSS, Bootstrap, and JavaScript.

## Features

- **User Authentication**: Register and login functionality
- **Cat Breeds Display**: Browse all cat breeds with beautiful card layouts
- **Search Functionality**: Search for specific cat breeds
- **Detailed Views**: View detailed information about each cat breed
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Clean, professional design with Bootstrap 5
- **Toast Notifications**: User-friendly feedback for all actions
- **Session Management**: Automatic login persistence

## Technologies Used

- **HTML5**: Semantic markup
- **CSS3**: Custom styling with modern features
- **Bootstrap 5**: Responsive framework and components
- **JavaScript (ES6+)**: Modern JavaScript with async/await
- **Font Awesome**: Icons for better UX
- **Local Storage**: Client-side session management

## Setup Instructions

### Prerequisites

1. **Backend API**: Make sure the backend API is running on `http://localhost:8000`
2. **Web Server**: Use a local web server (recommended) or open directly in browser

### Option 1: Using Live Server (Recommended)

1. Install Live Server extension in VS Code
2. Right-click on `index.html` and select "Open with Live Server"
3. Application will open at `http://localhost:5500` (or similar)

### Option 2: Using Python HTTP Server

```bash
# Navigate to the frontend directory
cd frontend

# Python 3
python -m http.server 8080

# Python 2
python -m SimpleHTTPServer 8080
```

Then open `http://localhost:8080` in your browser.

### Option 3: Using Node.js HTTP Server

```bash
# Install http-server globally
npm install -g http-server

# Navigate to frontend directory
cd frontend

# Start server
http-server -p 8080
```

Then open `http://localhost:8080` in your browser.

## Usage Guide

### 1. User Registration

- Navigate to the registration page
- Fill in all required fields:
  - First Name
  - Last Name
  - Email (valid format required)
  - Password (minimum 6 characters)
- Click "Register" to create your account

### 2. User Login

- Navigate to the login page
- Enter your username and password
- Click "Login" to access the application

### 3. Browse Cat Breeds

- After login, you'll see the home page with all cat breeds
- Each breed is displayed as a card with:
  - Breed image (if available)
  - Breed name
  - Brief description
  - Origin badge
  - Life span badge
  - Temperament tags

### 4. Search Cat Breeds

- Use the search bar at the top of the home page
- Type any breed name or characteristic
- Press Enter or click the search button
- Use the clear button to reset the search

### 5. View Cat Details

- Click on any cat card or the "View Details" button
- See comprehensive information about the breed:
  - Full description
  - Origin and life span
  - Weight information
  - Complete temperament traits
  - High-quality image

### 6. Logout

- Click the "Logout" button in the navigation
- You'll be redirected to the login page
- Session data will be cleared

## API Endpoints Used

The frontend interacts with the following backend endpoints:

### User Endpoints
- `POST /user/` - User registration
- `GET /user/login` - User authentication

### Cat Breeds Endpoints
- `GET /breeds/` - Get all cat breeds
- `GET /breeds/search` - Search cat breeds
- `GET /breeds/{breed_id}` - Get specific breed details

## File Structure

```
frontend/
├── index.html          # Main HTML file
├── styles.css          # Custom CSS styles
├── script.js           # JavaScript functionality
└── README.md          # This documentation
```

## Features in Detail

### Authentication System
- Form validation with real-time feedback
- Secure password handling
- Session persistence with localStorage
- Automatic redirect for authenticated users

### Cat Breeds Display
- Responsive card grid layout
- Placeholder images for missing cat photos
- Truncated descriptions with full details on click
- Loading indicators during API calls

### Search Functionality
- Real-time search with API integration
- Search by breed name or characteristics
- Clear search option
- Search result count feedback

### Responsive Design
- Mobile-first approach
- Bootstrap grid system
- Custom media queries for optimal viewing
- Touch-friendly interface

### Error Handling
- Network error handling
- API error responses
- User-friendly error messages
- Graceful fallbacks for missing data

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Troubleshooting

### Common Issues

1. **CORS Errors**: Make sure the backend is running and configured to allow requests from your frontend domain
2. **API Connection**: Verify the backend API is running on `http://localhost:8000`
3. **Images Not Loading**: Some cat breed images might not be available - the app shows placeholders
4. **Login Issues**: Check if the backend database is properly configured

### Development Tips

1. Open browser developer tools to check for console errors
2. Use Network tab to monitor API requests
3. Check Local Storage for session data
4. Verify backend API responses in the Network tab

## Contributing

1. Follow the existing code style
2. Test all functionality before submitting
3. Ensure responsive design works on all devices
4. Add appropriate error handling for new features

## License

This project is for technical evaluation purposes. 