using System;

namespace BONUS
{
    class Bonus
    {
        static void Main(string[] args)
        {
            Console.Write("Please enter a string: ");
            string userInput = Console.ReadLine();

            // any opening bracket of the allowed type must have a closing bracket...

            // check that the opening bracket is valid
            char openingBracket = userInput[0];
            if (openingBracket == '(' || openingBracket == '[' || openingBracket != '{')
            {
                char closingBracket = userInput[userInput.Length - 1];
            }
        }
    }
}
