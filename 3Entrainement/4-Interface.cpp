#include <iostream>
#include <vector>
using namespace std;

struct ReleveMeteo {
    string date;
    float temperature;
    string condition;
};

void afficher(const vector<ReleveMeteo>& releves) {
    for (auto& r : releves)
        cout << r.date << " | Temp: " << r.temperature << "°C | Condition: " << r.condition << endl;
}

int main() {
    vector<ReleveMeteo> releves;
    int choix;
    string dateRecherche;

    while (true) {
        cout << "\n1.Ajouter\n2.Supprimer\n3.Afficher\n4.Rechercher par date\n5.Quitter\nChoix: ";
        cin >> choix;

        if (choix == 1) {
            ReleveMeteo r;
            cout << "Date (YYYY-MM-DD) : "; cin >> r.date;
            cout << "Température : "; cin >> r.temperature;
            cout << "Condition météo : "; cin >> r.condition;
            releves.push_back(r);
        }
        else if (choix == 2) {
            cout << "Date du relevé à supprimer : "; cin >> dateRecherche;
            bool trouve = false;
            for (auto it = releves.begin(); it != releves.end(); ++it) {
                if (it->date == dateRecherche) {
                    releves.erase(it);
                    cout << "Supprimé.\n";
                    trouve = true;
                    break;
                }
            }
            if (!trouve) cout << "Non trouvé.\n";
        }
        else if (choix == 3) afficher(releves);
        else if (choix == 4) {
            cout << "Date à rechercher : "; cin >> dateRecherche;
            bool trouve = false;
            for (auto& r : releves) {
                if (r.date == dateRecherche) {
                    cout << r.date << " | Temp: " << r.temperature << "°C | Condition: " << r.condition << endl;
                    trouve = true;
                }
            }
            if (!trouve) cout << "Aucun relevé trouvé.\n";
        }
        else if (choix == 5) break;
        else cout << "Choix invalide.\n";
    }
    return 0;
}
