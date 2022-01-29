package types.invoice;

import java.util.List;

public class Invoice {
	
	public String invoice;
	public String date;
	public Person billTo;
	public Person shipTo;
	public List<Product> product;
	public double tax;
	public double total;
	public String comments;
	public String getInvoice() {
		return invoice;
	}
	public void setInvoice(String invoice) {
		this.invoice = invoice;
	}
	public String getDate() {
		return date;
	}
	public void setDate(String date) {
		this.date = date;
	}
	public Person getBillTo() {
		return billTo;
	}
	public void setBillTo(Person billTo) {
		this.billTo = billTo;
	}
	public Person getShipTo() {
		return shipTo;
	}
	public void setShipTo(Person shipTo) {
		this.shipTo = shipTo;
	}
	public List<Product> getProduct() {
		return product;
	}
	public void setProduct(List<Product> product) {
		this.product = product;
	}
	public double getTax() {
		return tax;
	}
	public void setTax(double tax) {
		this.tax = tax;
	}
	public double getTotal() {
		return total;
	}
	public void setTotal(double total) {
		this.total = total;
	}
	public String getComments() {
		return comments;
	}
	public void setComments(String comments) {
		this.comments = comments;
	}
	@Override
	public String toString() {
		return "Invoice [invoice=" + invoice + ", date=" + date + ", billTo=" + billTo + ", shipTo=" + shipTo
				+ ", product=" + product + ", tax=" + tax + ", total=" + total + ", comments=" + comments + "]";
	}
	
	
	

}
