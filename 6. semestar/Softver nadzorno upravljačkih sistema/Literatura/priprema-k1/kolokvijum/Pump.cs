namespace kolokvijum;

public class Pump
{
    public double InRate { get; set; }
    public bool IsOn { get; set; }

    public Pump()
    {
        InRate = 0.2;
        IsOn = false;
    }
}

