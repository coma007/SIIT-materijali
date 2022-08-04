using System;
using System.Collections.Generic;
using System.Linq;

namespace Naming.Noise
{
    /// <summary>
    /// ID izazova je dostupan na web prikazu.
    /// ** Nemoj da modifikuješ naziv namespace-a, Run klase i zaglavlja metoda ove klase. **
    /// 1. Odredi sve nazive koji sadrže generične ili beznačajne reči.
    /// 2. Ukloni ove reči ili ih promeni u nešto značajnije.
    /// 3. Potvrdi da nema sintaksnih grešaka i da je Run klasa ispratila bilo kakva preimenovanja klasa i metoda koje koristi.
    /// </summary>
    public class Doctor
    {
        public int DoctorId { get; }
        public ISet<Specialization> Specializations { get; } = new HashSet<Specialization>();

        public bool HasSpecializations(List<Specialization> specializations)
        {
            foreach (var specialization in specializations)
            {
                if (!Specializations.Contains(specialization)) return false;
            }

            return true;
        }

        public void AssignSpecialization(Specialization specialization)
        {
            if (Specializations.Contains(specialization)) throw new DoctorAlreadyHasSpecializationException("Doctor: " + DoctorId.ToString() + "Spec: " + specialization);
            Specializations.Add(specialization);
        }

    }

    public class DoctorAlreadyHasSpecializationException : Exception
    {
        public DoctorAlreadyHasSpecializationException(string message) : base(message)
        {
        }
    }

    public class Specialization
    {
        private readonly string _name;

        public Specialization(string name)
        {
            _name = name;
        }

        public override bool Equals(object obj)
        {
            if (!(obj is Specialization other)) return false;
            return other._name.Equals(_name);
        }

        public override int GetHashCode()
        {
            return _name.GetHashCode();
        }
    }

    #region Run
    public class Run
    {
        private readonly Doctor _doctor;

        public Run()
        {
            _doctor = new Doctor();
            _doctor.AssignSpecialization(new Specialization("Test 1"));
            _doctor.AssignSpecialization(new Specialization("Test 2"));
            _doctor.AssignSpecialization(new Specialization("Test 3"));
        }

        public void AddSpec()
        {
            _doctor.AssignSpecialization(new Specialization("Test 1"));
        }

        public List<Specialization> GetSpec()
        {
            return _doctor.Specializations.ToList();
        }

        public bool HasSpec(List<Specialization> all)
        {
            return _doctor.HasSpecializations(all);
        }
    }
    #endregion
}
