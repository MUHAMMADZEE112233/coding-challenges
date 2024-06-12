from pydantic import BaseModel


class JoinQuizRequest(BaseModel):
    quiz_id: int
    user_id: str


class JoinQuizResponse(BaseModel):
    message: str
