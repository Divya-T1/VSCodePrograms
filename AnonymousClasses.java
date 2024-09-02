public class AnonymousClasses {
    public static void main(String[] args) {
        Person person = new Person(); 
        System.out.println(person.getType());
        //Creating an anonymous class
        //Are especially useful to act as a shortcut for repetative logic
        Person student = new Person() //the name of the class being extended or implemented must be written out
        {
            //These anonymous classes are solely used to override and new methods and variables can't be introduced since the classes are nameless and simply don't have references so they can't be indentified or have new variables/methods
            //They can't create a constructor, but in the case on extended from a superclass, the beginning declaration may fill in the parameters based on constructors of the superclass

            @Override
            public String getType()
            {
                return "Student";
            }

            
        };
        System.out.println(student.getType());
        int i=0;
        Test test = new Test() {
            @Override
            public int test()
            {
                return i;
            }
        };

        //i=12; when a variable is utilized in an anonymous class, it can't be altered in any way afterwards or within the class itself
        //To not have to deal with this and make it easier to remember the value can't be altered, we can also intially declare the variable as final

        System.out.println(test.test());
        AnonymousClasses ac = new AnonymousClasses();
        ac.doIt();
    }

    int countArray(int[] values, IncludeValue includeValue) {
        int count = 0;
        for (int value : values) {
          if (includeValue.include(value)) {
            count++;
          }
        }
        return count;
      }

      void doIt() {
        int[] array = {1, 2, 5, -1};
        System.out.println(countArray(array, new IncludeValue() {
          @Override
          public boolean include(int value) {
            return value < 0;
          }
        }));
      }
}

//Anonymous classes must either extend a superclass or implement an interface
//Ex:

//Here is a superclass
class Person
{
    public String getType()
    {
        return "Person";
    }
}

//Ex2:

interface Test{ 
    int test();
}

//Ex3:
interface IncludeValue {
    // Return true if the value should be counted
    boolean include(int value);
  }










