// Frontend JavaScript for Cat Breeds App

// Configuration
const API_BASE_URL = 'http://localhost:8000';
let currentUser = null;
let allCats = [];
let currentPage = 'login';

// DOM Elements
const loginForm = document.getElementById('login-form');
const registerForm = document.getElementById('register-form');
const searchInput = document.getElementById('search-input');
const catsContainer = document.getElementById('cats-container');
const loadingSpinner = document.getElementById('loading');
const catDetailContent = document.getElementById('cat-detail-content');
const toastElement = document.getElementById('toast');
const toastMessage = document.getElementById('toast-message');

// Initialize app
document.addEventListener('DOMContentLoaded', function() {
    // Check if user is already logged in
    const savedUser = localStorage.getItem('currentUser');
    if (savedUser) {
        currentUser = JSON.parse(savedUser);
        updateNavigation();
        showPage('home');
    } else {
        showPage('login');
    }
    
    // Event listeners
    loginForm.addEventListener('submit', handleLogin);
    registerForm.addEventListener('submit', handleRegister);
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            searchCats();
        }
    });
});

// Navigation functions
function showPage(page) {
    // Hide all pages
    document.querySelectorAll('.page').forEach(p => p.style.display = 'none');
    
    // Show requested page
    document.getElementById(page + '-page').style.display = 'block';
    document.getElementById(page + '-page').classList.add('fade-in');
    
    currentPage = page;
    
    // Load data for specific pages
    if (page === 'home' && currentUser) {
        loadAllCats();
    }
}

function updateNavigation() {
    if (currentUser) {
        // User is logged in
        document.getElementById('nav-login').style.display = 'none';
        document.getElementById('nav-register').style.display = 'none';
        document.getElementById('nav-home').style.display = 'block';
        document.getElementById('nav-logout').style.display = 'block';
        document.getElementById('nav-user-info').style.display = 'block';
        document.getElementById('user-name').textContent = currentUser.first_name + ' ' + currentUser.last_name;
    } else {
        // User is not logged in
        document.getElementById('nav-login').style.display = 'block';
        document.getElementById('nav-register').style.display = 'block';
        document.getElementById('nav-home').style.display = 'none';
        document.getElementById('nav-logout').style.display = 'none';
        document.getElementById('nav-user-info').style.display = 'none';
    }
}

// Authentication functions
async function handleLogin(e) {
    e.preventDefault();
    
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;
    
    try {
        const response = await fetch(`${API_BASE_URL}/user/login?username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`);
        const data = await response.json();
        
        if (response.ok) {
            currentUser = data.user;
            localStorage.setItem('currentUser', JSON.stringify(currentUser));
            updateNavigation();
            showToast('Login successful!', 'success');
            showPage('home');
            loginForm.reset();
        } else {
            showToast(data.detail || 'Login failed', 'error');
        }
    } catch (error) {
        console.error('Login error:', error);
        showToast('Connection error. Please try again.', 'error');
    }
}

async function handleRegister(e) {
    e.preventDefault();
    
    const userData = {
        first_name: document.getElementById('register-first-name').value,
        last_name: document.getElementById('register-last-name').value,
        email: document.getElementById('register-email').value,
        password: document.getElementById('register-password').value
    };
    
    try {
        const response = await fetch(`${API_BASE_URL}/user/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userData)
        });
        
        const data = await response.json();
        
        if (response.ok) {
            showToast('Registration successful! You can now login.', 'success');
            showPage('login');
            registerForm.reset();
        } else {
            showToast(data.detail || 'Registration failed', 'error');
        }
    } catch (error) {
        console.error('Registration error:', error);
        showToast('Connection error. Please try again.', 'error');
    }
}

function logout() {
    currentUser = null;
    localStorage.removeItem('currentUser');
    updateNavigation();
    showPage('login');
    showToast('Logged out successfully!', 'success');
}

// Cat-related functions
async function loadAllCats() {
    try {
        showLoading(true);
        const response = await fetch(`${API_BASE_URL}/breeds/`);
        const data = await response.json();
        
        if (response.ok) {
            allCats = data.breeds;
            displayCats(allCats);
        } else {
            showToast('Failed to load cat breeds', 'error');
        }
    } catch (error) {
        console.error('Error loading cats:', error);
        showToast('Connection error. Please try again.', 'error');
    } finally {
        showLoading(false);
    }
}

async function searchCats() {
    const query = searchInput.value.trim();
    
    if (!query) {
        displayCats(allCats);
        return;
    }
    
    try {
        showLoading(true);
        const response = await fetch(`${API_BASE_URL}/breeds/search?q=${encodeURIComponent(query)}`);
        const data = await response.json();
        
        if (response.ok) {
            displayCats(data.breeds);
            showToast(`Found ${data.breeds.length} cat breeds`, 'info');
        } else {
            showToast('Search failed', 'error');
        }
    } catch (error) {
        console.error('Search error:', error);
        showToast('Search error. Please try again.', 'error');
    } finally {
        showLoading(false);
    }
}

function clearSearch() {
    searchInput.value = '';
    displayCats(allCats);
}

function displayCats(cats) {
    catsContainer.innerHTML = '';
    
    if (cats.length === 0) {
        catsContainer.innerHTML = `
            <div class="col-12 text-center">
                <div class="alert alert-info alert-custom">
                    <i class="fas fa-info-circle"></i> No cat breeds found.
                </div>
            </div>
        `;
        return;
    }
    
    cats.forEach(cat => {
        const catCard = createCatCard(cat);
        catsContainer.appendChild(catCard);
    });
}

function createCatCard(cat) {
    const col = document.createElement('div');
    col.className = 'col-lg-4 col-md-6 col-sm-12';
    
    const imageUrl = cat.image && cat.image.url ? cat.image.url : null;
    const imageHtml = imageUrl ? 
        `<img src="${imageUrl}" class="card-img-top" alt="${cat.name}" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
         <div class="no-image" style="display: none;">
             <i class="fas fa-cat"></i>
         </div>` :
        `<div class="no-image">
             <i class="fas fa-cat"></i>
         </div>`;
    
    col.innerHTML = `
        <div class="card cat-card" onclick="showCatDetail('${cat.id}')">
            ${imageHtml}
            <div class="card-body">
                <h5 class="card-title">${cat.name}</h5>
                <p class="card-text">${truncateText(cat.description || 'No description available', 100)}</p>
                <div class="mb-3">
                    ${cat.origin ? `<span class="badge bg-primary">${cat.origin}</span>` : ''}
                    ${cat.life_span ? `<span class="badge bg-success">${cat.life_span} years</span>` : ''}
                </div>
                <div class="d-flex flex-wrap mb-2">
                    ${cat.temperament ? cat.temperament.split(',').slice(0, 3).map(trait => 
                        `<span class="badge bg-secondary me-1 mb-1">${trait.trim()}</span>`
                    ).join('') : ''}
                </div>
            </div>
            <div class="card-footer">
                <button class="btn btn-outline-primary w-100" onclick="event.stopPropagation(); showCatDetail('${cat.id}')">
                    <i class="fas fa-eye"></i> View Details
                </button>
            </div>
        </div>
    `;
    
    return col;
}

async function showCatDetail(catId) {
    try {
        showLoading(true);
        const response = await fetch(`${API_BASE_URL}/breeds/${catId}`);
        const cat = await response.json();
        
        if (response.ok) {
            displayCatDetail(cat);
            showPage('cat-detail');
        } else {
            showToast('Failed to load cat details', 'error');
        }
    } catch (error) {
        console.error('Error loading cat details:', error);
        showToast('Connection error. Please try again.', 'error');
    } finally {
        showLoading(false);
    }
}

function displayCatDetail(cat) {
    const imageUrl = cat.image && cat.image.url ? cat.image.url : null;
    const imageHtml = imageUrl ? 
        `<img src="${imageUrl}" class="cat-detail-img" alt="${cat.name}" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
         <div class="no-image cat-detail-img" style="display: none;">
             <i class="fas fa-cat"></i>
         </div>` :
        `<div class="no-image cat-detail-img">
             <i class="fas fa-cat"></i>
         </div>`;
    
    catDetailContent.innerHTML = `
        <div class="card cat-detail-card">
            ${imageHtml}
            <div class="cat-detail-content">
                <h1 class="cat-detail-title">${cat.name}</h1>
                <p class="cat-detail-description">${cat.description || 'No description available for this breed.'}</p>
                
                <div class="row">
                    <div class="col-lg-6">
                        <div class="cat-detail-info">
                            <h5><i class="fas fa-info-circle"></i> Basic Information</h5>
                            <p><strong>Origin:</strong> ${cat.origin || 'Unknown'}</p>
                            <p><strong>Life Span:</strong> ${cat.life_span || 'Unknown'} years</p>
                            ${cat.weight ? `<p><strong>Weight:</strong> ${cat.weight.metric || cat.weight.imperial || 'Unknown'}</p>` : ''}
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="cat-detail-info">
                            <h5><i class="fas fa-heart"></i> Temperament</h5>
                            <div class="d-flex flex-wrap">
                                ${cat.temperament ? cat.temperament.split(',').map(trait => 
                                    `<span class="badge bg-primary me-1 mb-1">${trait.trim()}</span>`
                                ).join('') : '<span class="text-muted">No temperament information available</span>'}
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="text-center mt-4">
                    <button class="btn btn-primary" onclick="showPage('home')">
                        <i class="fas fa-arrow-left"></i> Back to All Breeds
                    </button>
                </div>
            </div>
        </div>
    `;
}

// Utility functions
function showLoading(show) {
    if (show) {
        loadingSpinner.classList.remove('d-none');
        catsContainer.style.opacity = '0.5';
    } else {
        loadingSpinner.classList.add('d-none');
        catsContainer.style.opacity = '1';
    }
}

function showToast(message, type = 'info') {
    const toastBootstrap = new bootstrap.Toast(toastElement);
    
    // Update toast appearance based on type
    const toastHeader = toastElement.querySelector('.toast-header');
    const icon = toastHeader.querySelector('i');
    
    // Reset classes
    icon.className = 'fas me-2';
    
    switch (type) {
        case 'success':
            icon.classList.add('fa-check-circle', 'text-success');
            break;
        case 'error':
            icon.classList.add('fa-exclamation-circle', 'text-danger');
            break;
        case 'warning':
            icon.classList.add('fa-exclamation-triangle', 'text-warning');
            break;
        default:
            icon.classList.add('fa-info-circle', 'text-primary');
    }
    
    toastMessage.textContent = message;
    toastBootstrap.show();
}

function truncateText(text, maxLength) {
    if (text.length <= maxLength) {
        return text;
    }
    return text.substring(0, maxLength) + '...';
}

// Handle search input on Enter key
function handleSearchKeyPress(event) {
    if (event.key === 'Enter') {
        searchCats();
    }
}

// Make functions available globally
window.showPage = showPage;
window.logout = logout;
window.searchCats = searchCats;
window.clearSearch = clearSearch;
window.showCatDetail = showCatDetail; 