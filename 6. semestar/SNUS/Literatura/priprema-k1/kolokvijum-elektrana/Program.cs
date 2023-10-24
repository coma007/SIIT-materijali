// See https://aka.ms/new-console-template for more information

namespace kolokvijum_elektrana;
public class Program
{
    public static void Main()
    {
        Reaction r = new Reaction();
        r.HeatingRate = 20;
        r.TimeSpan = 1;
        
        WaterCooling wc = new WaterCooling();
        
        
        NuclearReactor nr = new NuclearReactor(r, wc);
        
        NuclearReactorMonitoring nrm = new NuclearReactorMonitoring(nr);
        nrm.NuclearReactor.WaterCooling.Pump = new Pump();
        nrm.NuclearReactor.WaterCooling.Pump.InRate = 5;
        nrm.NuclearReactor.WaterCooling.Pump.IsOn = false;
        for (int i = 0; i < nrm.NuclearReactor.WaterCooling.Valves.Count; i++)
        {
            nrm.NuclearReactor.WaterCooling.Valves.ElementAt(i).IsOpen = false;
        }
        nrm.StartReactionSimulation(100);
        nrm.StartRandomisation(10);
    }
}