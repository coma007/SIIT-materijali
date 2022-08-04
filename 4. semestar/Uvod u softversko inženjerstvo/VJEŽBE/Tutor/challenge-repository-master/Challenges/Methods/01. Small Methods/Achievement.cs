using System;
using System.Collections.Generic;
using System.IO;

namespace Methods.Small
{
    /// <summary>
    /// ID izazova je dostupan na web prikazu.
    /// 1. Ekstrahuj više metoda iz AwardAchievement metode.
    /// 2. Za svaku novu metodu formuliši značajno ime.
    /// </summary>
    class AchievementService
    {
        private readonly string _achievementStorageLocation = "../Storage/Achievements/";

        public void AwardAchievement(int userId, int newAchievementId)
        {
            //Load data for new achievement
            Achievement newAchievement = null;
            GetAchievements(0);

            if (newAchievement == null) throw new Exception("New achievement does not exist in the registry.");

            //Load unlocked achievements for user
            List<Achievement> unlockedAchievements = GetUserAchivements(userId, newAchievement);

            //Check if user has prerequisite achievements unlocked
            CheckIfUnlocked(newAchievement, unlockedAchievements);

            //Save new achievement to storage
            SaveAchievement(newAchievement, userId);
        }

        public List<Achievement> GetUserAchivements(int userId, Achievement newAchievement)
        {
            string[] achievements = File.ReadAllLines(_achievementStorageLocation + userId + ".csv");
            List<Achievement> unlockedAchievements = new List<Achievement>();
            foreach (var storedAchievement in achievements)
            {
                string[] achievementElements = storedAchievement.Split(":");
                Achievement a = new Achievement();
                a.Name = achievementElements[0];
                a.ImagePath = achievementElements[1];
                //Check if newAchievement is already unlocked.
                if (a.Name.Equals(newAchievement.Name) && a.ImagePath.Equals(newAchievement.ImagePath))
                {
                    throw new InvalidOperationException("Achievement " + newAchievement.Name + " is already unlocked!");
                }
                unlockedAchievements.Add(a);
            }
            return unlockedAchievements;
        }

        public void SaveAchievement(Achievement newAchievement, int userId)
        {
            string newAchievementStorageFormat = newAchievement.Name + ":" + newAchievement.ImagePath + "\n";
            File.AppendAllText(_achievementStorageLocation + userId + ".csv", newAchievementStorageFormat);
        }

        public void CheckIfUnlocked(Achievement newAchievement, List<Achievement> unlockedAchievements)
        {
            foreach (var prerequisiteAchievement in newAchievement.PrerequisiteAchievementNames)
            {
                bool foundAchievement = false;
                foreach (var a in unlockedAchievements)
                {
                    if (a.Name.Equals(prerequisiteAchievement))
                    {
                        foundAchievement = true;
                        break;
                    }
                }
                if (!foundAchievement) throw new InvalidOperationException("Prerequisite achievement " + prerequisiteAchievement + " not completed.");
            }
        }

        public Achievement GetAchievements(int newAchievementId)
        {

            Achievement newAchievement = new Achievement();
            string[] allAchievements = File.ReadAllLines(_achievementStorageLocation + "allAchievements.csv");
            foreach (var achievement in allAchievements)
            {
                string[] achievementElements = achievement.Split(":");
                if (!achievementElements[0].Equals(newAchievementId.ToString())) continue;
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

    class Achievement
    {
        public string Name { get; set; }
        public string ImagePath { get; set; }
        public List<string> PrerequisiteAchievementNames { get; set; }
    }

}
