package types.point;

import com.opencsv.bean.CsvBindByPosition;

public class Point implements Comparable<Point>{
	
	@CsvBindByPosition(position = 0)
	public double x;
	@CsvBindByPosition(position = 1)
	public double y;
	@CsvBindByPosition(position = 2)
	public double z;
	@CsvBindByPosition(position = 3, required = false)
	public double r;
	
	public double getX() {
		return x;
	}
	public void setX(double x) {
		this.x = x;
	}
	public double getY() {
		return y;
	}
	public void setY(double y) {
		this.y = y;
	}
	public double getZ() {
		return z;
	}
	public void setZ(double z) {
		this.z = z;
	}
	public double getR() {
		return r;
	}
	public void setR(double r) {
		this.r = r;
	}
	
	@Override
	public String toString() {
		return "Point [x=" + x + ", y=" + y + ", z=" + z + ", r=" + r + "]";
	}
	
	public double countDistance() {
		r = Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2) + Math.pow(z, 2));
		return r;
	}
	
	
	@Override
	public int compareTo(Point point) {
		if (r < point.getR()) {
			return -1;
		}
		if (r > point.getR()) {
			return 1;
		}
		return 0;	
	
	
	}
}
