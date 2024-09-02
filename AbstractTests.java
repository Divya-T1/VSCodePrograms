public abstract class AbstractTests
{
    public abstract void yum();
    
    public static void main(String[] args) {
        int x;
        AbstractTests testing=null;
        testing.yum();
      
    }
    
}
abstract class test1 
{
    public abstract void eat();   
    public abstract void drink();
    
}

abstract class test2 extends test1
{
    public void eat()
    {
        System.out.println("I am eating!");
    }
}

class test3 extends test2
{
    public void drink()
    {
        System.out.println("I am drinking!");
    }
}

