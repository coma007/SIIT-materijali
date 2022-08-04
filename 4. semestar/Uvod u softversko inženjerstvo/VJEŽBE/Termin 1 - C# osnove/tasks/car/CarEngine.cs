using Newtonsoft.Json;

namespace Car
{
    [Serializable]
    public class CarEngine
    {
        [JsonProperty("$id")]
        public string Id { get; set; }
        public string Name { get; set; }
        public double CubicCapacity { get; set; }
        public double Power { get; set; }

        [JsonProperty("$ref")]
        public string Ref { get; set; }

        public CarEngine(string engineName, double engineVolume, double enginePower) {
            Name = engineName;
            CubicCapacity = engineVolume;
            Power = enginePower;
            
        }
        
        public override string ToString() {
            return "Engine {Name = " + Name + "; CubicCapacity = " + CubicCapacity + "; Power = " + Power + "}";
        }
    }
}