namespace PoolProgram;

delegate void PoolLevelHandler(double level);
delegate void PoolStatusHandler(string status);

public class PoolMonitoring
{
    private Pool Pool { get; set; }

    private event PoolLevelHandler poolLevelChanged;
    private event PoolStatusHandler poolStatusChanged;

    public PoolMonitoring(Pool pool)
    {
        this.Pool = pool;
        this.poolLevelChanged += OnPoolLevelChanged;
        this.poolLevelChanged += OnPoolLevelChangedLogger;
        this.poolStatusChanged += OnPoolStatusChanged;
    }

    public void LevelChangeSimulation(double inRate, double outRate)
    {
        while (this.Pool.Level > this.Pool.MinLevel)
        {
            this.Pool.Level -= outRate;
            this.Pool.Level = Math.Max(this.Pool.Level, this.Pool.MinLevel);
            Thread.Sleep(1000);
            poolLevelChanged(this.Pool.Level);
            if (this.Pool.Level.Equals(this.Pool.MinLevel))
            {
                poolStatusChanged(PoolStatus.EMPTY.ToString());
            }
        }

        while (this.Pool.Level < this.Pool.MaxLevel)
        {    
            this.Pool.Level += inRate;
            this.Pool.Level = Math.Min(this.Pool.Level, this.Pool.MaxLevel);
            Thread.Sleep(1500);
            poolLevelChanged(this.Pool.Level);
            if (this.Pool.Level.Equals(this.Pool.MaxLevel))
            {
                poolStatusChanged(PoolStatus.FULL.ToString());
            }
        }
    }

    private void OnPoolLevelChanged(double level)
    {
        Console.WriteLine($"Current level of water in pool: {Math.Round(level, 2)}\n" +
                          $"Time: {DateTime.Now.ToLongTimeString()}\n" +
                          $"----------------------------------------");
    }

    private void OnPoolStatusChanged(string status)
    {
        Console.WriteLine($"Current status of pool: {status}\n" +
                          $"Time: {DateTime.Now.ToLongTimeString()}\n" +
                          $"----------------------------------------");
    }

    private void OnPoolLevelChangedLogger(double level)
    {
        
        using (StreamWriter writer = File.AppendText("../../../poolLog.txt"))
        {
            writer.WriteLine($"level of water: {Math.Round(level, 2)} meters - " +
                             $"time: {DateTime.Now.ToLongTimeString()}");
        }
    }
}