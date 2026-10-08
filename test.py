# Reviewed under SE2 coding standards guidelines
"""Demostración del registro y reporte de un estudiante."""

import math


class Student:
    """Representa un estudiante y sus calificaciones."""

    def __init__(self, student_id, name):
        """Inicializa un estudiante con identificador, nombre y estado."""
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("El ID debe ser un texto no vacío.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("El nombre debe ser un texto no vacío.")

        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades = []

    def add_grade(self, grade):
        """Agrega una calificación a la lista del estudiante."""
        if (
            isinstance(grade, bool)
            or not isinstance(grade, (int, float))
            or not math.isfinite(grade)
            or not 0 <= grade <= 100
        ):
            return False

        self.grades.append(grade)
        return True

    def calculate_average(self):
        """Calcula el promedio de las calificaciones registradas."""
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

    @property
    def letter_grade(self):
        """Devuelve la calificación de letra correspondiente al promedio."""
        average = self.calculate_average()
        if average is None:
            return "N/A"
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        return "F"

    @property
    def is_passed(self):
        """Indica si el promedio cumple el mínimo aprobatorio de 60."""
        average = self.calculate_average()
        return average is not None and average >= 60

    @property
    def pass_status(self):
        """Devuelve el estado académico Passed o Failed."""
        return "Passed" if self.is_passed else "Failed"

    @property
    def honor_roll(self):
        """Indica si el promedio supera 90 y merece Honor Roll."""
        average = self.calculate_average()
        return average is not None and average > 90

    def check_honor(self):
        """Devuelve el estado booleano de Honor Roll."""
        return self.honor_roll

    def delete_grade(self, index):
        """Elimina la calificación ubicada en el índice indicado."""
        del self.grades[index]

    def report(self):
        """Imprime los datos y el resultado académico del estudiante."""
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.letter_grade)


def main():
    """Demuestra validaciones, promedios y estados sin interrumpirse."""
    for student_id, name in (("", "Ana"), ("S-002", " ")):
        try:
            Student(student_id, name)
        except ValueError as error:
            print(f"Estudiante inválido: {error}")

    honor_student = Student("S-001", "Ana Torres")
    for grade in (100, 95, "Fifty", -1, 101):
        if not honor_student.add_grade(grade):
            print(f"Nota inválida ignorada: {grade!r}")

    print(f"Promedio: {honor_student.calculate_average():.2f}")
    print(f"Calificación: {honor_student.letter_grade}")
    print(f"Estado: {honor_student.pass_status}")
    print(f"Honor Roll: {honor_student.honor_roll}")

    failing_student = Student("S-003", "Luis Pérez")
    failing_student.add_grade(55)
    print(f"Estado para {failing_student.name}: {failing_student.pass_status}")


if __name__ == "__main__":
    main()
