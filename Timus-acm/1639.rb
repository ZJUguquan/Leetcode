# 1639 

n,m = gets.chomp!.split(" ").map {|x| x.to_i}
puts  (n*m-1) % 2 == 1 ? "[:=[first]" : "[second]=:]"


=begin
int main(){
    int x, y;
    cin >> x >> y;
    if ((x*y-1)%2==1)
        cout << "[:=[first]";
    else cout << "[second]=:]";
    return 0;
}
=end