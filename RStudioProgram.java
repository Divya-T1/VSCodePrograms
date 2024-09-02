
import java.io.IOException;
public class RStudioProgram {
    @SuppressWarnings("deprecation")
    public static void main(String[] args)
    {
        Runtime runtime=Runtime.getRuntime();

        try{
            runtime.exec("notepad.exe")

        }

        catch (IOException e)
        {

        }
    }
}
