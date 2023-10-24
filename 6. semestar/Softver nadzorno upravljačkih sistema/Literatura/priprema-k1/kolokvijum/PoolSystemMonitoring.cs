namespace kolokvijum;

delegate void PoolWaterLevelHandler(double waterLevel);
delegate void PoolChlorineLevelHandler(double chlorineLevel);

public class PoolSystemMonitoring
{
    private static object valveLocker = new object();
    public Pump pump { get; set; }
    public ChlorineMachine chlorineMachine { get; set; }
    public Pool pool { get; set; }
    public SystemStatesWrapper wrapper { get; set; }
    public List<Valve> valves { get; set; }

    private event PoolWaterLevelHandler poolWaterLevelChanged;
    private event PoolChlorineLevelHandler poolChlorineLevelChanged;
    
    public Thread poolUsingThread { get; set; }
    public Thread poolEmptyingThread { get; set; }
    public Thread poolFillingThread { get; set; }
    public Thread chlorineAddingThread { get; set; }

    public PoolSystemMonitoring(Pump pump, ChlorineMachine chlorineMachine, Pool pool)
    {
        this.pump = pump;
        this.chlorineMachine = chlorineMachine;
        this.pool = pool;

        this.wrapper = new SystemStatesWrapper();
        this.wrapper.waterStates = new List<SystemWaterState>();
        this.wrapper.chlorineStates = new List<SystemChlorineState>();
        this.valves = new List<Valve>();

        poolWaterLevelChanged += OnPoolWaterLevelChanged;
        poolChlorineLevelChanged += OnPoolChlorineLevelChanged;

        poolUsingThread = new Thread(UsingPool);
        poolEmptyingThread = new Thread(EmptyPool);
        poolFillingThread = new Thread(FillingPool);
        chlorineAddingThread = new Thread(AddingChorine);
    }

    public void AddValve(Valve valve)
    {
        this.valves.Add(valve);
    }

    public void OpenValve(int index)
    {
        lock (valveLocker)
        {
            this.valves.ElementAt(index).IsOpen = true;
        }
    }

    public void CloseValve(int index)
    {
        lock (valveLocker)
        {
            this.valves.ElementAt(index).IsOpen = false;
        }

        }

    public void TurnOnPump()
    {
        this.pump.IsOn = true;
    }

    public void TurnOffPump()
    {
        this.pump.IsOn = false;
    }

    public void StartUsingPool(double dirtRate)
    {
        poolUsingThread.Start(dirtRate);
    }

    public void UsingPool(object dirtRate)
    {
        while (pool.ChlorineLevel > pool.MinChlorineLevel)
        {
            pool.ChlorineLevel -= (double)dirtRate;
            if (pool.ChlorineLevel < pool.MinChlorineLevel)
            {
                pool.ChlorineLevel = pool.MinChlorineLevel;
            }

            poolChlorineLevelChanged(pool.ChlorineLevel);
            Thread.Sleep(1 * 1000);
        }
    }
    
    public void StartEmptyingPool()
    {
        poolEmptyingThread.Start();
    }

    public void EmptyPool()
    {
        double totalOutRate = 0;
        foreach (var valve in valves)
        {
            if (valve.IsOpen)
            {
                totalOutRate += valve.OutRate;
            }
        }
        while (pool.WaterLevel > pool.MinWaterLevel)
        {
            pool.WaterLevel -= totalOutRate;
            if (pool.WaterLevel < pool.MinWaterLevel)
            {
                pool.WaterLevel = pool.MinWaterLevel;
            }

            poolWaterLevelChanged(pool.WaterLevel);
            Thread.Sleep(1 * 1000);
        }

    }
    
    public void StartFillingPool()
    {
        poolFillingThread.Start();
    }
    
    public void FillingPool()
    {
        double totalInRate = pump.InRate;
        foreach (var valve in valves)
        {
            if (valve.IsOpen)
            {
                totalInRate -= valve.OutRate;
            }
        }
        while (pool.WaterLevel < pool.MaxWaterLevel)
        {
            pool.WaterLevel += totalInRate;
            if (pool.WaterLevel > pool.MaxWaterLevel)
            {
                pool.WaterLevel = pool.MaxWaterLevel;
            }
            poolWaterLevelChanged(pool.WaterLevel);
            Thread.Sleep(1 * 1000);
        }

        for (int i = 0; i < valves.Count; i++)
        {
            CloseValve(i);
        }
    }
    public void StartAddingChlorine()
    {
        chlorineAddingThread.Start();
    }
    
    public void AddingChorine()
    {
        while (pool.ChlorineLevel < pool.MaxChlorineLevel)
        {
            pool.ChlorineLevel += chlorineMachine.InChlorineRate;
            if (pool.ChlorineLevel > pool.MaxChlorineLevel)
            {
                pool.ChlorineLevel = pool.MaxChlorineLevel;
            }

            poolChlorineLevelChanged(pool.ChlorineLevel);
            Thread.Sleep(1 * 1000);
        }

        for (int i = 0; i < valves.Count; i++)
        {
            valves.ElementAt(i).IsOpen = false;
        }
    }

    private void OnPoolWaterLevelChanged(double level)
    {
        Console.WriteLine($"Water level: {level}");
        SystemWaterState state = new SystemWaterState();
        state.PoolWaterLevel = level;
        state.TimeStamp = DateTime.Now;
        this.wrapper.waterStates.Add(state);
    }
    
    private void OnPoolChlorineLevelChanged(double chlorineLevel)
    {
        Console.WriteLine($"Chlorine level: {chlorineLevel}");
        SystemChlorineState state = new SystemChlorineState();
        state.PoolChlorineLevel = chlorineLevel;
        state.TimeStamp = DateTime.Now;
        this.wrapper.chlorineStates.Add(state);
    }

    public void Report()
    {
        Console.WriteLine("------Report------");
        // var query = from waterState in wrapper.waterStates
        //     join chlorineState in wrapper.chlorineStates on waterState.TimeStamp equals chlorineState.TimeStamp
        //     select new { waterState.TimeStamp, waterState.PoolWaterLevel, chlorineState.PoolChlorineLevel };
        //
        var query = from waterState in wrapper.waterStates
            join chlorineState in wrapper.chlorineStates on waterState.TimeStamp.Second equals chlorineState.TimeStamp.Second
            select new { waterState.TimeStamp, waterState.PoolWaterLevel, chlorineState.PoolChlorineLevel };

        if (query.Count() == 0)
        {
            Console.WriteLine("No matching results.");
        }

        foreach (var result in query)
        {
            Console.WriteLine($"TimeStamp: {result.TimeStamp.ToLongTimeString()}, Water level: {Math.Round(result.PoolWaterLevel, 2)}, Chlorine level: {Math.Round(result.PoolChlorineLevel, 2)}");
        } 
    }

}