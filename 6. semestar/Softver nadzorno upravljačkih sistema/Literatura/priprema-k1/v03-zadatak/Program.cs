namespace PoolProgram;
    public class Program
    {
        public static void Main()
        {
            Pool pool = new Pool();
            PoolMonitoring monitor = new PoolMonitoring(pool);
            monitor.LevelChangeSimulation(0.3, 0.2);
        }
    }

