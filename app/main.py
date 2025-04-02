from fastapi import FastAPI, HTTPException, Depends
from routes import router

app = FastAPI(title="PairProAI", description="AI-powered pair programming API")

# Include Routes
app.include_router(router)

@app.get("/")
def health_check():
    return {"message": "PairProAI API is running"}
