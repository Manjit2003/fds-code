#include <iostream>
#include <string.h>
using namespace std;
class publication
{
private:
    int price;
    string names;

public:
    void getbookdetails()
    {
        cout << "enter the name of book: ";
        cin >> names;
        cout << endl;
        cout << "enter the price: ";
        cin >> price;
        cout << endl;
    }
    void gettapedetails()
    {
        cout << "enter the name: ";
        cin >> names;
        cout << endl;
        cout << "enter the price: ";
        cin >> price;
        cout << endl;
    }
    void printbooksdata()
    {
        cout << "the name of the book is: " << names << endl;
        cout << "the price of the book is: " << price << endl;
    }
    void printtapedetails()
    {
        cout << "the name of the tape is: " << names << endl;
        cout << "the price of the tape is: " << price << endl;
    }
};
class book : public publication
{
private:
    int pages;

public:
    void getpages()
    {
        cout << "enter the number of pages: ";
        cin >> pages;
    }
    void printbpages()
    {
        cout << "the number of pages of books are: " << pages << endl;
        cout << endl;
    }
};
class tapes : public publication
{
private:
    int time;

public:
    void gettime()
    {
        cout << "enter the time of playing: ";
        cin >> time;
    }
    void printtime()
    {
        cout << "the time of tape is: " << time << endl;
    }
};
int main()
{
    book b[10];
    tapes t[10];
    int bn;
    cout << "enter the number of books: ";
    cin >> bn;
    for (int i = 1; i <= bn; i++)
    {
        cout << ".... ENTER BOOK DETAILS NO." << i << "....." << endl;
        b[i].getbookdetails();
        b[i].getpages();
        cout << endl;
    }
    for (int i = 1; i <= bn; i++)
    {
        cout << "....BOOK DETAILS NO." << i << "....." << endl;
        b[i].printbooksdata();
        b[i].printbpages();
    }
    int tn;
    cout << "enter the number of tapes: ";
    cin >> tn;
    for (int i = 1; i <= tn; i++)
    {
        cout << ".... ENTER TAPE DETAILS NO." << i << "....." << endl;
        t[i].gettapedetails();
        t[i].gettime();
        cout << endl;
    }
    for (int i = 1; i <= tn; i++)
    {
        cout << "....TAPE DEATILS NO." << i << "....." << endl;
        t[i].printtapedetails();
        t[i].printtime();
        cout << endl;
    }
}
