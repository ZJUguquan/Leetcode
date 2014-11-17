#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
const int nMax=250005;
const int mMax=2000005;
char text[mMax],pat[nMax];
int lent,lenp,nnext[nMax];

void get_nnext(){
    int i,j=-1;
    nnext[0]=-1;
    for(i=1;i<=lenp;i++){     
        while(j>-1&&pat[j+1]!=pat[i])j=nnext[j];
        if(pat[j+1]==pat[i])j++;
        nnext[i]=j;
    }
}

int KMP(){
    int ans=0,i=0,j=-1;
    get_nnext();
    for(i=0;i<lent;i++){
        while(j!=-1&&pat[j+1]!=text[i]){
            j=nnext[j];
        }
        if(pat[j+1]==text[i])j=j+1;
        if(j==lenp-1){
      //      cout<<"fuck "<<i<<endl;
            if(i==lenp-1)return 0;
            return lent-i-1;//ans++;  
        }
    }
    return -1;
}

int main(){
    int t;
    while(scanf("%d",&lenp)!=EOF){
        scanf("%s%s",text,pat);
        for(int i=0;i<lenp;i++){
            text[i+lenp]=text[i];
        }
        lent=2*lenp;
        text[lent]='\0';
        int ans=KMP();
        if(ans!=-1){
            printf("%d\n",ans);
        }
        else{
            printf("-1\n");
        }
    }
    return 0;
}
