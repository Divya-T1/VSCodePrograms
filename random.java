import java.time.LocalDate;
import java.time.LocalTime;
import java.time.Period;
import java.time.format.DateTimeFormatter;
import java.time.format.FormatStyle;
import java.util.Scanner;
public class random 
{
    public String yo="yo";
    
    static 
    {
        System.out.print("1 ");
    }
    {
        System.out.print("2 ");
    }
   
    
    private static random rand1=new random();
    public random()
    {

    }
    public random(String hi)
    {

    }
    public static void main(String[] args) 
    {
       
        //rand.length=3;
        //System.out.println(rand.length);
       /*  Scanner scan=new Scanner(System.in);
        String input=scan.next();
        String input2="";
        for(int i=input.length()-1; i>=0; i--)
        {
            input2=input2+input.substring(i,i+1);
        }
        System.out.println(input2);
        */
        String s="java";
        StringBuilder s2=new StringBuilder("java");
        System.out.println(s.equals(s2));
        double hi=(byte) 50;
        int i=0;
        i=i++;
        System.out.println(i);
        byte x = 5;
        byte y = 10;
        byte z = (byte) (x + y);
        LocalTime time = LocalTime.of(19, 3, 50);
        LocalTime time2 = time.minusHours(1);
        System.out.println(time2.format(DateTimeFormatter.ISO_LOCAL_TIME));
        Period period=Period.ofYears(2);
        DateTimeFormatter dateFormat= DateTimeFormatter.ofLocalizedDate(FormatStyle.SHORT);
        LocalDate date=LocalDate.of(2006,8,13);
        LocalDate date2 = date.plus(period);
        System.out.println(dateFormat.format(date2));
        
        System.out.println(x);
    }
    


}

class rand2
{
    public static int length=4;
}
