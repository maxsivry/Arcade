import java.util.Scanner;
public class hangman{
   public static void main(String [] args){
      //instantiate input scanner
      Scanner input;
      input = new Scanner(System.in);
      //read in argument from command line
      String word = args[0];
      //create empty string which is used as a culmination of user guesses
      String workingWord = "";
      //create boolean for function while loop to operate with
      boolean wordGuessed = false;
      //populate working word variable with underscores
      for (int i = 0; i < word.length(); i++){
         workingWord = workingWord + "_";
      }
      //prompt user two to start game
      System.out.println("\n\n\n\n\n\n\n\n\n\n\nWelcome to Hangman! The user before you has written a word, now guess it!");
      //run hangman function
      hangman(word, workingWord, input, wordGuessed);
   }
   static boolean hangman(String word, String workingWord, Scanner input, boolean wordGuessed){
      //create word to be displayed at the end of the loop
      String printWord = "";
      //if (wordGuessed == true) return wordGuessed;
      //create infinite while loop (the function is recursive and program will terminate at the end)
      while(!wordGuessed){
         //prompt user to guess a letter
         System.out.println("Guess a letter:");
         //get input from user
         String letterString = input.nextLine();
         while(letterString.length() > 1 | letterString.length() == 0){
            System.out.println("please only one letter, case sensitive");
            letterString = input.nextLine();
         }
         //convert string to char
         char letter = letterString.charAt(0);
         //create a loop to iterate through the word
         for(int i = 0; i < word.length(); i++){
            //check if letter matches the character at i position in the word
            if (letter == word.charAt(i)){
                //if so, add this letter to the printword string
               printWord = printWord + letter;
            }
            else{
                //otherwise, add an underscore to the printword string
               printWord = printWord + "_";
            }
            //ensure that wordGuessed is false by checking for underscores
//             for (int j = 0; j < printWord.length(); j++){
//                if (printWord.charAt(j) == '_'){
//                   wordGuessed = false;
//                }
//
//             }
         }
//         System.out.println(printWord);
         //create finalWord variable to be passed into the function recursively
         String finalWord = "";
         //use for loop to iterate through workingWord and printWord
         for(int i = 0; i < printWord.length(); i++){
            //check if letter at printWord matches word at i
            if(printWord.charAt(i) == word.charAt(i)){
                //if so, add this letter to finalWord
               finalWord = finalWord + printWord.charAt(i);
            }
            //if not, check if the letter matches at working word (i) and word (i)
            else if(workingWord.charAt(i) == word.charAt(i)){
                //if so, add this char to the finalWord
               finalWord = finalWord + workingWord.charAt(i);
            }
            else{
                //if neither, add an underscore
               finalWord = finalWord + "_";
            }
         }
         //display final word
         System.out.println("Here's what you're working with:");
         System.out.println(finalWord);
         //check if the user has guessed the word
         if(finalWord.equals(word)){
            //run victory message function to kill the program and return to arcade
            printVictoryMessage();
         }
         //otherwise, recursively run hangman
         hangman(word, finalWord, input, wordGuessed);
      }
      //in case something goes horrible wrong it can return the boolean variable to exit the program safely
      return wordGuessed;
   }
   static void printVictoryMessage(){
      //print victory message
      System.out.println("Congratulations! You guessed the word!");
      //i hate recursion i hate recursion kill it with fire
      //exit program and return to arcade
      System.exit(0);
   }
}