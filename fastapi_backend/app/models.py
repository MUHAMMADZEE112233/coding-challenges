from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class QuizSession(Base):
    __tablename__ = "quiz_sessions"
    quiz_id = Column(Integer, primary_key=True, index=True)
    quiz_name = Column(String, index=True)

class QuizParticipant(Base):
    __tablename__ = "quiz_participants"
    participant_id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quiz_sessions.quiz_id"))
    user_id = Column(String, index=True)
