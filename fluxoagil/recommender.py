
import json
from itertools import product
from mip import Model, xsum, BINARY


def _get_curriculum_courses_by_id(curriculum_id: str) -> tuple[list, list]:
    mandatory_courses = json.load(
        open("static/courses.json", "r"))[curriculum_id]
    optional_courses = json.load(
        open("static/optional_courses.json", "r"))[curriculum_id]

    return (mandatory_courses,
            optional_courses,
            [*mandatory_courses, *optional_courses])


def _get_nested_course_prerequisites(course: dict, curriculum_courses: list) -> list:
    """given a course id, returns all prerequisites of prerequisites"""

    nested_prerequisites = []

    if len(course["prerequisites"]) != 0:

        for prerequisite_id in course["prerequisites"]:
            prerequisite_course = next(
                filter(lambda c: c["id"] == prerequisite_id, curriculum_courses), None)

            nested_prerequisites.append(prerequisite_course)

            nested_prerequisites.extend(_get_nested_course_prerequisites(
                prerequisite_course, curriculum_courses))

    return nested_prerequisites


def _get_missing_courses(curriculum_id: str, approved: list, optionals: list) -> list:
    """(mandatory + optional) - approved = missing"""

    (mandatory_courses,
     optional_courses,
     all_courses) = _get_curriculum_courses_by_id(curriculum_id)

    def filter_missing(mandatory_course):
        def find_approved(approved_course_id):
            return approved_course_id == mandatory_course["id"]

        return not next(filter(find_approved, approved), None)

    missing_mandatory_courses = list(filter(filter_missing, mandatory_courses))

    optional_courses = list(
        filter(lambda c: c["id"] in optionals, all_courses))

    missing_courses = [*missing_mandatory_courses, *optional_courses]
    missing_courses_with_prerequisites = [*missing_courses]

    for missing_course in missing_courses:
        missing_course_prerequisites = _get_nested_course_prerequisites(
            missing_course, all_courses)

        for prerequisite_course in missing_course_prerequisites:
            if prerequisite_course in missing_courses:
                continue

            if prerequisite_course["id"] in approved:
                continue

            missing_courses_with_prerequisites.append(prerequisite_course)

    return missing_courses_with_prerequisites


def _get_recommendation_structure(max_credits_by_period, courses):
    courses_map = {}
    for index, course in enumerate(courses):
        courses_map[index + 1] = course

    n_courses_count = len(courses)
    p_courses_time_consumption = [0, *([1] * n_courses_count), 0]
    u_courses_credits = [
        [0, 0], *list(map((lambda c: [c["credits"], 0]), courses)), [0, 0]]
    c_max_credits_by_period = [max_credits_by_period, 0]

    s_precedence = []

    for course_index, course in courses_map.items():
        if len(course["prerequisites"]) > 0:
            for prerequisite_id in course["prerequisites"]:
                prerequisite_index = [
                    k for k, v in courses_map.items() if v["id"] == prerequisite_id]

                if len(prerequisite_index) > 0:
                    s_precedence.append([prerequisite_index[0], course_index])
        else:
            s_precedence.append([0, course_index])

        prerequisite_sublist = list(
            map(lambda c: c["prerequisites"], list(courses_map.values())))

        all_prerequisite_ids = [
            item for sublist in prerequisite_sublist for item in sublist]

        if course["id"] not in all_prerequisite_ids:
            s_precedence.append([course_index, n_courses_count + 1])

    return (n_courses_count,
            p_courses_time_consumption,
            u_courses_credits,
            c_max_credits_by_period,
            s_precedence,
            courses_map)


def get_recommendation(settings: dict, approved: list, optionals: list = []) -> list:
    curriculum_id = settings["curriculumId"]
    max_credits_by_period = settings["maxCreditsByPeriod"]

    missing_courses = _get_missing_courses(curriculum_id, approved, optionals)

    (n, p, u, c, S, courses_map) = _get_recommendation_structure(
        max_credits_by_period, missing_courses)

    (R, J, T) = (range(len(c)), range(len(p)), range(sum(p)))

    model = Model()

    x = [[model.add_var(name="x({},{})".format(j, t), var_type=BINARY)
          for t in T] for j in J]

    model.objective = xsum(t * x[n + 1][t] for t in T)

    for j in J:
        model += xsum(x[j][t] for t in T) == 1

    for (r, t) in product(R, T):
        model += (
            xsum(u[j][r] * x[j][t2]
                 for j in J for t2 in range(max(0, t - p[j] + 1), t + 1))
            <= c[r])

    for (j, s) in S:
        model += xsum(t * x[s][t] - t * x[j][t] for t in T) >= p[j]

    model.optimize(max_seconds=60)

    periods_count = int(model.objective_value)
    periods = [[0 for x in range(0)] for y in range(periods_count)]

    print("Recomendação: ")
    for (course_index, period) in product(J, T):
        if x[course_index][period].x >= 0.99 and course_index in courses_map:
            course = courses_map[course_index]
            print("{} no {} semestre".format(course, period))

            periods[period].append(course)

    print("Quantidade de semestres necessários {}".format(periods_count))

    return {
        "maxCreditsByPeriod": max_credits_by_period,
        "periods": periods
    }
