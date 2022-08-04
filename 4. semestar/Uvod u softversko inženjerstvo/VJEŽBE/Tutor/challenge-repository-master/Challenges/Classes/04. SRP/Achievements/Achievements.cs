using System;
using System.Collections.Generic;
using System.IO;

namespace Classes.SRP.Achievements
{
    /// <summary>
    /// ID izazova je dostupan na web prikazu.
    /// 1. Refaktoriši kod tako da redukuješ broj odgovornosti koje AchievementService ispunjava.
    /// 2. Primeni "extract class", "extract method" ili "move method" refaktorisanja tokom ovog procesa.
    /// </summary>
    public class AchievementService
    {
        private readonly string _achievementStorageLocation = "C:/MyGame/Storage/Achievements/";
        public void AwardAchievement(int userId, string newAchivemenetName)
        {
            Achievement newAchievement = LoadAchievement(newAchivemenetName);
            if (newAchievement == null) throw new Exception("New achievement does not exist in the registry.");
            
            List<Achievement> unlockedAchievements = LoadUserAchievements(userId, newAchievement);

            CheckIfPrerequisitesUnlocked(newAchievement, unlockedAchievements);

            SaveAchievement(userId, newAchievement);
        }

        private void SaveAchievement(int userId, Achievement newAchievement)
        {
            //Save new achievement to storage
            string newAchievementStorageFormat = newAchievement.Name + ":" + newAchievement.ImagePath + "\n";
            File.AppendAllText(_achievementStorageLocation + userId + ".csv", newAchievementStorageFormat);
        }

        private static void CheckIfPrerequisitesUnlocked(Achievement newAchievement, List<Achievement> unlockedAchievements)
        {
            //Check if user has prerequisite achievements unlocked
            foreach (var prerequisiteAchievement in newAchievement.PrerequisiteAchievementNames)
            {
                if(!AchievementIsUnlocked(prerequisiteAchievement, unlockedAchievements)) {
                    throw new InvalidOperationException("Prerequisite achievement " + prerequisiteAchievement + " not completed.");
                }
            }
        }

        private static bool AchievementIsUnlocked(string name, List<Achievement> unlockedAchievements)
        {
            foreach (var a in unlockedAchievements)
            {
                if (a.Name.Equals(name)) return true;
            }
            return false;
        }

        private List<Achievement> LoadUserAchievements(int userId, Achievement newAchievement)
        {
            //Load unlocked achievements for user
            List<Achievement> unlockedAchievements = new List<Achievement>();
            string[] achievements = File.ReadAllLines(_achievementStorageLocation + userId + ".csv");
            foreach (var storedAchievement in achievements)
            {
                string[] achievementElements = storedAchievement.Split(":");
                Achievement a = new Achievement();
                a.Name = achievementElements[0];
                a.ImagePath = achievementElements[1];
                //Check if newAchievement is already unlocked.
                if (a.Name.Equals(newAchievement.Name))
                {
                    throw new InvalidOperationException("Achievement " + newAchievement.Name + " is already unlocked!");
                }
                unlockedAchievements.Add(a);
            }

            return unlockedAchievements;
        }

        private Achievement LoadAchievement(string name)
        {
            //Load data for new achievement
            Achievement newAchievement = null;
            string[] allAchievements = File.ReadAllLines(_achievementStorageLocation + "allAchievements.csv");
            foreach (var achievement in allAchievements)
            {
                string[] achievementElements = achievement.Split(":");
                if (!achievementElements[0].Equals(name)) continue;
                newAchievement = new Achievement();
                newAchievement.Name = achievementElements[0];
                newAchievement.ImagePath = achievementElements[1];
                newAchievement.PrerequisiteAchievementNames = new List<string>();
                //Add ids of prerequisite achievements
                for (int i = 2; i < achievementElements.Length; i++)
                {
                    newAchievement.PrerequisiteAchievementNames.Add(achievementElements[i]);
                }
            }

            return newAchievement;
        }
    }

    public class Achievement
    {
        public string Name { get; set; }
        public string ImagePath { get; set; }
        public List<string> PrerequisiteAchievementNames { get; set; }
    }
}
