using System.Diagnostics.Contracts;

namespace PoolProgram;

public class Pool
{
    public double Level { get; set; }
    public double MinLevel { get; set; }
    public double MaxLevel { get; set; }
    public PoolStatus Status { get; set; }

    public Pool()
    {
        this.Level = 2.5;
        this.Status = PoolStatus.HALF_FULL;
        this.MinLevel = 0;
        this.MaxLevel = 5;
    }

}

public enum PoolStatus
{
    FULL, HALF_FULL, EMPTY
}