#include <iostream>
using namespace std;
class complex
{
public:
    int r, i;
    complex() // default constructor
    {
        r = 0;
        i = 0;
    }
    complex operator+(complex o1)
    {
        complex temp;
        temp.r = r + o1.r;
        temp.i = i + o1.i;
        return temp;
    }
    complex operator-(complex o1)
    {
        complex temp;
        temp.r = r - o1.r;
        temp.i = i - o1.i;
        return temp;
    }
    complex operator*(complex o1)
    {
        complex temp;
        temp.r = (r * o1.r) - (i * o1.i);
        temp.i = (r * o1.i) + (i * o1.r);
        return temp;
    }
    friend istream &operator>>(istream &, complex &);
    friend ostream &operator<<(ostream &, complex &);
};
istream &operator>>(istream &in, complex &o)
{
    cout << "enter real part: ";
    in >> o.r;
    cout << "enter imaginary part: ";
    in >> o.i;
    return in;
}
ostream &operator<<(ostream &out, complex &o)
{
    out << o.r << "+" << o.i << "i";
}
int main()
{
    complex c1, c2;
    cout << "default constructor value is: ";
    cout << c1 << endl;
    cout << "Enter details of first complex number\n\n";
    cin >> c1;
    cout << "\n\n";
    cout << "Enter details of second complex number\n\n";
    cin >> c2;
    cout << "\n\n";
    cout << "The first complex number is: " << c1;
    cout << "\n\n";
    cout << "The second complex number is: " << c2;
    cout << "\n\n";
    complex c3;
    c3 = c1 + c2;
    cout << "\n\n";
    cout << "The addition of complex number is: " << c3;
    complex c4;
    c4 = c1 - c2;
    cout << "\n\n";
    cout << "The subtraction of complex number is: " << c4;
    complex c5;
    c5 = c1 * c2;
    cout << "\n\n";
    cout << "The multiplication of complex number is: " << c5;
    cout << endl;
    cout << "\n\n";
    cout << "\n\n";
    return 0;
}
