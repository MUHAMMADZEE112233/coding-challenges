from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db, Base, engine
from app.models import QuizSession, QuizParticipant
from app.schemas import JoinQuizRequest, JoinQuizResponse

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/joinQuiz", response_model=JoinQuizResponse)
async def join_quiz(request: JoinQuizRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(QuizSession).where(QuizSession.quiz_id == request.quiz_id)
    )
    quiz_session = result.scalars().first()
    if not quiz_session:
        raise HTTPException(status_code=400, detail="Invalid Quiz ID")

    new_participant = QuizParticipant(quiz_id=request.quiz_id, user_id=request.user_id)
    db.add(new_participant)
    await db.commit()

    return JoinQuizResponse(message="Joined the quiz successfully")
