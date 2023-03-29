//
// Created by Max Ivry on 10/27/22.
//
#include <fstream>
#include <iostream>
using namespace std;

// Different OSs use different CLI commands to run Languages
#ifdef _WIN32
// if running on Windows
const string python = "py";
#else
//If Mac/Linux
const string python = "python3";
#endif

//for running and compiling java
const string javaCompile = "javac";
const string java = "java";

//Prints the main menu of options:
void printMenu();

/*
 * Prompts the user for one of the options from the menu.
 * Validates input: makes sure the user enters exactly one character
 * and that it is one of the four valid options.
 * If it isn't valid, keep prompting for input until a valid option
 * is entered.
 */
char getArcade();
/*
 * get status method to prompt user if they'd still like to play and return a bool
 * Validates input to make sure input is either yes or no
 */
bool getStatus();

//method call for passing to hangman a word and validates to make sure it is a word no numbers no spaces
string getWord();

//method  that gets file name and does input validation to make sure it is a .txt
string getFilename();

int main() {

    //status to continue to play
    bool status = true;

    //opening statements
    cout << "Welcome to Max and Matt's arcade!" << endl;
    cout << "We have a few games for you to try if you enjoy fun!" << endl;

    while (status) {

        //print options and get options
        printMenu();
        char choice = getArcade();

        //depending on the choice, print statement and create and run command line
        string command;

        if (choice == 'a') {
            cout << "You chose Word Hunt!" << endl;
            //add info to pass to word hunt along with command line
            string fileName = getFilename();
            command = python + " ../word_hunt.py " + fileName;
            system(command.c_str());
        } else if (choice == 'b') {
            cout << "You chose Mancala!" << endl;
            command = python + " ../mancala.py";
            system(command.c_str());
        } else if (choice == 'c') {
            cout << "You chose Hangman!" << endl;
            //compile the java program
            command = javaCompile + " ../hangman.java";
            system(command.c_str());
            //add info to pass to hangman through getWord method call
            string word = getWord();
            command = java + " ../hangman.java " + word;
            system(command.c_str());
        }

        //would you still like to play?
        cout << "Would you like to keep playing? enter yes to continue or no to exit the arcade" << endl;
        status = getStatus();
    }

    //link to website for more information
    cout << "Thank you for your visit to our arcade!" << endl;
    cout << "Please checkout our accompanying website to learn more about our Module 3 open ended." << endl;
    cout << "link: https://mivry.w3.uvm.edu/CS120/" << endl;
    return 0;
}

//function definitions
void printMenu() {
    cout << "Which game would you like to play?" << endl;
    cout <<  "Choose: \n(a) Word Hunt! (b) Mancala! (c) Hangman!" << endl;
}

char getArcade() {

    //get input from user
    string input;
    string junk;
    //get input from user
    getline(cin, input);

    //while input is invlaid
    while (input != "a" && input != "b" && input != "c" && input != "d") {
        //clear the stream
        cin.clear();
        //reprompt
        cout << "Not one of the options. Try again!" << endl;
        getline(cin, input);
    }
    char c = input[0];
    return c;
}
bool getStatus() {
    //get input from user
    string input;
    string junk;
    //get input from user
    getline(cin, input);

    //while input is invlaid
    while (input != "yes" && input != "no") {
        //clear the stream
        cin.clear();
        //reprompt
        cout << "Must be true or false! Try again!" << endl;
        getline(cin, input);
    }
    //if input is yes versus if input is no
    if (input == "yes") {
        return true;
    }
    else if (input == "no") {
        return false;
    }
}

string getWord() {

    //variable declaration
    string input;
    bool status = false;

    //opening statement
    cout << "Enter a word for the user to guess"<<endl;

    //get input into str
    getline(cin,input);

    // while does not meet all conditions to be a word
    while (!status) {
        // if there is no input, display message re-prompt user
        if (input.empty())
        {
            //clear stream display message reprompt user
            cin.clear();
            cout << "No input, enter a single word" << endl;
            getline(cin,input);
        }

            //else, for each letter in word
        else if (!(input.empty()))
        {
            //status is true unless...
            status=true;

            //for each char in length if char is a letter and is not a space
            for (int i = 0; i < input.length(); i++)
            {
                if (!(isalpha(input[i]))) {
                    status = false;
                }
                if (input[i] == ' ') {
                    status = false;
                }
            }
            //if input is not valid word display message clear stream and reprompt
            if (!status)
            {
                cin.clear();
                cout << "invalid input, enter a single word" << endl;
                getline(cin, input);
            }
        }
    }
    //if exiting the loop then return the input
    return input;
}

string getFilename() {
    //prompt user for file name
    cout << "What is the name of your file you would like to print the results of Word hunt to? (must be .txt)" << endl;
    cout << "If input is invalid, will use finalResults.txt" << endl;
    //get input
    string input;
    getline(cin, input);

    //if input is empty return default
    if (input.empty()) {
        return "finalResults.txt";
    }
    else {
        //find the file extension
        string fileExtension = "";
        fileExtension.append(1,input[input.length()-4]);
        fileExtension.append(1,input[input.length()-3]);
        fileExtension.append(1,input[input.length()-2]);
        fileExtension.append(1,input[input.length()-1]);

        //test if valid file extension, return default
        if (fileExtension != ".txt" ) {
            return "finalResults.txt";
        }
        //for each char in length if char is a letter and is not a space
        for (int i = 0; i < input.length(); i++)
        {
            if (!(isalpha(input[i])) && input[i] != '.') {
                return "finalResults.txt";
            }
            if (input[i] == ' ') {
                return "finalResults.txt";
            }
        }
    }
    return input;
}
