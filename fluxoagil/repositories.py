from fluxoagil.models import CurriculumContainsCourse, Course
from sqlalchemy import select
from sqlalchemy.orm import Session
from fluxoagil.db.connection import engine

class CoursesRepository:
    def get_by_curriculum_and_type(self, curriculum_id: str, type: str) -> list[dict]:
        query = select(CurriculumContainsCourse.course_id).\
            where(CurriculumContainsCourse.curriculum_id == curriculum_id)

        query = select([Course.id, Course.name, Course.workload_in_hours]).\
            where(Course.id.in_(query))

        with Session(engine) as session:
            result = session.execute(query)
            courses = [c._asdict() for c in result.all()]
                    
        return courses
