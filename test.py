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
            or not 0 <= grade <= 100
            or not math.isfinite(grade)
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
        """Indica si el promedio de 90 o más merece Honor Roll."""
        average = self.calculate_average()
        return average is not None and average >= 90

    def check_honor(self):
        """Devuelve el estado booleano de Honor Roll."""
        return self.honor_roll

    def delete_grade(self, index):
        """Elimina una calificación por índice; devuelve False si no existe."""
        if (
            isinstance(index, bool)
            or not isinstance(index, int)
            or not 0 <= index < len(self.grades)
        ):
            return False
        del self.grades[index]
        return True

    def delete_grade_by_value(self, grade):
        """Elimina la primera nota igual al valor indicado, si existe."""
        try:
            self.grades.remove(grade)
        except ValueError:
            return False
        return True

    def report(self):
        """Imprime el reporte académico completo del estudiante."""
        average = self.calculate_average()
        average_text = f"{average:.2f}" if average is not None else "N/A"
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Average: {average_text}")
        print(f"Final Grade: {self.letter_grade}")
        print(f"Status: {self.pass_status}")
        print(f"Honor Roll: {self.honor_roll}")


def main():
    """Demuestra los requisitos académicos y el manejo de errores."""
    for student_id, name in (("", "Ana"), ("S-002", " ")):
        try:
            Student(student_id, name)
        except ValueError as error:
            print(f"Estudiante inválido: {error}")

    honor_student = Student("S-001", "Ana Torres")
    for grade in (100, 80, "Fifty", -1, 101):
        if not honor_student.add_grade(grade):
            print(f"Nota inválida ignorada: {grade!r}")

    print("Reporte del estudiante con promedio exacto de 90:")
    honor_student.report()

    failing_student = Student("S-003", "Luis Pérez")
    failing_student.add_grade(55)
    print("Reporte del estudiante reprobado:")
    failing_student.report()

    deletion_student = Student("S-004", "Caso de eliminación")
    deletion_student.add_grade(0)
    deletion_student.add_grade(100)
    print(f"Índice inválido rechazado: {not deletion_student.delete_grade(5)}")
    print(
        "Valor inexistente rechazado: "
        f"{not deletion_student.delete_grade_by_value(50)}"
    )
    print(f"Eliminación por índice exitosa: {deletion_student.delete_grade(0)}")
    print(
        "Eliminación por valor exitosa: "
        f"{deletion_student.delete_grade_by_value(100)}"
    )


if __name__ == "__main__":
    main()
