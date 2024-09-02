//Casting
/*
Implicit Cast - Compiler does the casting for you
Ex: cout << 'c' + 5; -> 104 ('c' = 99)
Explicit Cast - You specify the casting
Ex: unsigned int k=1; //unsigned means k can't be a neg #, and in using static_cast<int> below, we can cast k to be assigned to a pos value
cout << static_cast<int>(k) - 2 << endl; -> -1 
const - is the same as final in java; so, can't be changed once declared
Ex: const int kDrivingAge = 16;
*/

//Selection

/*
If statements
Ex: 
if(bool) {
//code
} 
else if(bool) {

}
else {

}


Switch Statements
Ex: 
char grade = 'A';
switch (grade) {
    case 'A': //the value being checked can only be an int or char
        //code
        break; //tells it to exit the switch statement completely if the case is satisfied
    case 'B':
        //code
    ....

    default:
        //Only prints after all cases have been checked and none of them were satisfied
}
*/

//Short Circuiting
/*
int main() {
    int k = 0; 
    if(k!=0 && 10/k == 1) { //when 0, it's undefined, so what the code outputs is unpredictable
        //if the first part of the bool statement above is false, the computer uses a short-circuit method to automatically skip checking the rest of the bool statement
        //So, 10/k is never solved if k=0 since the first part would be false
        cout << "k is 10" <<endl;
    }
}
*/