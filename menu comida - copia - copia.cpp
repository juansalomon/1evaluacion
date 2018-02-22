#include<iostream>
using namespace std;
int main(){
     struct menu{
      string primero;
      string segundo;
      string postre;
   };
   int cont;
   int salir;
   menu menuComedor[5];
   for(cont=0;cont<5;cont++){
     cout<<"comedor"<<cont<<endl;                        
     cout<<"Que hay de primero ";
     cin>>menuComedor[cont].primero;
     cout<<"Que hay de segundo ";
     cin>>menuComedor[cont].segundo;
     cout<<"Que hay de postre: ";
     cin>>menuComedor[cont].postre; 
   }
   cout<<"EL MENU ES: "<<endl;
   for(cont=0;cont<5;cont++){
      cout<<"De primero hay "<<menuComedor[cont].primero<<" , de segundo "<<menuComedor[cont].segundo<<" y de postre "<<menuComedor[cont].postre<<endl;                           
   }
    cout<<"Toca cualquier tecla para acabar";
    cin>>salir;
     
 }
