#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ofstream out("ITEMS.txt");
    char pname[30];
    char feature[30];
    int n, price, warranty;
    cout << "Type number of products to entered: ";
    cin >> n;
    cout << endl;
    for (int i = 0; i < n; i++)
    {
        cout << "enter your product name: ";
        cin >> pname;
        cout << endl;
        cout << "enter your product feature: ";
        cin >> feature;
        cout << endl;
        cout << "enter your product price: ";
        cin >> price;
        cout << endl;
        cout << "enter your product warranty: ";
        cin >> warranty;
        cout << endl;
        out << pname << " "
            << " " << feature << " " << price << " " << warranty;
    }
    out.close();
    ifstream in("ITEMS.txt");
    for (int j = 0; j < n; j++)
    {
        in >> pname;
        in >> feature;
        in >> price;
        in >> warranty;
        cout << "product name= ";
        cout << pname << endl;
        cout << "product feature= ";
        cout << feature << endl;
        cout << "product price= ";
        cout << price << endl;
        cout << "product warranty years= ";
        cout << warranty << endl;
    }
    in.close();
    return 0;
}
