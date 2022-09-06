import enum
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
        return f'Curriculum: {self.name} ({self.id})'


class Course(Base):
    __tablename__ = 'course'
    id = Column(String, primary_key=True)
    name = Column(String(50))
    description = Column(String(50))
    credits = Column(Integer)
    workload_in_hours = Column(Integer)

    def __repr__(self) -> str:
        return f'Course: {self.name} ({self.id})'

class CourseType(enum.Enum):
    MANDATORY = 1
    OPTIONAL = 2
    FREE_MODULE = 3

class CurriculumContainsCourse(Base):
    __tablename__ = 'curriculum_contains_course'
    curriculum_id = Column(String, ForeignKey('curriculum.id'), nullable=False, primary_key=True)
    course_id = Column(String, ForeignKey('course.id'), nullable=False, primary_key=True)
    type = Column(enum.Enum(CourseType))

class CoursePreRequisite(Base):
    __tablename__ = 'course_pre_requisite'
    course_id = Column(String, ForeignKey('course.id'), nullable=False, primary_key=True)
    pre_requisite_id = Column(String,  ForeignKey('course.id'), nullable=False, primary_key=True)
    pre_requisite = Column(String(50), nullable=False)

    def __repr__(self) -> str:
        return f'Pre-Requisite: {self.pre_requisite} ({self.pre_requisite_id})'

class CourseCoRequisite(Base):
    __tablename__ = 'course_co_requisite'
    course_id = Column(String, ForeignKey('course.id'), nullable=False, primary_key=True)
    co_requisite_id = Column(String, ForeignKey('course.id'), nullable=False, primary_key=True)
    co_requisite = Column(String(50), nullable=False)

    def __repr__(self) -> str:
        return f'Co-Requisite: {self.co_requisite} ({self.co_requisite_id})'

class CourseEquivalentTo(Base):
    __tablename__ = 'course_equivalent_to'
    course_id = Column(String, ForeignKey('course.id'), nullable=False, primary_key=True)
    equivalente_to_id = Column(String, ForeignKey('course.id'), nullable=False, primary_key=True)
    equivalent_to = Column(String(50), nullable=False)

    def __repr__(self) -> str:
        return f'Equivalent To: {self.equivalent_to} ({self.equivalente_to_id})'
