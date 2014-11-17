
#include<iostream>
using namespace std;
#include<queue>
int main()
{std::priority_queue<int>pr;
int n,i,a;
int v[250000/2 + 3];
cin>>n;
for(; i< n/2+1; ++i) cin >> v[i];
make_heap(v,v+n/2 + 1); 
for(;i<n; ++i){
	cin >> v[n/2+1];
	push_heap(v,v+n/2 +2);
	pop_heap(v,v+n/2+2);
}

		 
	 
for(i=1;i<=n/2+1;i++)
    {cin>>a;
    pr.push(a);
    }
 i=n/2+2;
    while(i<=n){
        cin>>a;
        pr.push(a);i++;
pr.pop();
}
if(n%2!=0)
	cout<<pr.top()<<".0"<<endl;
else
	{a=pr.top();
		pr.pop();
		if(a%2+pr.top()%2==2)
			cout<<a/2+pr.top()/2+1<<".0"<<endl;
    	else
        if(a%2+pr.top()%2==0)
        	cout<<a/2+pr.top()/2<<".0"<<endl;
        else
            if(a%2+pr.top()%2==1)
            	cout<<(a/2+pr.top()/2)<<".5"<<endl;
}
return 0;
}