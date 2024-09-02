public class Exceptions
{
    //Aside from everything below about the throws clause or try/catch blocks, 
    //it is possible to use the asserts function
    //Ex:
    /*
        void doIt(String it) {
        assert it != null : "That's not it!";
        System.out.println(it);
        }
        doIt("Good!");
        doIt(null);

        Output:
            Good!
            Threw an exception: java.lang.AssertionError: That's not it!
            at doIt(:7)
            at main(:12)

     */

     //However, to use asserts, it must be enabled in through the cmd using java -ea ClassName
     public static void main(String[] args) throws NullPointerException
     {
        try {
            throw new IndexOutOfBoundsException();
        } catch (IndexOutOfBoundsException e) {
            try
            { 
                System.out.println(1);
                throw new NullPointerException();
            }

            catch(NullPointerException h)
            {
                System.out.println(2);
            }

        }

        finally{ //Always executes despite try or catch being executed
            System.out.println("Always running");
        } //even if a return statement was involves in this method, the finally would run
       

        switch (5)
        {
        case 1,2,3: 
        System.out.println("Nope");
        break;
        case 4,5:
        System.out.println("Yup!");
        break;
        }
     }    

     public static void m1() 
     {
        System.out.println("m1");
        throw new IndexOutOfBoundsException();
     }
}
