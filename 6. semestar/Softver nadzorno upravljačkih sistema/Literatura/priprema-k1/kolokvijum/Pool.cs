namespace kolokvijum;

public class Pool
{
    public double WaterLevel { get; set; }
    public double MinWaterLevel { get; set; }
    public double MaxWaterLevel { get; set; }
    public double ChlorineLevel { get; set; }
    public double MinChlorineLevel { get; set; }
    public double MaxChlorineLevel { get; set; }

    public Pool()
    {
        WaterLevel = 2;
        MinWaterLevel = 0;
        MaxWaterLevel = 2.5;
        ChlorineLevel = 5;
        MinChlorineLevel = 2;
        MaxChlorineLevel = 8;
    }
}
