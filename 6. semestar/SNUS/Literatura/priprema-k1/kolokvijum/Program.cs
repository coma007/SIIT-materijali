// See https://aka.ms/new-console-template for more information

namespace kolokvijum;
public class Program
{
    public static void Main()
    {
        Pool pool = new Pool();
        Pump pump = new Pump();
        ChlorineMachine chlorineMachine = new ChlorineMachine();

        PoolSystemMonitoring monitoring = new PoolSystemMonitoring(pump,  chlorineMachine, pool);
        Valve v1 = new Valve();
        v1.IsOpen = false;
        v1.OutRate = 0.5;
        Valve v2 = new Valve();
        v2.IsOpen = true;
        v2.OutRate = 0.3;
        monitoring.AddValve(v1);
        monitoring.AddValve(v2);
        
        monitoring.StartUsingPool(1);
        monitoring.poolUsingThread.Join();
        monitoring.StartEmptyingPool();
        monitoring.poolEmptyingThread.Join();
        for (int i = 0; i < monitoring.valves.Count; i++)
        {
            monitoring.CloseValve(i);
        }
        monitoring.StartFillingPool();
        monitoring.StartAddingChlorine();
        monitoring.poolFillingThread.Join();
        monitoring.chlorineAddingThread.Join();
        
        monitoring.Report();
        // nisam zakljucavala WaterLevel i ChlorineLevel jer se sa oba
        // rukuje u razlicitim nitima i nema dijeljenja resursa izmedju
        // te dvije niti, ista nit i upisuje i cita resurs
        
        // posto program radi konkurentno, tesko da ce bas u istom
        // trenutku da se dese dvije promjene - zato report nema rezultata;
        // ako bi se npr. promijenio uslov za "trenutak", npr. da u istom
        // sekundu promijene vrijednost i nivo vode i nivo hlora,
        // onda ima rezultata
        // mozete pogledati ovaj kod u metodi
        // Report() i otkomentarisati odgovarajuci komentar.
    }
}