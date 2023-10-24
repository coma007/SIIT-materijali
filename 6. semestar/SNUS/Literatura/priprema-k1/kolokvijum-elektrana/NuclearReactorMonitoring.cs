using System.ComponentModel.Design.Serialization;

namespace kolokvijum_elektrana;

public delegate void CoreTemperatureHandler(double temperature);
public delegate void CriticalTemperatureHandler();

public class NuclearReactorMonitoring
{
    public NuclearReactor NuclearReactor { get; set; }
    private event CoreTemperatureHandler coreTemperatureChanged;
    private event CriticalTemperatureHandler criticalValueOccured;
    public List<SystemState> SystemStates { get; set; }
    public Thread reactionThread { get; set; }
    public Thread waterCoolingThread { get; set; }
    public Thread randomiseThread { get; set; }
    private static readonly object locker = new object();
    private bool reactionDone = false;
    

    public NuclearReactorMonitoring(NuclearReactor reactor)
    {
        this.NuclearReactor = reactor;
        coreTemperatureChanged += OnCoreTemperatureChanged;
        criticalValueOccured += OnCriticalTemperatureOccured;
        this.SystemStates = new List<SystemState>();

        NuclearReactor.WaterCooling.Valves = new List<Valve>();
        Valve v1 = new Valve();
        Valve v2 = new Valve();
        Valve v3 = new Valve();
        NuclearReactor.WaterCooling.Valves.Add(v1);
        NuclearReactor.WaterCooling.Valves.Add(v2);
        NuclearReactor.WaterCooling.Valves.Add(v3);

        Pump p = new Pump();
        NuclearReactor.WaterCooling.Pump = p;
    }

    public void OpenCloseValves()
    {
        lock (locker)
        {
            Random r = new Random();
            int valve = r.Next(0, 3);
            NuclearReactor.WaterCooling.Valves.ElementAt(valve).IsOpen = false;
            NuclearReactor.WaterCooling.Valves.ElementAt((valve + 1) % 3 ).IsOpen = true;
            NuclearReactor.WaterCooling.Valves.ElementAt((valve + 2) % 3).IsOpen = true;
        }
    }

    public void StopReactionAZ5()
    {
        lock (locker)
        {
            NuclearReactor.Reaction.HeatingRate = 0;
            for (int i = 0; i < NuclearReactor.WaterCooling.Valves.Count; i++)
            {
                NuclearReactor.WaterCooling.Valves.ElementAt(i).IsOpen = true;
            }
            NuclearReactor.WaterCooling.Pump.IsOn = true;
        }
        }

    public void StartReactionSimulation(int seconds)
    {
        this.reactionThread = new Thread(() =>
        {
            while (seconds >= 0)
            {
                Thread.Sleep(1000);
                seconds--;
                ReactionSimulation();
                if (this.NuclearReactor.CurrentTemperature >= this.NuclearReactor.MaxTemperature ||
                    this.NuclearReactor.CurrentTemperature <= this.NuclearReactor.MinTemperature)
                {
                    break;
                }
            }
            lock (locker)
            {
                reactionDone = true;
            }
        });
        this.reactionThread.Start();
    }

    public void ReactionSimulation()
    {
        double inRateSum = 0;
        foreach (Valve valve in NuclearReactor.WaterCooling.Valves)
        {
            if (valve.IsOpen)
            {
                inRateSum += valve.InRate;
            }
        }

        lock (locker)
        {
        NuclearReactor.CurrentTemperature +=
        NuclearReactor.Reaction.HeatingRate / NuclearReactor.Reaction.TimeSpan - inRateSum;
        }
        coreTemperatureChanged(NuclearReactor.CurrentTemperature);
        
        if (NuclearReactor.CurrentTemperature >= NuclearReactor.MaxTemperature)
        {
            lock (locker)
            {
                NuclearReactor.CurrentTemperature = NuclearReactor.MaxTemperature;
            }
            criticalValueOccured();
            StopReactionAZ5();
            StartWaterCoolingSimulation();
        }
        if (NuclearReactor.CurrentTemperature <= NuclearReactor.MinTemperature)
        {
            lock (locker)
            {
                NuclearReactor.CurrentTemperature = NuclearReactor.MinTemperature;
            }
            criticalValueOccured();
        }

    }

    public void StartWaterCoolingSimulation()
    {
        this.waterCoolingThread = new Thread(WaterCoolingSimulation);
        this.waterCoolingThread.Start();
    }

    public void WaterCoolingSimulation()
    {
        while (NuclearReactor.CurrentTemperature >= NuclearReactor.MinTemperature)
        {
            Thread.Sleep(2000);
            OpenCloseValves();
            
        }

    }

    public void StartRandomisation(int seconds)
    {
        randomiseThread= new Thread(() =>
        {
            while (!reactionDone)
            {
                this.NuclearReactor.RandomiseHeatRate();
                Thread.Sleep(seconds*1000);
            }
            
        });
        randomiseThread.Start();
        
    }

    private void OnCoreTemperatureChanged(double temperature)
    {
        Console.WriteLine($"Current temperature: {temperature}");
        SystemState state = new SystemState(DateTime.Now, this.NuclearReactor.CurrentTemperature, this.NuclearReactor.WaterCooling.Pump, this.NuclearReactor.Reaction.HeatingRate, this.NuclearReactor.WaterCooling.Valves);
        this.SystemStates.Add(state);
    }
    
    private void OnCriticalTemperatureOccured()
    {
        Console.WriteLine($"panic: Current temperature: {this.NuclearReactor.CurrentTemperature}");
    }
}