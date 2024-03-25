// Solución del problema de las n reinas con backtracking.

#include <iostream>
#include <vector>
#include <ctime>

using namespace std;

/**
 * Comprueba que el número colocado en la columna c (que representa una fila) sea válido.
 * Con ser válido se refiere a que:
 * 1) no hay otra reina en esa misma fila y
 * 2) no interfiere en las diagonales con otra reina.
 * @param c : número de columna a verificar.
 * @param estado : estado actual del tablero.
 */
bool posicion_valida(int c, vector<int> & estado){
    int fila_actual = estado.at(c);
    //Para comprobar que no se interfiere con otras reinas por fila, basta con comprobar que
    //ese número no se repite en las casillas anteriores.
    for(int i=0; i<c; i++){
        if(estado.at(i) == fila_actual){
            return false;
        }
    }
    //Luego se comprueba que no interfiera con las diagonales.
    int delta = 1;
    for(int i=c-1; i>=0; i--){
        if(fila_actual+delta == estado.at(i) ||
           fila_actual-delta == estado.at(i)){
            return false;
        }
        delta++;
    }
    return true;
}

/**
 * @brief Se realiza el backtracking en el tablero. Lo que hace es "quitar" las
 * reinas que ya había colocado hasta encontrar una reina que no haya llegado
 * a la última fila.
 * @param estado del tablero
 * @param pos posición a partir de la cual se hace backtracking
 */
void backtrack(vector<int> & estado, int & pos){
    int n = estado.size()-1;
    while(pos>0 && estado.at(pos) >= n){
        estado[pos] = -1;
        pos--;
    }
}

//Imprime un vector de enteros.
void imprime_vector(vector<int> & v1){
    cout << "[";
    for(int i=0; i<v1.size()-1; i++){
        cout << v1.at(i) << ", ";
    }
    cout << v1.at(v1.size()-1) << "]" << endl;
}

//Imprime un tablero con las posiciones de las reinas
void imprime_tablero(vector<int> & v1){
    int n = v1.size();
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(v1.at(j) == i){
                cout << "👑";
            }else{
                if((i+j)%2 == 0){
                    cout << "⬜";
                }else{
                    cout << "⬛";
                }
            }
        }
        cout << endl;
    }
}

//Método principal.
int main(){
    cout << "Indique el número de reinas a colocar en el tablero." << endl;
    int n_reinas = 0;
    cin >> n_reinas;
    cout << "Indique el tiempo límite de ejecución, en segundos." << endl;
    long tl = 0;
    cin >> tl;
    vector<int> estado(n_reinas); //guardará la fila actual de cada reina.
    vector<int> mejor_estado(n_reinas); //se guardará el mejor estado encontrado.
    int max_reinas = -1; //guarda el máximo número de reinas colocadas.
    for(int i=0; i<n_reinas; i++){
        estado[i] = -1;
        mejor_estado[i] = -1;
    }
    int index_act = 0; //la columna donde se va a colocar la siguiente reina.
    long ti = time(NULL);
    //en este ciclo se intentan colocar las n reinas.
    while(estado[0] < n_reinas-1 && index_act < n_reinas && time(NULL)-ti < tl){
        estado[index_act]++;
        if(posicion_valida(index_act, estado)){
            //si la posición es válida, se intenta colocar la siguiente reina.
            index_act++;
            //se actualiza el mejor estado encontrado si es necesario.
            if(index_act > max_reinas){
                max_reinas = index_act;
                mejor_estado = estado;
            }
        }else{
            //si la posición no es válida y la reina en index_act
            //ya llegó a la última fila se hace backtracking.
            if(estado.at(index_act) == n_reinas-1){
                backtrack(estado, index_act);
            }
        }
    }
    cout << "Mejor tablero econtrado:" << endl;
    //se imprime el mejor estado obtenido (en forma de vector)
    imprime_vector(mejor_estado);
    //se imprime el tablero del mejor estado.
    imprime_tablero(mejor_estado);
}
