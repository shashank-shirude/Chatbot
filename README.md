# Chatbot Application

A full-stack chatbot application with a React frontend and FastAPI backend.

## Project Structure

```
chatbot/
├── frontend/          # React.js application
│   ├── src/
│   |__ index.html   
│   │
│   │    
│   │   
│   ├── public/
│   └── package.json
|   
│
└── backend/           # FastAPI application
    ├── main.py
    ├── requirements.txt
    └── README.md
```

## Quick Start

### 1. Start the Backend (Terminal 1)

```bash
cd backend

# Create virtual environment (first time only)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (first time only)
pip install -r requirements.txt

# Run the server
python main.py
```

The backend will be running at **http://localhost:8000**

### 2. Start the Frontend (Terminal 2)

```bash
cd frontend

# Install dependencies (first time only - if already not done)
npm install

# Start the React app
npm start
```

If you get error or command not found: npm, 
Follow steps to install npm on your system at **https://nodejs.org/en

If you see any vulnerabilities, run:

```bash
npm audit fix --force

#followed by
npm run dev
```

The frontend will be running at **http://localhost:3000**

## Features

### Frontend
- ✨ Modern dark theme with cyan-blue accents
- 💬 Real-time chat interface
- ⚡ Smooth animations and transitions
- 💭 Typing indicator
- 📱 Fully responsive design
- ⌨️ Keyboard support (Enter to send)

### Backend
- 🚀 FastAPI framework
- 💬 RESTful chat endpoint
- 🔄 CORS enabled
- 📝 Conversation history
- 🏥 Health check endpoint
- 📚 Interactive API documentation

## API Documentation

Once the backend is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Testing the API

### Using curl:
```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello!"}'
```

### Using the browser:
The frontend at http://localhost:3000 automatically connects to the backend.

## Customization

### Add AI Integration

The backend currently uses simple rule-based responses. To integrate with OpenAI, LangChain, or other AI services:

1. Open `backend/main.py`
2. Modify the `get_bot_response()` function
3. See `backend/README.md` for examples

### Change Theme Colors

1. Open `frontend/src/Chatbot.css`
2. Modify the color variables and gradients
3. Changes will hot-reload automatically

## Deployment

### Backend Deployment Options:
- **Heroku**: `git push heroku main`
- **AWS Lambda**: Using Mangum adapter
- **Docker**: See backend/README.md
- **DigitalOcean App Platform**

### Frontend Deployment Options:
- **Vercel**: `vercel deploy`
- **Netlify**: `netlify deploy`
- **AWS S3 + CloudFront**
- **GitHub Pages**

## Troubleshooting

### Frontend shows connection error
- Make sure the backend is running on port 8000
- Check that CORS is properly configured in `backend/main.py`

### Backend won't start
- Ensure Python 3.8+ is installed
- Activate virtual environment: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

### Port already in use
```bash
# Backend - change port
uvicorn main:app --reload --port 8001

# Frontend - set PORT environment variable
PORT=3000 npm start
```

## Technologies Used

### Frontend
- React 19
- CSS3 with modern features
- Fetch API for HTTP requests

### Backend
- FastAPI
- Uvicorn (ASGI server)
- Pydantic (data validation)


MIT
