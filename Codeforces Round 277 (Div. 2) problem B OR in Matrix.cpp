#include <bits/stdc++.h>
 
using namespace std;
 
int main()
{
    int n,m;
    cin>>m>>n;
    int b[m][n];
    for(int i=0; i<m; i++)
        for(int j=0; j<n; j++)
            cin>>b[i][j];
    /*
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++)
            cout<<b[i][j]<<" ";
        cout<<endl;
    }*/
    int a[m][n];
    for(int i=0; i<m; i++)
        for(int j=0; j<n; j++)
            a[i][j]=1;
    
    
    for(int i=0; i<m; i++)
        for(int j=0; j<n; j++)
            if(b[i][j] == 0){
                for(int k=0; k<n; k++)
                    a[i][k]=0;
                for(int k=0; k<m; k++)
                    a[k][j]=0; 
            }
    bool TEST=true;
    for(int i=0; i<m; i++)
        for(int j=0; j<n; j++)
            if(b[i][j]==1){
                bool test=false;
                int k=0;
                while(test==false && k<m){
                    if(a[k][j]==1){
                        test = true;
                        break;
                    }
                    k++;
                }
                int l=0;
                while(test==false && l<n){
                    if(a[i][l]==1){
                        test = true;
                        break;
                    }
                    l++;
                }
                if(test==false)
                    TEST=false;
            }
    
    
    
    if(TEST==false)cout<<"NO";
    else{
        cout<<"YES"<<endl;
    for(int i=0; i<m; i++){
        for(int j=0; j<(n-1); j++)
            cout<<a[i][j]<<" ";
        cout<<a[i][n-1];
        cout<<endl;
    }
    }
 
    return 0;
}
