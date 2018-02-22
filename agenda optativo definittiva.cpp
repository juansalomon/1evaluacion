 #include<iostream>
 using namespace std;
 int salir;
 int main(){
   struct agenda{
      string nombre;
      string apellido1;
      char apellido2;
      int telefono;
      int edad;
      int curso;
   };
   
   
   int cont;
  agenda alumno[100];
   for(cont=0;cont<100;cont++){
     cout<<"DATOS ALUMNOS"<<cont;                        
     cout<<"Como se llama tu amigo: ";
      cin>>alumno[cont].nombre;
      cout<<"Cual es el primer apellido: ";
     cin>>alumno[cont].apellido1;
      cout<<"cual es la primera letra de tu segundo apellido: ";
     cin>>alumno[cont].apellido2;
     cout<<"cual es tu telefono movil: ";
     cin>>alumno[cont].telefono;
     cout<<"Cuántos años tiene: ";
     cin>>alumno[cont].edad;
     cout<<"De que color tiene el peluco: ";
     cin>>alumno[cont].curso; 
   }
 cout<<"LOS ALUMNOS SON: "<<endl;
   for(cont=0;cont<100;cont++){
      cout<<"El alumno "<<alumno[cont].nombre<<","<<alumno[cont].apellido1<<","<<alumno[cont].apellido2<<"tiene "<<alumno[cont].edad<<" años, cursa "<<alumno[cont].curso<<"curso y su numero de telefono es"<<alumno[cont].telefono;                           
   }
   {istream fichero("misalumnos.txt");
   fichero<<agenda;
}
    cout<<"Toca cualquier tecla para acabar";
    cin>>salir;
       
 }
