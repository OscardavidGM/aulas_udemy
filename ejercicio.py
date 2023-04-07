class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade


class RegistroEstudiantes:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def get_student_details(self):
        for student in self.students:
            print(
                f"Nombre: {student.get_name()}, Edad: {student.get_age()}, Calificación: {student.get_grade()}")


# Crear registros
registro = RegistroEstudiantes()

# Agregar estudiantes al registro
student1 = Student("Juan", 15, "8vo grado")
student2 = Student("María", 16, "9no grado")
student3 = Student("Pedro", 14, "7mo grado")

registro.add_student(student1)
registro.add_student(student2)
registro.add_student(student3)

# Obtener detalles de estudiantes
registro.get_student_details()

# Eliminar un estudiante y volver a imprimir los detalles
registro.remove_student(student1)

registro.get_student_details()
