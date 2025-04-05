#include <iostream>
#include <vector>
using namespace std;

struct Parametres {
    float puissanceLaser;
    float vitesseDeplacement;
    float debitPoudre;
};

void afficher(const vector<Parametres>& params) {
    for (size_t i = 0; i < params.size(); i++) {
        cout << "Parametre " << i + 1 << " : Laser = " << params[i].puissanceLaser
             << " W, Vitesse = " << params[i].vitesseDeplacement << " mm/s, Debit poudre = "
             << params[i].debitPoudre << " g/min" << endl;
    }
}

int main() {
    vector<Parametres> listeParams;
    int choix;

    while (true) {
        cout << "\nMenu:\n1.Ajouter\n2.Modifier\n3.Afficher\n4.Quitter\nChoix : ";
        cin >> choix;

        if (choix == 1) {
            Parametres p;
            cout << "Puissance Laser (W) : "; cin >> p.puissanceLaser;
            cout << "Vitesse deplacement (mm/s) : "; cin >> p.vitesseDeplacement;
            cout << "Debit poudre (g/min) : "; cin >> p.debitPoudre;
            listeParams.push_back(p);
        }
        else if (choix == 2) {
            size_t id;
            cout << "Entrer le numero du parametre a modifier : ";
            cin >> id;
            if (id > 0 && id <= listeParams.size()) {
                cout << "Nouvelle Puissance Laser : "; cin >> listeParams[id-1].puissanceLaser;
                cout << "Nouvelle Vitesse deplacement : "; cin >> listeParams[id-1].vitesseDeplacement;
                cout << "Nouveau Debit poudre : "; cin >> listeParams[id-1].debitPoudre;
            } else {
                cout << "Numero invalide !" << endl;
            }
        }
        else if (choix == 3) {
            afficher(listeParams);
        }
        else if (choix == 4) {
            break;
        }
        else {
            cout << "Choix invalide !" << endl;
        }
    }
    return 0;
}
