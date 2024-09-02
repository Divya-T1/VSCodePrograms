public class Interfaces 
{
    //Every Java object has an interface
    //while inheritance allows only one class to be extended, interfaces allow a class to implement multiple interfaces while also extending or not extending another class

    public static void main(String[] args) /*throws Exception*/ 
    {
        //Shape shape = new Shape();  isn't possible to instantiate and create an object for, but we can extend from an abstract class and utilize its child classes
        Square square = new Square(); 
        System.out.println(square.sides());
        Shape shape = new Circle(); //shows the idea of polymorphism
        System.out.println(shape.sides()); 
        System.out.println();

        //Looking at references with Interfaces
        Simpler simpler = new Simpler();
        System.out.println(simpler.simple(1));
        Simple simple = new Simpler(); //Can use interface class to create references of the classes that actually implement the interface class
        System.out.println(simple.simple(1));
        /*System.out.println(simple.simpler());*/ //can't call the method simpler since it isn't a part of the Simple class and only exists in Simpler class which implements the interface Simple since the reference variable is of type interface, Simple
        simple = new Another(); //reassigning the previous reference to that of a reference to the Another class
        System.out.println(simple.simple(1)); //so, we are using the simple method from the Another class
    }

}

abstract class Shape 
{
    public abstract int sides();  /*can't have a method body since it's an abstract method, but any of the child classes that extend or implement this class, must define the method body*/

}

class Square extends Shape //since we utilize the extends word for abstract classes, we can only extend one abstract class at a time, but interfaces which essentially mimic abstract classes allow us to implement multiple interfaces simultaneously
{
    public int sides()
    {
        return 4;
    }
}

class Circle extends Shape
{
    public int sides()
    {
        return 0;
    }
}

interface Simple {
    //simple returns its argument +1
    int simple(int first);

}

interface Second {
    void example();
}

class Parent { }

class Simpler extends Parent implements Simple, Second 
{
    public int simple(int argument) //method must be public because methods of interfaces are by default public
    {
        return argument + 1;
    }

    public void example() {

    }

    public void simpler()
    {

    }
}

class Another extends Parent implements Simple, Second 
{
    public int simple(int argument) //method must be public because methods of interfaces are by default public
    {
        return argument - 1;
    }

    public void example() {

    }
}

//Working with the interface Comparable

/*class Example implements Comparable {
    private int value;
    public Example(int setValue) {
      value = setValue;
    }
    @Override
    public String toString() {
      return "Example with value=" + value;
    }
    @Override
    public int compareTo(Object o) {
      Example other = (Example) o; #will throw a ClassCastException if Example instance isn't provided in the parameter
      #Must follow the contract in the documentation of compareTo in Comparable<> where the method must provide 0 if the objects are equal, -1 if the instance is smaller than the parameter, and 1 if vice versa
        if (value < other.value) {
        return -1;
        } else if (value > other.value) {
        return 1;
        } else {
        return 0;
        }
        }
  }
  Example example = new Example(8);
  Example second = new Example(10);
  Example third = new Example(10);
  System.out.println(second.compareTo(third));
  Example[] examples = {new Example(10), new Example(5), new Example(12)};
Arrays.sort(examples); #this only works because the class Example implements the class Comparable which is a requirement of Arrays.sort()
System.out.println(Arrays.toString(examples));*/

//Working with the interfaces Iterable and Iterator






























