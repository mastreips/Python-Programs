#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
   int b=0,i,j,n,m,k,l,p=0;
char a[500][500];
scanf("%d%d",&n,&m);
for(i=0;i<n;i++)
{
    scanf("%500s",a[i]);
}
for(i=0;i<n-1;i++)
{
    for(j=i+1;j<n;j++)
    {
    l=0;
        for(k=0;k<m;k++)
        {
            if((a[i][k]==49)||(a[j][k]==49))
            {
                l++;
            }
        }
        if(b<l)
        {
            p=1;
            b=l;
        }
        else if(b==l)
        {
            p++;
        }
    }
}
printf("%d\n%d",b,p);
    return 0;
}
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
   int b=0,i,j,n,m,k,l,p=0;
char a[500][500];
scanf("%d%d",&n,&m);
for(i=0;i<n;i++)
{
    scanf("%500s",a[i]);
}
for(i=0;i<n-1;i++)
{
    for(j=i+1;j<n;j++)
    {
    l=0;
        for(k=0;k<m;k++)
        {
            if((a[i][k]==49)||(a[j][k]==49))
            {
                l++;
            }
        }
        if(b<l)
        {
            p=1;
            b=l;
        }
        else if(b==l)
        {
            p++;
        }
    }
}
printf("%d\n%d",b,p);
    return 0;
}
