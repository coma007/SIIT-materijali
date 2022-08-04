using System;
using System.Collections.Generic;

namespace Classes.Structural
{
     /// <summary>
    /// ID izazova je dostupan na web prikazu.
    /// 1. Izračunaj strukturalnu koheziju CourseService klase.
    /// 2. Primeni odgovarajuće refaktorisanje kako bi završio sa visoko-kohezivnim klasama.
    /// </summary>
    class CourseService
    {
        private readonly List<Course> _courses = new List<Course>();
        private readonly List<Student> _students = new List<Student>();
        public void RegisterStudent(Student newStudent)
        {
            foreach (var student in _students)
            {
                if (student.Index.Equals(newStudent.Index)) throw new InvalidOperationException("Student exists.");
            }
            _students.Add(newStudent);
        }

        public void EnrollStudent(int studentId, Course course)
        {
            Student student = FindStudent(studentId);
            student.Enroll(course);
        }

        public Student FindStudent(int studentId)
        {
            foreach (var student in _students)
            {
                if (student.Id == studentId) {
                    return student;
                }
            }
            throw new ArgumentException("Student not found.");
        }

        public Course FindCourse(int courseId)
        {
            foreach (var course in _courses)
            {
                if (course.Id == courseId) {
                    return course;
                }
            }
            throw new ArgumentException("Course not found.");
        }

        public void RegisterCourse(Course newCourse)
        {
            foreach (var course in _courses)
            {
                if (course.Name.Equals(newCourse.Name)) throw new InvalidOperationException("Course with provided name exists.");
            }
            _courses.Add(newCourse);
        }
    }

    internal class Course
    {
        public int Id { get;set; }
        public string Name { get;set; }
        public int CourseESPB { get; set; }
    }

    internal class CourseEnrollment {
        public Course Course { get;set; }
        public string Status { get; set; }
        public bool IsActive()
        {
            return Status.Equals("enrolled") || Status.Equals("current");
        }
    }

    internal class Student
    {
        public int Id { get;set; }
        public List<CourseEnrollment> Enrollments { get; set; }
        public string Name { get; }
        public string Surname { get; }
        public DateTime DateOfBirth { get; }
        public string Index { get; }
        public int ActiveESPB { get; set; }

        public void Enroll(Course newCourse)
        {
            int numberOfActiveCourses = 0;
            foreach (var c in Enrollments)
            {
                if (c.IsActive()) numberOfActiveCourses++;
            }

            if (numberOfActiveCourses < 7 && ActiveESPB < 80)
            {
                Enrollments.Add(new CourseEnrollment { Course = newCourse, Status = "enrolled" });
                ActiveESPB += newCourse.CourseESPB;
            }
        }
    }
}