#include<iostream>
using namespace std;
template<class T>
void ssort(T a[],int n)
{
for (int i=0;i<n-1;i++)
{
int imin=i;
for(int j=i+1;j<n;j++)
{
if(a[j]<a[imin])
{
imin=j;
}
}
if (imin!=i)
{
swap(a[imin],a[i]);
}
}
}
int main()
{
int a[100],n1;
float b[100],n2;
cout<<"enter the number of integer elements to be entered: ";
cin>>n1;
for(int i=0;i<n1;i++){
cout<<"enter the element at "<<i<<" index ";
cin>>a[i];
}
ssort(a,n1);
cout<<"array is sorted: ";
cout<<"[";
for(int i=0;i<n1;i++)
{
cout<<"\t"<<a[i];
}
cout<<" ]";
cout<<"\n\n";
cout<<"enter the number of float elements to be entered: ";
cin>>n2;
for(int i=0;i<n2;i++){
cout<<"enter the element at "<<i<<"index ";
cin>>b[i];
}
ssort(b,n2);
cout<<"array is sorted:";
cout<<"[";
for(int i=0;i<n2;i++)
{
cout<<"\t"<<b[i];
}
cout<<"]";
}
