import java.sql.Array;
import java.util.ArrayList;
import java.util.Scanner;

public class Pascal_Triangle
{
    /*public static void main(String args[]) 
    {
        Scanner scan=new Scanner(System.in);
        int run = scan.nextInt();
        System.out.println("1");
        System.out.println("1 1");
        int count=0;
        ArrayList<Integer> nums = new ArrayList<Integer>();
        nums.add(0,1);
        nums.add(1);
        while(count<run-2)
        {
            ArrayList<Integer> nums2 = new ArrayList<Integer>();
            for(int i=0; i<nums.size()-1; i++)
            {
                nums2.add(nums.get(i)+nums.get(i+1));
            }
            nums2.add(0,1);
            nums2.add(1);
            nums=nums2;
            for(int i=0; i<nums2.size(); i++)
            {
                System.out.print(nums2.get(i)+" ");
            }

            System.out.println();
            count++;
        }    
    }
    */
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>(); 
        list.add(null);
        list.add(5);
    }
}
