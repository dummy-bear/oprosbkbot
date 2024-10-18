from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    BigInteger, Text, Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from sqlalchemy import func

engine = create_engine("")

class Base(DeclarativeBase):
    pass


# Модель для таблицы пользователей
class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=True)
    full_name: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    # Связи с заметками и напоминаниями
    opros: Mapped[list["Opros"]] = relationship("Opros", back_populates="user", cascade="all, delete-orphan")
    answers: Mapped[list["Answer"]] = relationship("Answer", back_populates="user", cascade="all, delete-orphan")


# Модель для опросов
class Opros(Base):
    __tablename__ = 'opros'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    opros_name: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    
    user: Mapped["User"] = relationship("User", back_populates="opros")

# Модель для вопросов опросов
class Question(Base):
    __tablename__ = 'questions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    opros_id: Mapped[int] = mapped_column(ForeignKey('opros.id'), nullable=False)
    question: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    
    opros: Mapped["Opros"] = relationship("Opros", back_populates="question")

# Модель для ответов на вопросы опросов
class Answer(Base):
    __tablename__ = 'answers'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    #opros_id: Mapped[int] = mapped_column(ForeignKey('opros.id'), nullable=False)
    quest_id: Mapped[int] = mapped_column(ForeignKey('questions.id'), nullable=False)
    ans: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    
    user: Mapped["User"] = relationship("User", back_populates="answers")
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

Base.metadata.drop_all(engine)    
Base.metadata.create_all(engine)
engine.connect()

new_opros = Opros(id=1, user_id=1, full_name=full_name)
            session.add(new_user)

print(engine)
