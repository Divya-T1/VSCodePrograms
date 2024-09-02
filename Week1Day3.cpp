/*
Organizing C++ code
2 components:
    -Header files (.hpp) -> have function declarations (explains what it does)
    -Source files (.cc) -> have function definitions (how does it do it)

    Ex:
    The header file (functions.hpp)
    /*Requires:
    Modifies: cout
    Effects: prints out a welcome message
    void func(String name);
    */ 
    //The source file (functions.cc)
    /*
    void func(String name){
        cout << "Welcome!" << name <<endl;
    }
    */ 

//driver.cc -> turns code into a format understandable to the computer (machine code)
//functions.cc & functions.hpp -> compile the code separately, and then use a linker to actually run the code, output a compile error, or compile a runtime error

/* TO RUN FILES IN THE PRAIRE WORKSPACE, START WITH make exec
    THEN SAY ./bin/exec */

/*
For Loops:
    //Use when you know how many times you want to run smt
    for(int i=0; i<2; i++) { //checks the first declared value too
        cout << i;
    }

    //Use when you want it to run until a condition changes
While Loops:
    int i=0;
    while(i<2) {

    }
*/

/*
for(int i; i<2; i++) {
    cout << i << " "; //may compile or may not (if it compiles, it will print smt random because it will take whatever i has been "stored" as within memory)
}
*/

/*
Vectors:
    -must have this line at the top with #include <iostream>
    #include <vector>

    vector<int> vec = {1, 2} (essentially declared type int of a vector with the name vec)
    *Access Elements: vec[index#]
    *Functions:
        -push_back(#) -> adds # to the end
            Ex: vec.push_back(7);
    *Looping through vec
        for(unsigned int i=0; i<vec.size() (return type of size() is unsigned int); i++) {
            cout << vec[i];
        }
    
*/