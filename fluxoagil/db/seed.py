
from email.policy import default
from fluxoagil.models import Course, Curriculum, Graduation
from fluxoagil.db.connection import engine
from sqlalchemy.orm import Session

import json

file = open('esw.json')
data = json.load(file)

with Session(engine) as session:
    grad = Graduation(
        id=str(data['id']),
        name=data['title'],
        description="O curso mais legal de todos",
        credits=0,
        workload_in_hours=0
    )

    print('>>> Graduation', grad)
    curricula = []
    for curriculum_id in data['curricula']:
        curriculum = Curriculum(
            id=curriculum_id,
            name=curriculum_id,
            description='',
            graduation_id=grad.id
        )
        curricula.append(curriculum)
        # print(curriculum_id)
        # print(curriculum)

        period = 0
        courses = []
        for courses_in_period in data['curricula'][curriculum_id]['courses']['required']:
            # print('period', period)
            for course_id in courses_in_period:
                course_json = courses_in_period[course_id]
                
                # print('course>>', courses_in_period[course_id])
                course = Course(
                    id=course_id,
                    name=course_json['title'],
                    description='',
                    workload_in_hours=int(course_json['workload']),
                    credits=int(course_json['workload'])/15,
                    default_period=period
                )
                courses.append(course)
            period += 1
                
    session.add(grad)
    session.flush() # Precisa existir a tabela Graduation antes de inserir em Curriculum
    session.add_all(courses)
    session.add_all(curricula)
    session.commit()
    
file.close()
