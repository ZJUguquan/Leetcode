import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class 1685 {

    public static void main(String[] args) throws IOException
    {
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        char[] a = new char[20005];
        char[] b = new char[20005];
        int n = 0;
        while(true)
        {
            int x = sc.read();
            if (x==13)
                break;
            n++;
            a[n] = (char)x;
        }
        int left = 1;
        int right = n;
        ArrayList<Integer> listR = new ArrayList<Integer>();
        ArrayList<Integer> listO = new ArrayList<Integer>();
        int orta = (left+right)/2;
        for (int i = 1; i <=n; i++)
        {
            System.out.println("L="+left+" R="+right+" O="+orta);
            if (left<=right)b[orta] = a[i];
            if (left<right){
                listR.add(right);
                right = orta-1;
                listO.add(orta);
                orta = (left+right)/2;
            }
            else{
                System.out.println(listO);
                left = listO.get(listO.size()-1)+1;
                listO.remove(listO.size()-1);
                right = listR.get(listR.size()-1);
                listR.remove(listR.size()-1);
                orta = (left+right)/2;
            }
        }
        for (int i = 1; i <=n; i++)
        {
            System.out.print(b[i]);
        }
    }

}
