
public class edificio {
	private String direccion;
	private int codigoPostal;
	private int altura;
	private boolean calefaccionCentral;
	public edificio(String direccion, int codigoPostal, int altura,
			boolean calefaccionCentral) {
		this.direccion = direccion;
		this.codigoPostal = codigoPostal;
		this.altura = altura;
		this.calefaccionCentral = calefaccionCentral;
	}
	public String getDireccion() {
		return direccion;
	}
	public void setDireccion(String direccion) {
		this.direccion = direccion;
	}
	public int getCodigoPostal() {
		return codigoPostal;
	}
	public void setCodigoPostal(int codigoPostal) {
		this.codigoPostal = codigoPostal;
	}
	public int getAltura() {
		return altura;
	}
	public void setAltura(int altura) {
		this.altura = altura;
	}
	public boolean isCalefaccionCentral() {
		return calefaccionCentral;
	}
	public void setCalefaccionCentral(boolean calefaccionCentral) {
		this.calefaccionCentral = calefaccionCentral;
	}
	

}
