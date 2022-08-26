from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from .db.connection import Base

class Graduation(Base):
    __tablename__ = 'graduation'
    id = Column(String, primary_key=True)
    name = Column(String(50))
    description = Column(String(50))
    url = Column(String(80))
    credits = Column(Integer)
    workload_in_hours = Column(Integer)

    def __repr__(self) -> str:
        return f'Graduation: {self.name} ({self.id})'


class Curriculum(Base):
    __tablename__ = 'curriculum'
    id = Column(String, primary_key=True)
    name = Column(String(50))
    description = Column(String(50))
    graduation_id = Column(String, ForeignKey('graduation.id'), nullable=False)

    def __repr__(self) -> str:
        return f'Currículo: {self.name} ({self.id})'


class Course(Base):
    __tablename__ = 'course'
    id = Column(String, primary_key=True)
    name = Column(String(50))
    description = Column(String(50))
    credits = Column(Integer)
    workload_in_hours = Column(Integer)

    def __repr__(self) -> str:
        return f'Course: {self.name} ({self.id})'


class CurriculumContainsCourse(Base):
    __tablename__ = 'curriculum_contains_course'
    name = Column(String(50))
    curriculum_id = Column(String, ForeignKey('curriculum.id'), nullable=False, primary_key=True)
    course_id = Column(String, ForeignKey('course.id'), nullable=False, primary_key=True)
