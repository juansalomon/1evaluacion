//Lectura hasta el final
#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(){
    string linea;
    string nombre;
    int salir;
    int repetir=0;
    
    cout<<"Dime la ruta del fichero: ";
     getline(cin,nombre);
      ifstream fichero(nombre.c_str());
    do{
               
      if(fichero.fail()==1){
         cout<<"ERROR.No existe la ruta"<<endl;
         getline(cin,nombre);
         ifstream fichero(nombre.c_str());
         cin>>salir;
         repetir=1;
         }else{
            repetir=0;
    }
    }while(repetir==1);
    while (fichero.eof()==0){
    getline(fichero,linea);
    cout<<linea;
    }
    fichero.close();
    cin>>salir;
    return 0;
}
