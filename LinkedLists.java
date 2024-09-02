public class LinkedLists {
//unlike elements from arrays, LinkedLists have items where each item consists of 2 parts: the value and next
//the next references the value of the next item within the LinkedList
//to reference the value of item1 or define what item #1 is, we use item.start
//this concept involves the idea of inner classes

//the first item you add to a linkedList ends up becoming the last item when the entirity of the list is complete
    public static void main(String[] args) {
        
    }
}

interface SimpleList {
    Object get(int index);
    void set(int index, Object value);
    Object remove(int index);
    void add(int index, Object value);
    int size();
}

class SimpleLinkedList implements SimpleList{
    private class Item {
        private Object value;
        private Item next;
        Item(Object setValue, Item setNext) {
            value = setValue;
            next = setNext;
        }
    }
    public Object get(int index)
    {

    }
    public void set(int index, Object value);
    public Object remove(int index);
    public void add(int index, Object value);
    public int size();
}

