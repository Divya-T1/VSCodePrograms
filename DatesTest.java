import java.time.LocalDate;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class DatesTest 
{
    public final int NUMS;
    static{
        DatesTest datess=new DatesTest();
        datess.NUMS=4;
    }
    public static void main(String[] args) {
        DateTimeFormatter form = DateTimeFormatter.ofPattern("MM dd yyyy");
        String dates="01 02 2015";
        LocalDate date =  LocalDate.parse(dates , form);
        System.out.println(date);

       


       
    }
}
