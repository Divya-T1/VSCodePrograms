import java.util.*;

class Maps {
    // Creating a map
    public static void main(String[] args) {
        // Map has no get() method to get a specific element
        // Best to use to store the data in the form of key/value pair 
        // At most 1 null key and any number of null values
        // classes: HashMap, LinkedHashMap, and TreeMap, HashTable, ConcurrentHashMap
        Map<Integer, String> map1 = new HashMap<Integer, String>();
        map1.put(1, "Venkat");
        map1.put(3, "Divya");
        map1.put(2, "Dhana");  
        map1.put(4, "Chinnu");

        for (Map.Entry m : map1.entrySet()) {
            System.out.println(m.getKey()+" "+m.getValue()); // Map orders automatically based on key, and order of insertion doesn't matter
        }

        map1.put(5, "Dhana");
        map1.put(2, "Lakshmi"); //changes key 2 to now equal Lakshmi

        System.out.println(map1);
    }
}