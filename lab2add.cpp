#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

int bins(int a[],int n, int k)
{
	int f=0,m=0,l=n-1;
	while(f<l)
	{
		m=((f+l)/2);
		if(a[m]==k)
			return m;
		else if(a[m]>=a[f])
		{
			if(a[m]>k&&a[f]<=k)
				l=m-1;
			else
				f=m+1;
					
		}
		else
		{
			if(a[m]<k&&k<=a[l])
				f=m+1;
			else
				l=m-1;
		}
		if(a[f]==k)
			return f;
		
	}
	return -1;
}
int main()
{
	int n;
	cout<<"enter n: ";
	cin>>n;
	int a[20];
	cout<<"enter elements: ";
	for(int i=0;i<n;i++)
		cin>>a[i];
	int k;
	cout<<"enter k: ";
	cin>>k;
	cout<<bins(a,n,k);
}