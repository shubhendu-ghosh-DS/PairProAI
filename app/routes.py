from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.services import generate_code

router = APIRouter()

# Request Model
class CodeRequest(BaseModel):
    code: str = Field(..., example="print('Hello, World!')")
    option: str = Field(..., example="Code Translation")
    target_language: str | None = Field(None, example="Java")
    error_message: str | None = Field(None, example="SyntaxError: invalid syntax")

# Response Model
class CodeResponse(BaseModel):
    code: str
    explanation: str

@router.post("/generate", response_model=CodeResponse)
async def generate_solution(request: CodeRequest):
    try:
        generated_code, explanation = generate_code(
            request.code, request.option, request.target_language, request.error_message
        )
        return {"code": generated_code, "explanation": explanation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
