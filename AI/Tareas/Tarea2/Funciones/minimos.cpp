
// Encontrando mínimos con ascensión de colinas.

#include <iostream>
#include <vector>
#include <list>
#include <ctime>
#include <cmath>
#include <cstdlib>

using namespace std;

// 𝑓(x,y)=x^2 + y^2
double funcion1(double x, double y){
    return (x*x + y*y);
}

// 𝑔(x,y) =(2)(418.9829) − x∗sin⁡(√|x|)  − y∗sin⁡(√|y|))
double funcion2(double x, double y){
    double a = 2*418.9829;
    double b = -x*sin(sqrt(abs(x)));
    double c = -y*sin(sqrt(abs(y)));
    return a+b+c;
    //2*418.9829-x*sin(sqrt(abs(x)))-y*sin(sqrt(abs(y)))
}

/**
 * @brief Genera un número real aleatorio entre 0 y 1.
 * @return número aleatorio entre 0 y 1.
 */
double randb01(){
    double rm1 = (static_cast <double> (rand())) / (static_cast <double> (RAND_MAX));
    return rm1;
}

/**
 * @brief Genera los sucesores de un punto
 * @param punto punto actual
 * @param siguientes los siguientes puntos hacia donde se va a mover el agente.
 * @param delta el incremento o decremento que se hará en el punto actual.
 * @param idFunc número de la función
 */
void expande(vector<double> & punto, vector<vector<double>> & siguientes, double delta, int idFunc){
    double x = punto[0];
    double y = punto[1];
    double dx;
    double dy;

    for(int i=0; i<4; i++){
        switch(i){
            case 0: dx = delta;
                    dy = 0.0;
            break;
            case 1: dx = -delta;
                    dy = 0.0;
            break;
            case 2: dx = 0.0;
                    dy = delta;
            break;
            case 3: dx = 0.0;
                    dy = -delta;
        }

        siguientes[i][0] = x+dx;
        siguientes[i][1] = y+dy;
        if(idFunc == 1){
            siguientes[i][2] = funcion1(x+dx, y+dy);
        }else{
            siguientes[i][2] = funcion2(x+dx, y+dy);
        }
    }
}

/**
 * @brief Realiza ascensión de colinas para tratar de encontrar al mínimo
 * en alguna función.
 * @param idFunc id de la función (sólo puede ser 1 o 2).
 * @return vector de puntos (x, y, z) tal que la z es la mínima encontrada por el algoritmo.
 */
vector<double> hillclimber(int idFunc){
    srand(time(0));
    vector<double> actual(3); //Vector con los 3 puntos (x, y, f(x,y))
    double liminf, limsup, delta;
    if(idFunc == 1){
        liminf = -5.0; //límite inferior
        limsup = 5.0; //límite superior
        delta = 0.0001; //incremento
    }else{
        liminf = -500.0;
        limsup = 500.0;
        delta = 0.01;
    }
    vector<vector<double>> sucesores(4); //El vector actual siempre tendrá 4 sucesores.
    for(auto & row : sucesores){
        row.resize(3);
    }
    double x_actual = (limsup-liminf)*randb01() + liminf;
    double y_actual = (limsup-liminf)*randb01() + liminf;
    double fxy_actual = 0;
    if(idFunc == 1){
        fxy_actual = funcion1(x_actual, y_actual);
    }else{
        fxy_actual = funcion2(x_actual, y_actual);
    }
    actual[0] = x_actual;
    actual[1] = y_actual;
    actual[2] = fxy_actual;
    bool sin_sucesores = false; //verdadero si y sólo si ya no tiene sucesores factibles.
    list<int> candidatos; //lista de posibles sucesores.
    //A partir de aquí comienza el ascenso.
    while(!sin_sucesores){
        expande(actual, sucesores, delta, idFunc);
        candidatos.clear();
        for(int i=0; i<sucesores.size(); i++){
            //Se guardan en la lista los candidatos que sean factibles.
            //Los factibles son los que sus 'x' y 'y' caen en el rango [liminf, limsup]
            //y tienen una f(x,y) menor estricta que el punto actual.
            if(liminf <= sucesores[i][0] && sucesores[i][0] <= limsup
            && liminf <= sucesores[i][1] && sucesores[i][1] <= limsup
            && sucesores[i][2] < actual[2]){
                candidatos.push_back(i);
            }
        }
        if(!candidatos.empty()){
            double minimo = actual[2];
            int indiceMinimo = -1;
            for(int cand : candidatos){
                if(sucesores[cand][2] < minimo){
                    minimo = sucesores[cand][2];
                    indiceMinimo = cand;
                }
            }
            actual = sucesores[indiceMinimo]; //mueve al agente al mejor estado
        }else{
            sin_sucesores = true;
        }
    }
    return actual;
}

//Función principal.
int main(){
    cout << "Escriba un número para elegir una de las siguientes funciones:" << endl;
    cout << "1) f(x,y) = x²+y²" << endl;
    cout << "2) g(x,y) = (2)(418.9829) - x*sin(√|x|) - y*sin(√|y|))" << endl;
    int idFunc = 0;
    cin >> idFunc;
    if(idFunc != 1 && idFunc != 2){
        cout << "Ese número no es válido" << endl;
        return 0;
    }
    cout << "Ingrese el límite de tiempo en segundos" << endl;
    long limite_tiempo;
    cin >> limite_tiempo;
    vector<double> mp; //Mejor punto
    vector<double> cp; //Candidato a mejor punto
    mp = hillclimber(idFunc);
    long tiempo_inicial = time(NULL);
    while(time(NULL)-tiempo_inicial < limite_tiempo){
        cp = hillclimber(idFunc);
        if(cp[2] < mp[2]){
            mp = cp;
        }
    }
    cout << "Mejor punto encontrado:" << endl;
    cout << "x: " << mp[0] << ", y: " << mp[1] << ", f(x,y): " << mp[2] << endl;
}
