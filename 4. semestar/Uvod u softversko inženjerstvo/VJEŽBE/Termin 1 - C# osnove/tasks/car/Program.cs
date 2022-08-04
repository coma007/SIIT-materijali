using System.Text.Json.Nodes;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace Car
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Car c = new Car("A6", "Audi", "black", 2018, "TeslaEngines", 1.2, 1000);
            Console.WriteLine(c);
            Car c1 = new Car("Golf 5", "VW", "Grey", 2012, "VWEngine", 1.6, 1220);
            Console.WriteLine(c1);

            var cars = new List<Car>();
            cars.Add(c1);

            string crs= System.IO.File.ReadAllText("../../../files/cars.json");
            Console.WriteLine(crs);
            cars = JsonConvert.DeserializeObject<List<Car>>(File.ReadAllText("../../../files/cars.json"),
                new JsonSerializerSettings
                {
                    PreserveReferencesHandling = PreserveReferencesHandling.Objects
                });
            Console.WriteLine(cars.Count);
        foreach (var car in cars) {
                Console.WriteLine(car);
            }
        }
        
    }
}