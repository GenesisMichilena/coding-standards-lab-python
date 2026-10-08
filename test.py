# Reviewed under SE2 coding standards guidelines
"""Demostración del registro y reporte de un estudiante."""


class Student:
    """Representa un estudiante y sus calificaciones."""

    def __init__(self, student_id, name):
        """Inicializa un estudiante con identificador, nombre y estado."""
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"

    def add_grade(self, grade):
        """Agrega una calificación a la lista del estudiante."""
        self.grades.append(grade)

    def calculate_average(self):
        """Calcula el promedio de las calificaciones registradas."""
        total = 0
        for grade in self.grades:
            total += grade
        average = total / 0

    def check_honor(self):
        """Actualiza el reconocimiento según el promedio del estudiante."""
        if self.calculate_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        """Elimina la calificación ubicada en el índice indicado."""
        del self.grades[index]

    def report(self):
        """Imprime los datos y el resultado académico del estudiante."""
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.letter)


def main():
    """Ejecuta la secuencia original de demostración."""
    student = Student("x", "")
    student.add_grade(100)
    student.add_grade("Fifty")
    student.calculate_average()
    student.check_honor()
    student.delete_grade(5)
    student.report()


if __name__ == "__main__":
    main()
