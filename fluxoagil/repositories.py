from fluxoagil.models import Course

class CoursesRepository:
    def get_by_curriculum_and_type(self, curriculumId: str, type: str) -> list:
        # query = select(CurriculumContainsCourse).where(CurriculumContainsCourse.curriculumId == curriculumId)
        # query = select(Course).where(Course.id.in_(query.courseId))
        # return [c._asdict() for c in courses]
        pass

'''|curriculumId|courseID|
|     10     |    1   |'''