from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.student_with_courses = Student(
            "s with courses",
            {"SoftUni": ['note']}
        )
        self.student = Student("d without courses")

    def test_correct_initializing(self):
        self.assertEqual("d without courses", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual(
            {"SoftUni": ['note']},
            self.student_with_courses.courses
        )

    def test_enroll_add_notes_to_ex_course(self):
        result = self.student_with_courses.enroll("SoftUni", ["note 2"])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(
            {"SoftUni": ['note', 'note 2']},
            self.student_with_courses.courses
        )

    def test_enroll_add_notes_to_non_ex_course(self):
        result = self.student.enroll("SoftUni", ["note 2"])

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"SoftUni": ['note 2']}, self.student.courses)

    def test_enroll_add_notes_to_non_ex_course_with_Y(self):
        result = self.student.enroll("SoftUni", ["note 2"], "Y")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"SoftUni": ['note 2']}, self.student.courses)

    def test_enroll_without_notes(self):
        result = self.student.enroll("SoftUni", ["note 2"], "no")

        self.assertEqual(0, len(self.student.courses["SoftUni"]))
        self.assertEqual("Course has been added.", result)

    def test_add_notes_to_non_ex_course_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.add_notes("Soft", "note")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_to_ex_course(self):
        result = self.student_with_courses.add_notes("SoftUni", "note 1")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual({"SoftUni": ['note', 'note 1']}, self.student_with_courses.courses)

    def test_leave_non_ex_course_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.leave_course("Soft")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_ex_course(self):
        result = self.student_with_courses.leave_course("SoftUni")

        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student_with_courses.courses)


if __name__ == "__main__":
    main()
