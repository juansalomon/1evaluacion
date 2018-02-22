#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(){
     struct persona{
             string nombre;
             int edad;
             char colorpelo;
     };
     persona amigo1;
     persona amigo2;
     persona amigo3;
     
     cout<<"Como se llama tu amigo: ";
     cin>>amigo1.nombre;
     cout<<"Cuantos años tiene: ";
     cin>>amigo1.edad;
     cout<<"De que color tiene pelo: ";
     cin>>amigo1.colorpelo;
}
