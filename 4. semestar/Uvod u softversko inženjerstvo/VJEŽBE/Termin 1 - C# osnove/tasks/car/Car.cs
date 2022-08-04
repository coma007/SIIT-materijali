using Newtonsoft.Json;

namespace Car
{
    [Serializable]
    public class Car
    {
        
        [JsonProperty("$id")]
        public string Id { get; set; }
        public string Model { get; set; }
        public string Mark { get; set; }
        public string Color { get; set; }
        public int Year { get; set; }
        public CarFuel Fuel { get; set; }
        public CarEngine Engine { get; set; }

        public Car()
        {
        }

        public Car(string model, string brand, string color, int year, string engineName, double engineVolume, double enginePower, bool diesel=true) {
            Model = model;
            Mark = brand;
            Color = color;
            Year = year;
            Engine = new CarEngine(engineName, engineVolume, enginePower);
            Fuel = CarFuel.Gasoline;
            if (diesel) {
                Fuel = CarFuel.Diesel;
            }
        }

        public override string ToString() {
            string fuel;
            if (Fuel == 0) {
                fuel = "Gasoline";
            }
            else {
                fuel = "Diesel";
            }
            string engine = Engine.ToString();
            return "Car { Model = " + Model + "; Brand = " + Mark + "; Color = " + Color + "; Year = " + Year + "; Fuel = " + fuel + "; Engine = " + engine + " }";
        }

    }
}