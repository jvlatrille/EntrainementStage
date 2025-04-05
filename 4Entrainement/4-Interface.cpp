#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Station {
    string nom;
    string gps;
    int altitude;
};

void afficherStations(const vector<Station>& stations) {
    for (const auto& s : stations)
        cout << s.nom << " | GPS: " << s.gps << " | Altitude: " << s.altitude << "m\n";
}

int main() {
    vector<Station> stations;
    int choix;
    string recherche;

    while (true) {
        cout << "\n1. Ajouter\n2. Modifier\n3. Afficher\n4. Rechercher\n5. Quitter\nChoix : ";
        cin >> choix;

        if (choix == 1) {
            Station s;
            cout << "Nom: "; cin >> s.nom;
            cout << "GPS: "; cin >> s.gps;
            cout << "Altitude: "; cin >> s.altitude;
            stations.push_back(s);
        }
        else if (choix == 2) {
            cout << "Nom station à modifier: "; cin >> recherche;
            for (auto& s : stations)
                if (s.nom == recherche) {
                    cout << "Nouveau GPS: "; cin >> s.gps;
                    cout << "Nouvelle altitude: "; cin >> s.altitude;
                }
        }
        else if (choix == 3) afficherStations(stations);
        else if (choix == 4) {
            cout << "Rechercher station (nom): "; cin >> recherche;
            auto it = find_if(stations.begin(), stations.end(), [&](Station s){ return s.nom == recherche; });
            if (it != stations.end())
                cout << it->nom << " | GPS: " << it->gps << " | Altitude: " << it->altitude << "m\n";
            else
                cout << "Station introuvable.\n";
        }
        else if (choix == 5) break;
        else cout << "Choix invalide\n";
    }
    return 0;
}
