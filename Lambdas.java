public class Lambdas {
    // is a shortcut for anonymous classes, but solely implements interfaces that
    // have one abstract method

    public static void main(String[] args) {
        Modify mod = ( /*int -> can include this if i want*/value) -> { 
            //or if a single statement with no loops or conditionals, we can just say value -> value - 1;
            if (value < 0) {
                return value - 1;
            }

            return value + 1;
        };

        System.out.println(mod.modify(2));

    }
}

interface Modify {
    int modify(int value);
}
