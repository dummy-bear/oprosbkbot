from sqlalchemy import BigInteger, Integer, Text, ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base


# Модель для таблицы пользователей
class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=True)
    full_name: Mapped[str] = mapped_column(String, nullable=True)

    # Связи с заметками и напоминаниями
    opros: Mapped[list["Opros"]] = relationship("Opros", back_populates="user", cascade="all, delete-orphan")
    answers: Mapped[list["Answer"]] = relationship("Answer", back_populates="user", cascade="all, delete-orphan")


# Модель для опросов
class Opros(Base):
    __tablename__ = 'opros'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    opros_name: Mapped[str] = mapped_column(String, nullable=True)
    
    user: Mapped["User"] = relationship("User", back_populates="opros")
    questions: Mapped[list["Question"]] = relationship("Question", back_populates="opros", cascade="all, delete-orphan")

# Модель для вопросов опросов
class Question(Base):
    __tablename__ = 'questions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    opros_id: Mapped[int] = mapped_column(ForeignKey('opros.id'), nullable=False)
    question: Mapped[str] = mapped_column(Text, nullable=True)
    
    opros: Mapped["Opros"] = relationship("Opros", back_populates="questions")    

# Модель для ответов на вопросы опросов
class Answer(Base):
    __tablename__ = 'answers'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    #opros_id: Mapped[int] = mapped_column(ForeignKey('opros.id'), nullable=False)
    quest_id: Mapped[int] = mapped_column(ForeignKey('questions.id'), nullable=False)
    ans: Mapped[str] = mapped_column(Text, nullable=True)
    
    
    user: Mapped["User"] = relationship("User", back_populates="answers")
