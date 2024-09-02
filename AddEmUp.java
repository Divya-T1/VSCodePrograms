import java.util.ArrayList;
import java.util.Scanner;
class AddEmUp
{
    public static void main(String[] args)
    {
        int[] values=new int[5];
        for(int i=0; i<values.length; i++)
        {
            values[i]=i+1;
        }

        int total=0;

        for(int element : values)
        {
            total+=element;
        }

        System.out.println(total);
    }
    /*static int numCards, sumCards;
    static ArrayList<String> cardNums;

    public static void main(String[]args)
    {
        Scanner scan=new Scanner(System.in);
        String sum=scan.nextLine();
        scan=new Scanner(System.in);
        String cards=scan.nextLine(); 

        numCards = Integer.parseInt(sum.substring(0,sum.indexOf(" ")));
        sumCards = Integer.parseInt(sum.substring((sum.indexOf(" ")+1)));
        String[] nums = cards.split(" ", numCards);
        cardNums=new ArrayList<String>();


     
        for(int i=0; i<nums.length; i++)
        {
            cardNums.add(nums[i]);
        }

       

        if(check())
        {
            System.out.println("YES");
        }

        else
        {
            System.out.println("NO");
        }
    }

    public static boolean check()
    {
        boolean checks=false;
        int sizes=cardNums.size();
        for(int i=0; i<sizes; i++)
        {
            String value=findNum(cardNums.get(i));

            if(!(value.equals("")))
            {
                cardNums.add(value);
            }
        }

        for(int i=0; i<cardNums.size()-1; i++)
        {
            for(int j=i+1; j<cardNums.size(); j++)
            {
                if(((Integer.parseInt(cardNums.get(i)))+(Integer.parseInt(cardNums.get(j))))==sumCards && !(j-i==numCards))
                {
                    checks=true;
                    j=cardNums.size()-1;
                    i=cardNums.size()-2;
                }

                else
                {
                    checks=false;
                }
            }
        }

        return checks;
    }

    public static String findNum(String num)
    {
        boolean checker=true;
        String temp="";
        String finalNum="";
        for(int i=0; i<num.length(); i++)
        {
            if(num.substring(i,i+1).equals("0") || num.substring(i,i+1).equals("1") || num.substring(i,i+1).equals("2") ||
            num.substring(i,i+1).equals("5") || num.substring(i,i+1).equals("8"))
            {
                temp+=num.substring(i, i+1);
            }

            else if(num.substring(i,i+1).equals("6"))
            {
                temp+="9";
            }

            else if(num.substring(i,i+1).equals("9"))
            {
                temp+="6";
            }

            else
            {
                checker=false;
            }
        }

        if(checker)
        {
            for(int i=temp.length()-1; i>=0; i--)
            {
               finalNum+=temp.substring(i,i+1);
            }
        }


        if(finalNum.equals(num))
        {
            return "";
        }

        else
        {
            return finalNum;
        }

    }
    */
}