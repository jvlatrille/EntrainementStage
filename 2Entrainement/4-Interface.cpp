#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Piece {
    string nom;
    int quantite;
    string reference;
};

void afficherStock(const vector<Piece>& stock) {
    for (size_t i = 0; i < stock.size(); ++i)
        cout << "Ref: " << stock[i].reference << ", Piece: " << stock[i].nom << ", Qte: " << stock[i].quantite << endl;
}

int main() {
    vector<Piece> stock;
    int choix;
    string ref;

    while (true) {
        cout << "\n1. Ajouter piece\n2. Supprimer piece\n3. Afficher stock\n4. Quitter\nChoix : ";
        cin >> choix;

        if (choix == 1) {
            Piece p;
            cout << "Nom piece : "; cin >> p.nom;
            cout << "Quantite : "; cin >> p.quantite;
            cout << "Reference : "; cin >> p.reference;
            stock.push_back(p);
        }
        else if (choix == 2) {
            cout << "Reference a supprimer : "; cin >> ref;
            bool found = false;
            for (auto it = stock.begin(); it != stock.end(); ++it) {
                if (it->reference == ref) {
                    stock.erase(it);
                    found = true;
                    cout << "Piece supprimee.\n";
                    break;
                }
            }
            if (!found) cout << "Piece non trouvee.\n";
        }
        else if (choix == 3) afficherStock(stock);
        else if (choix == 4) break;
        else cout << "Choix invalide.\n";
    }
    return 0;
}
