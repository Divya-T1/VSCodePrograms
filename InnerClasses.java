public class InnerClasses {
    public static void main(String[] args) {
        Outer.Inner inner = new Outer().create();
        inner.greet();
    }
}

class Outer {
    class Inner {
        void greet() {
            System.out.println("here");
        }
    }

    Inner create() {
        return new Inner();
    }
}
