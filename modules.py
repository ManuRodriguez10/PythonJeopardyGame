def jeopardy_intro():
    '''
    Breaks up the introduction into smaller parts and using the enter key (or any input) to move to the next part of the introduction
    parameters: nothing
    :return: nothing
    prints introduction and game rules
    '''
    print("Welcome to Jeopardy!\n"
          "Get ready to test your trivia skills and strategic thinking in this thrilling game.\n"
          "Here's how it works:\n")
    input("Press Enter to continue...")
    #Moves to second part of intro
    print("\n1. Categories and Clues:\n"
          "\t- We have various categories, each hiding clues with different monetary values.\n"
          "\t- Players take turns choosing a category and a clue within it.")
    input("Press Enter to continue...")
    #Moves to third part of intro
    print("\n2. Answering Clues:\n"
          "\t- Players respond to the clue in the form of a question.\n"
          "\t- For instance, if the clue is 'The capital of France,' the correct response would be 'What is Paris?'\n"
          "\t- Correct answers earn you the money associated with that clue.")
    input("Press Enter to continue...")
    #Moves to fourth part of intro
    print("\n3. Gameplay:\n"
          "\t- Players can choose to skip a question, but there's a penalty for doing so.\n"
          "\t- Incorrect answers lead to a deduction of the clue's value from the player's score.\n"
          "\t- If a player gets the answer incorrect, the other player will have the chance to take the prize from them if they answer correctly.")
    input("Press Enter to continue...")
    #Moves to fifth part of intro
    print("\n4. Winning the Game:\n"
          "\t- The game continues until all clues are exhausted or a player reaches a winning score.\n"
          "\t- The player with the highest total score at the end emerges as the Jeopardy champion!")
    input("Press Enter to continue...")
    #Moves to last part of intro
    print("\nAre you ready to showcase your knowledge and strategy in the world of Jeopardy?\n"
          "Let the games begin!\n")

    return True

def display_board(categories, money_values_five, player1, player1_score, player2, player2_score):
    """
    Display the game board with categories, money values, and player scores.
    Algorithm:
    1. Initialize an empty list 'categories_all_same_length' to store categories with the same length.
    2. Find the maximum length among all categories.
    3. Iterate through each category and make its length equal to the maximum length by adding spaces.
    4. Print the formatted categories and money values in a table format.
    5. Print the scores of player 1 and player 2.

    Explanation:
    - The function takes categories, money values, and player information as input parameters.
    - It ensures that all categories have the same length for proper formatting.
    - The maximum length among categories is determined to ensure consistent formatting.
    - Categories are padded with spaces to match the maximum length.
    - The function then prints the formatted categories and money values in a table format.
    - Player names and scores are printed below the table.
    - The function does not return any value.

    :parameter categories: List of category names.
    :param money_values_five: 2D list containing money values for each category.
    :param player1: Name of player 1.
    :param player1_score: Score of player 1.
    :param player2: Name of player 2.
    :param player2_score: Score of player 2.

    :return: No returns
    """
    # Makes all categories the same length
    #Initialize list and max_length
    categories_all_same_length = []
    max_length = 0
    for cat in categories:  #Iterate through each index in categories list
        if len(cat) > max_length: #compares current indexed category to the max length so far found
            max_length = len(cat) #if length of current iteration is greater than max length found already then replaces the max length value
    for cat in categories: #iterates through each category in categories list
        if len(cat) != max_length: #if the length of the category was not as long as the max length
            missing_length = max_length - len(cat) #finds how much shorter the current category is compared to the max length and sets it equal to missing_length
            categories_all_same_length.append(cat+ " " * missing_length + " |||     ") #adds the needed spaces to make all the categories the same length and additional aesthetics
        else:
            categories_all_same_length.append(cat+" |||     ") #adds aesthetics for display board

    # During each iteration, the for loop pairs elements from 'categories_all_same_length' and 'money_values_five'-->,
    # assigning the 'category' variable to an element from the categories_all_same_length_list and 'values' variable-->
    # to the corresponding element from the money_values_five list.
    for category, values in zip(categories_all_same_length, money_values_five):
        print("{:<10}".format(category), end="")  # Print the formatted category with a width of 10 spaces
        for value in values: # Iterate through the money values for the current category
            print("{:<15}".format(value),end="") # Print each money value with a width of 15 spaces
        print() # Move to the next line after printing all values for a category
    # How our data is being stored
    '''money_values_five = [
    ["$100", "$200", "$300", "$400", "$500"],
    ["$100", "$200", "$300", "$400", "$500"],
    ["$100", "$200", "$300", "$400", "$500"],
    ["$100", "$200", "$300", "$400", "$500"],
    ["$100", "$200", "$300", "$400", "$500"]
    ]
    '''
    # How it is being printed
    """
    categories = [baseball, soccer, basketball, football, olympics]
    categories[0] ||| ["$100", "$200", "$300", "$400", "$500"]
    categories[1] ||| ["$100", "$200", "$300", "$400", "$500"]
    categories[2] ||| ["$100", "$200", "$300", "$400", "$500"]
    categories[3] ||| ["$100", "$200", "$300", "$400", "$500"]
    categories[4] ||| ["$100", "$200", "$300", "$400", "$500"]
    """
    print(f"\t{player1}: {player1_score}\t\t{player2}: {player2_score}") #prints player score
    return
def update_board(money_values_five, categories, category, money_values, money_value):
    """
    Purpose: Update the game board to mark a used clue.

    :param money_values_five: 2D list containing money values for each category.
    :param categories: List of category names.
    :param category: Chosen category.
    :param money_values: List of money values.
    :param money_value: Chosen money value.

    :return: No returns

    Algorithm:
    1. Find the indices of the chosen category and money value in the board.
    2. Mark the corresponding position in 'money_values_five' with 'X'.

    Explanation:
    - The function takes the game board, category, and money value as input.
    - It finds the indices of the chosen category and money value in the board.
    - The function updates the board by marking the corresponding position with 'X'.
    """
    index_category = categories.index(category) #gets index of category chosen
    index_money_value = money_values.index(money_value) #gets index of money value chosen

    money_values_five[index_category][index_money_value] = 'X' #uses indicies to replace -' with an 'x'
def get_clue(jeopardy_data, used_clues_list, categories, money_values):
    '''
    Algorithm:
    1. Asks user to input a valid category and money value (and will keep asking until they provide one)
    2. Using both inputs from the user it will take them and use them to search through the JSON file
    3. From there it will pull the specific clue from that specific category and money value
    4. Then it will check if the clue has already been used or not using the used_clue funtion will check if
        it has been used or not, and return a True(yes, used), or False(not used).
        a. if the clue has been used then it will go and use recursion to repeat the function (get_clue) until the user
            picks a valid clue to use
        b. if the clue has not been used, then the function will return the values category, clue, and money_value to be used
             as parameters in the main function.

    :param jeopardy_data: Dictionary containing Jeopardy game data
    :param used_clues_list: List to track clues that have already been used
    :param categories: List of available categories
    :param money_values: List of available money values
    :return: Tuple containing category, clue, and money value for the selected clue.
    '''
    # ask user to choose a category and make sure it is a valid category
    category = input(f"Which category would you like to pick?: ").strip().lower()
    while category not in jeopardy_data['categories']:
        category = input("Please enter a valid category: ").strip().lower()

    # ask user to choose a money value and make sure it is a valid value from the selected category
    money_value = '$' + input(f"Which money value?: $")
    while money_value not in jeopardy_data['categories'][category]:
        money_value = '$' + input(f"Please enter a valid money value {money_values}: $")

    # get clue for the selected category and money value
    clue = jeopardy_data['categories'][category][money_value]['clue']

    # Check if the selected clue has already been used
    if used_clue(used_clues_list, clue):
        # If the clue has been used, use recursion for the function to call itself to get another clue
        return get_clue(jeopardy_data, used_clues_list, categories, money_values)

    elif not used_clue(used_clues_list, clue):
        # If the clue has not been used, return the category, clue, and money value
        return category, clue, money_value

def used_clue(used_clues_list, clue):
    '''
    Helping function to check is a clue has already been used
    :param used_clues_list:
    :param clue:
    :return: True or False bool value
    '''
    if clue in used_clues_list:
        print("This clue has already been used. Please choose another one.")
        return True
    else:
        return False

def check_answer(clue, player_answer, jeopardy_data):
    '''

    Algorithm:
    1. Search for the correct answer by first looping through Jeopardy categories, then values to find the
    correct answer for the given clue.
    2. Finally, break the loop when the correct answer is found.
    3. Check player's answer by using conditionals to check for:
        a. If the player's answer matches the correct answer return True.
        b. Otherwise, return False

    :param clue:The clue for which the answer is being checked
    :param player_answer:The player's answer to the clue
    :param jeopardy_data:Dictionary containing Jeopardy game data
    :return: True if correct, False if incorrect
    '''
    # Iterate through each category in the Jeopardy data
    for category in jeopardy_data['categories']:
        # Then iterate through each money value in that current category
        for value in jeopardy_data['categories'][category]:
            # Check if the clue tied to the current money value matches the provided clue
            if jeopardy_data['categories'][category][value]['clue'] == clue:
                # If there is a match, retrieve the correct answer and exit the loop
                correct_answer = jeopardy_data['categories'][category][value]['answer']
                break

    # Conditionals to check for different inputs
    if player_answer.strip().lower() == correct_answer.strip().lower():
        return True
    else:
        return False

def get_win(player1, player1_score, player2, player2_score, money_values_five):
    '''

    Algorithm:
    1. Iterate through each list in money_values_five (display board) and check each value in the list for an 'X'
        a. If any value is not 'X', set game_finished to False and break from the loop.
        b. If all the values are 'X', game_finished stays as a True bool value and goes onto the second part of the function
    2. If game_finished equals to True, there are conditionals for one of 3 scenarios:
         a. If player1_score has a greater score, and prints a victory message for player1.
         b. If player2_score has a greater, and prints a victory message for player2.
         c. If player1_score and player2_score are equal, print a tie message.
            i. Return True to indicate the end of the game.
    3. If game_finished is False, return False to continue the game.

    :parameter:player1: Name of player 1
    :parameter:player1_score: Score of player 1
    :parameter:player2: Name of player 2
    :parameter:player2_score: Score of player 2
    :parameter:money_values_five: Display board represented by a list of lists
    :returns: True if game finished, False otherwise
    '''

    # Checks if any value in the display board is not 'X'
    game_finished = True
    for row in money_values_five:
        for value in row:
            if value != 'X':
                game_finished = False
                break

    # Checks for a win using player scores and prints victory/tie messages
    if game_finished:
        if player1_score > player2_score:
            print(f"Congratulations!\n{player1}, you won Jeopardy.")
        elif player2_score > player1_score:
            print(f"Congratulations!\n{player2}, you won Jeopardy.")
        elif player1_score == player2_score:
            print(f"Congratulations!\nYou both have tied Jeopardy.")
        return True
    else:
        return False