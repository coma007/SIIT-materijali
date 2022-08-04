using System;
using System.Collections.Generic;

namespace Methods.Params
{
    /// <summary>
    /// ID izazova je dostupan na web prikazu.
    /// 1. Primeni odgovarajuće strategije za redukciju liste parametra za metode ispod.
    /// </summary>
    class CourseService
    {
        private readonly List<Student> _students = new List<Student>();
        public void RegisterStudent(Student student)
        {
            foreach (var s in _students)
            {
                if(s.Index.Equals(student.Index)) throw new InvalidOperationException("Student exists.");
            }
            _students.Add(student);
        }
        
    }

    internal class Course
    {
        public string Status { get; set; }
        public int ESPB {get; set;}

        
        public bool IsActive()
        {
            return Status.Equals("enrolled") || Status.Equals("current");
        }
    }

    internal class Student
    {
        public Student(string name, string surname, DateTime dateOfBirth, string index)
        {
            Name = name;
            Surname = surname;
            DateOfBirth = dateOfBirth;
            Index = index;
            ActiveESPB = 0;
        }
        
        public List<Course> Courses { get; set; }
        public string Name { get; }
        public string Surname { get; }
        public DateTime DateOfBirth { get; }
        public string Index { get; }
        public int ActiveESPB { get; set; }

        public void Enroll(Course course)
        {
            int numberOfActiveCourses = 0;
            foreach (var c in Courses)
            {
                if (c.IsActive()) numberOfActiveCourses++;
            }

            if (numberOfActiveCourses < 7 && ActiveESPB < 80)
            {
                Courses.Add(course);
                ActiveESPB += course.ESPB;
            }
        }

    }
}
