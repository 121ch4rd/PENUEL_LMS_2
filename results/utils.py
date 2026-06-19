from .models import Result


def calculate_gpa(student, semester):
    results = Result.objects.filter(
        student=student,
        subject__semester=semester
    )
    total_points = 0
    total_credits = 0
    for result in results:
        total_points += (
            result.grade_point *
            result.subject.credit_hours
        )
        total_credits += (
            result.subject.credit_hours
        )
    if total_credits == 0:
        return 0
    return round(
        total_points / total_credits,
        2
    )

def overall_gpa(student):
    sem1 = calculate_gpa(
        student,
        1
    )
    sem2 = calculate_gpa(
        student,
        2
    )
    return round(
        (sem1 + sem2) / 2,
        2
    )

