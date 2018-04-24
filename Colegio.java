
public class Colegio extends edificio{
	private int numeroAulas;
	private boolean pabellon;
	public Colegio(String direccion, int codigoPostal, int altura,
			boolean calefaccionCentral) {
		super(direccion, codigoPostal, altura, calefaccionCentral);
		this.numeroAulas=numeroAulas;
		
		// TODO Auto-generated constructor stub
	}
	public int getCapacidadColegio(){
		int capacidadColegio;
		capacidadColegio=numeroAulas*30;
		return(capacidadColegio);
		
	}


}
