namespace kolokvijum;

public class ChlorineMachine 
{
    public double InChlorineRate { get; set; }
    public bool IsOn { get; set; }

    public ChlorineMachine()
    {
        InChlorineRate = 0.3;
        IsOn = false;
    }
}
