namespace kolokvijum_elektrana;

public class SystemState
{
    public DateTime TimeStamp { get; set; }
    public double CoreTemperature { get; set; }
    public Pump pump { get; set; }
    public double heatingRate { get; set; }
    public List<Valve> ValvesSnapshot { get; set; }

    public SystemState(DateTime timeStamp, double coreTemperature, Pump pump, double heatingRate, List<Valve> valvesSnapshot)
    {
        TimeStamp = timeStamp;
        CoreTemperature = coreTemperature;
        this.pump = pump;
        this.heatingRate = heatingRate;
        ValvesSnapshot = valvesSnapshot;
    }
}