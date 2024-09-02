import java.util.*;
class Sets
{
    //Creating a set
    public static void main(String[] args) 
    {
        //Set has no get() method to get a specific element
        //Best to use to have a unique collection of elements
        //At most 1 null 
        //classes: HashSet, LinkedHashSet, and TreeSet
        Set<String> set1=new HashSet<String>();
        set1.add("Why");
        set1.add("Who");
        set1.add("What");
        set1.add("When");
        set1.add("Where");
        set1.add("How");

        for(String word : set1)
        {
            System.out.println(word); //Set automatically organizes added info in order and doesn't maintain info in the order it was added
        }

        set1.add("Words");
        set1.add("What"); //no duplicates

        System.out.println(set1); 
    }
}