from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import time

app = FastAPI(title="Chatbot API", version="1.0.0")

# Configure CORS to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request and Response Models
class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    conversation_id: str
    timestamp: float

# In-memory conversation storage (replace with database in production)
conversations = {}

@app.get("/")
async def root():
    """Root endpoint to check if API is running"""
    return {
        "message": "Chatbot API is running",
        "version": "1.0.0",
        "endpoints": {
            "/chat": "POST - Send a message and get a response",
            "/health": "GET - Check API health status"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": time.time()}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat endpoint that receives a message and returns a bot response
    
    You can replace the get_bot_response function with your actual AI/ML model
    """
    try:
        if not request.message or not request.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        # Generate conversation ID if not provided
        conversation_id = request.conversation_id or f"conv_{int(time.time() * 1000)}"
        
        # Store conversation (optional)
        if conversation_id not in conversations:
            conversations[conversation_id] = []
        
        conversations[conversation_id].append({
            "user": request.message,
            "timestamp": time.time()
        })
        
        # Get bot response
        bot_response = get_bot_response(request.message)
        
        conversations[conversation_id].append({
            "bot": bot_response,
            "timestamp": time.time()
        })
        
        return ChatResponse(
            response=bot_response,
            conversation_id=conversation_id,
            timestamp=time.time()
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

def get_bot_response(message: str) -> str:
    """
    Simple bot response logic
    
    Replace this with your actual AI model, LangChain, OpenAI API, or other AI service
    """
    message_lower = message.lower()
    
    # Simple rule-based responses
    if any(greeting in message_lower for greeting in ["hello", "hi", "hey", "good morning", "good afternoon"]):
        return "Hello! How can I assist you today?"
    
    elif any(word in message_lower for word in ["help", "support"]):
        return "I'm here to help! You can ask me questions, and I'll do my best to assist you. What would you like to know?"
    
    elif any(word in message_lower for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day! Feel free to come back anytime."
    
    elif "how are you" in message_lower:
        return "I'm doing great, thank you for asking! How can I help you today?"
    
    elif "what can you do" in message_lower or "your capabilities" in message_lower:
        return "I'm a chatbot assistant. I can answer questions, provide information, and have conversations with you. What would you like to talk about?"
    
    elif "weather" in message_lower:
        return "I don't have access to real-time weather data yet, but you can check your local weather service for accurate information!"
    
    elif "joke" in message_lower:
        return "Why don't scientists trust atoms? Because they make up everything! 😄"
    
    elif "thank" in message_lower:
        return "You're welcome! Is there anything else I can help you with?"
    
    elif any(question in message_lower for question in ["?", "what", "when", "where", "why", "how", "who"]):
        return f"That's an interesting question about '{message}'. I'm currently a simple chatbot, but I'm learning! Could you tell me more about what you'd like to know?"
    
    else:
        return "I understand you're saying: '" + message + "'. That's interesting! Could you tell me more, or is there something specific I can help you with?"

@app.get("/conversations/{conversation_id}")
async def get_conversation(conversation_id: str):
    """Get conversation history by ID"""
    if conversation_id not in conversations:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    return {
        "conversation_id": conversation_id,
        "messages": conversations[conversation_id]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
