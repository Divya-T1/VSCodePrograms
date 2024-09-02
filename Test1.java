import java.util.ArrayList;
public class Test1 {
    public static void main(String[] args) {
        ArrayList arrayList = new SimpleArrayList(new Integer[0]);
        arrayList.add(0, 8);
        System.out.println(arrayList.get(0));
    }
}

interface SimpleList
{
    public Object get(int index);
    public void set(int index, Object element);
    public int size();
    public Object remove(int removeIndex);
    public void add(int addIndex, Object obj)

}

class SimpleArrayList implements SimpleList{
    /** Internal array for storing values. */
    private Object[] array;

    /**
     * Create a list from an array of Objects.
     *
     * Copies references from the passed array so that
     * modifications to this list will not affect the original array.
     * We'll need to make copies of the array later to support add and remove,
     * so this is the right thing to do now.
     *
     * @param originalArray original array of Objects used to create the list
     */
    SimpleArrayList(Object[] originalArray) {
        // Would normally need to defend against originalArray being null,
        // but we'll defer that until later.
        if (originalArray != null) {
            array = new Object[originalArray.length];
            for (int i = 0; i < originalArray.length; i++) {
                array[i] = originalArray[i];
            }
        }
    }

    public Object get(int index) {
        if (index < 0 || index >= array.length) {
            return null;
        }
        return array[index];
    }
    public void set(int index, Object element) {
        if (index >= 0 && index < array.length) {
            array[index] = element;
        }
    }

    public int size() {
        return array.length;
    }

    public Object remove(int removeIndex) {
        if (removeIndex < 0 || removeIndex >= array.length) {
            return null;
        }

        // remove returns the item being removed
        Object toReturn = array[removeIndex];

        // Create and populate our new smaller array. We use for loop syntax
        // maintaining two indices.
        Object[] newArray = new Object[array.length - 1];
        int originalIndex = 0;
        for (int newIndex = 0; newIndex < newArray.length; newIndex++) {
            // Skip the spot that we are removing
            if (newIndex == removeIndex) {
                originalIndex++;
            }
            newArray[newIndex] = array[originalIndex];
            originalIndex++;
        }
        array = newArray;
        return toReturn;
    }
    
    public void add(int addIndex, Object obj)
    {
       if(obj!=null && addIndex>=0 && addIndex<array.length)
       {
            Object[] newArray = new Object[array.length+1];
            int  arrayIndex = 0;
            for(int i=0; i<newArray.length; i++)
            {
                if(i==addIndex)
                {
                    newArray[i] = obj;
                    i++;
                }
                
                else
                {
                    newArray[i] = array[arrayIndex];
                    arrayIndex++;
                }
            }
            
            array = newArray;
       }
       
    }
}

class SimpleArrayList implements SimpleList {
    /** Internal array for storing values. */
    private Object[] array;

    /**
     * Create a list from an array of Objects.
     *
     * Copies references from the passed array so that
     * modifications to this list will not affect the original array.
     * We'll need to make copies of the array later to support add and remove,
     * so this is the right thing to do now.
     *
     * @param originalArray original array of Objects used to create the list
     */
    SimpleArrayList(Object[] originalArray) {
        // Would normally need to defend against originalArray being null,
        // but we'll defer that until later.
        if (originalArray != null) {
            array = new Object[originalArray.length];
            for (int i = 0; i < originalArray.length; i++) {
                array[i] = originalArray[i];
            }
        }
    }

    public Object get(int index) {
        if (index < 0 || index >= array.length) {
            return null;
        }
        return array[index];
    }
    public void set(int index, Object element) {
        if (index >= 0 && index < array.length) {
            array[index] = element;
        }
    }

    public int size() {
        return array.length;
    }

    public Object remove(int removeIndex) {
        if (removeIndex < 0 || removeIndex >= array.length) {
            return null;
        }

        // remove returns the item being removed
        Object toReturn = array[removeIndex];

        // Create and populate our new smaller array. We use for loop syntax
        // maintaining two indices.
        Object[] newArray = new Object[array.length - 1];
        int originalIndex = 0;
        for (int newIndex = 0; newIndex < newArray.length; newIndex++) {
            // Skip the spot that we are removing
            if (newIndex == removeIndex) {
                originalIndex++;
            }
            newArray[newIndex] = array[originalIndex];
            originalIndex++;
        }
        array = newArray;
        return toReturn;
    }
    
    public void add(int addIndex, Object obj)
    {
       if(obj!=null && addIndex>=0 && addIndex<array.length)
       {
            Object[] newArray = new Object[array.length+1];
            int  arrayIndex = 0;
            for(int i=0; i<newArray.length; i++)
            {
                if(i==addIndex)
                {
                    newArray[i] = obj;
                    i++;
                }
                
                else
                {
                    newArray[i] = array[arrayIndex];
                    arrayIndex++;
                }
            }
            
            array = newArray;
       }
       
    }
}

class SimpleArrayList implements SimpleList {
    /** Internal array for storing values. */
    private Object[] array;

    /**
     * Create a list from an array of Objects.
     *
     * Copies references from the passed array so that
     * modifications to this list will not affect the original array.
     * We'll need to make copies of the array later to support add and remove,
     * so this is the right thing to do now.
     *
     * @param originalArray original array of Objects used to create the list
     */
    SimpleArrayList(Object[] originalArray) {
        // Would normally need to defend against originalArray being null,
        // but we'll defer that until later.
        if (originalArray != null) {
            array = new Object[originalArray.length];
            for (int i = 0; i < originalArray.length; i++) {
                array[i] = originalArray[i];
            }
        }
    }

    public Object get(int index) {
        if (index < 0 || index >= array.length) {
            return null;
        }
        return array[index];
    }
    public void set(int index, Object element) {
        if (index >= 0 && index < array.length) {
            array[index] = element;
        }
    }

    public int size() {
        return array.length;
    }

    public Object remove(int removeIndex) {
        if (removeIndex < 0 || removeIndex >= array.length) {
            return null;
        }

        // remove returns the item being removed
        Object toReturn = array[removeIndex];

        // Create and populate our new smaller array. We use for loop syntax
        // maintaining two indices.
        Object[] newArray = new Object[array.length - 1];
        int originalIndex = 0;
        for (int newIndex = 0; newIndex < newArray.length; newIndex++) {
            // Skip the spot that we are removing
            if (newIndex == removeIndex) {
                originalIndex++;
            }
            newArray[newIndex] = array[originalIndex];
            originalIndex++;
        }
        array = newArray;
        return toReturn;
    }
    
    public void add(int addIndex, Object obj)
    {
       if(obj!=null && addIndex>=0 && addIndex<array.length)
       {
            Object[] newArray = new Object[array.length+1];
            int  arrayIndex = 0;
            for(int i=0; i<newArray.length; i++)
            {
                if(i==addIndex)
                {
                    newArray[i] = obj;
                    i++;
                }
                
                else
                {
                    newArray[i] = array[arrayIndex];
                    arrayIndex++;
                }
            }
            
            array = newArray;
       }
       
    }
}

class SimpleArrayList implements SimpleList {
    /** Internal array for storing values. */
    private Object[] array;

    /**
     * Create a list from an array of Objects.
     *
     * Copies references from the passed array so that
     * modifications to this list will not affect the original array.
     * We'll need to make copies of the array later to support add and remove,
     * so this is the right thing to do now.
     *
     * @param originalArray original array of Objects used to create the list
     */
    SimpleArrayList(Object[] originalArray) {
        // Would normally need to defend against originalArray being null,
        // but we'll defer that until later.
        if (originalArray != null) {
            array = new Object[originalArray.length];
            for (int i = 0; i < originalArray.length; i++) {
                array[i] = originalArray[i];
            }
        }
    }

    public Object get(int index) {
        if (index < 0 || index >= array.length) {
            return null;
        }
        return array[index];
    }
    public void set(int index, Object element) {
        if (index >= 0 && index < array.length) {
            array[index] = element;
        }
    }

    public int size() {
        return array.length;
    }

    public Object remove(int removeIndex) {
        if (removeIndex < 0 || removeIndex >= array.length) {
            return null;
        }

        // remove returns the item being removed
        Object toReturn = array[removeIndex];

        // Create and populate our new smaller array. We use for loop syntax
        // maintaining two indices.
        Object[] newArray = new Object[array.length - 1];
        int originalIndex = 0;
        for (int newIndex = 0; newIndex < newArray.length; newIndex++) {
            // Skip the spot that we are removing
            if (newIndex == removeIndex) {
                originalIndex++;
            }
            newArray[newIndex] = array[originalIndex];
            originalIndex++;
        }
        array = newArray;
        return toReturn;
    }
    
    public void add(int addIndex, Object obj)
    {
       if(obj!=null && addIndex>=0 && addIndex<array.length)
       {
            Object[] newArray = new Object[array.length+1];
            int  arrayIndex = 0;
            for(int i=0; i<newArray.length; i++)
            {
                if(i==addIndex)
                {
                    newArray[i] = obj;
                    i++;
                }
                
                else
                {
                    newArray[i] = array[arrayIndex];
                    arrayIndex++;
                }
            }
            
            array = newArray;
       }
       
    }
}