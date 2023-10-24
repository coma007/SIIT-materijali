namespace kolokvijum_elektrana;

public class NuclearReactor
{
    
    public Reaction Reaction { get; set; }
    public WaterCooling WaterCooling { get; set; }
    public double CurrentTemperature { get; set; }
    public double MinTemperature { get; set; }
    public double MaxTemperature { get; set; }

    public NuclearReactor(Reaction reaction, WaterCooling waterCooling)
    {
        Reaction = reaction;
        WaterCooling = waterCooling;
        this.MaxTemperature = 300;
        this.MinTemperature = 50;
        this.CurrentTemperature = (300 - 50) / 2;
    }

    public void RandomiseHeatRate()
    {
        Random r = new Random();
        this.Reaction.HeatingRate = r.Next(-30, 30);
    }
}