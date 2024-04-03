import modules
import json
def main():
    '''
    The main function runs the main components of the Jeopardy game

    1. Load jeopardy data from JSON file and make it available to use
    2. Initialize variables and lists that will be used throughout the game
    3. Begin the game by introducing the players to the rules
    4. Begin the gameplay
        a. if a player gets the correct answer they keep playing
        b. if a player gets the wrong answer it first gives the other player a chance to answer or skip
        c. Then whether the second player gets it wrong or right it switches to them anyways to call a clue
    5. This process repeats until all the questions are used and then the game finishes, and the winner is
      calculated

    parameters: none
    return: none
    '''
    # Load and make JSON file with Jeopardy data available to read as "jeopardy_data"
    json_file = 'jeopardy_SQA'
    with open(json_file, 'r') as file:
        jeopardy_data = json.load(file)

    # Gets all the categories, and money values we are using from the JSON file and stores them within lists
        # (Allows us in future to change categories without changing print statements within main)
    categories = []
    money_values = []
    money_values_five = []
    # Pulls categories and money values from JSON file
    for category in jeopardy_data['categories']:
        categories.append(category)

        for money_value in jeopardy_data['categories'][category]:
            if money_value not in money_values:  # So it only adds a singular money value once
                money_values.append(money_value)

    # Creates a list within a list for each money value
    for i in range(len(categories)):
        money_values_five.append(list(money_values))

    # Introduction Message
    modules.jeopardy_intro()

    # Get player names
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    current_player = player1
    # Initialize Scores
    player1_score = 0
    player2_score = 0
    current_player_score = player1_score
    # Initialize list for clues that have been used (so that we do not reuse them)
    used_clues_list = []
    game_over = False  # Set bool value to game_over

    while game_over != True:  # A while loop that will end once game_over equals to True

        # Display's the Jeopardy game board and then begins the turns
        modules.display_board(categories, money_values_five, player1, player1_score, player2, player2_score)
        print(f"\nIt's {current_player}'s turn.")

        # gets the clue and goes to function
        category, clue, money_value = modules.get_clue(jeopardy_data, used_clues_list, categories, money_values)
        print(f"\n\t\t\tClue: \n{clue} ")  # Presents clue

        player_answer = input("\nWhat is...").strip() # Player answers in this format

        if not player_answer:  # if player does not answer they are asked to put something
            print("Please provide an answer.")
            player_answer = input("\nWhat is...").strip()

        while modules.check_answer(clue, player_answer, jeopardy_data):  # A while loop making it so that as long as
                                                                        # the player keeps getting it correct they keep playing
            print(f"\nCorrect answer! You earned {money_value}")

            current_player_score += int(money_value[1:])  # Turn money value into int and add it to the current players score
            # adds that current score to the players score (depending on who's turn it is)
            if current_player == player1:
                player1_score = current_player_score
            else:
                player2_score = current_player_score

            print(f"{current_player}, your score is now ${current_player_score}")  # Presents current score

            used_clues_list.append(clue) # Since in this loop they get it correct, you can not use that clue anymore

            # Display's the Jeopardy game board and updates it by marking an 'X' wherever the used question is
            modules.update_board(money_values_five, categories, category, money_values, money_value)
            modules.display_board(categories, money_values_five, player1, player1_score, player2, player2_score)

            # Checks if the game is done at this point and will end depending on whatever is returned game_over will be True or False
            if modules.get_win(player1, player1_score, player2, player2_score, money_values_five):
                game_over = True
                break

            # Since it is still the players turn they go again
            category, clue, money_value = modules.get_clue(jeopardy_data, used_clues_list, categories, money_values)
            print(f"\n\t\tClue: \n{clue} ")
            player_answer = input("\nWhat is...").strip().lower()


        if modules.check_answer(clue, player_answer, jeopardy_data) is False: # This if statement is if they get the answer incorrect
            # Player gets answer wrong if they call on the clue and get it wrong or skip it
            if player_answer == 'skip':
                print(f"{current_player} has decided to skip the question.")
                print(f"\n{current_player}, you have been deducted {money_value} for skipping a question.")
            else:
                print(f"{current_player}, your answer was incorrect. You have been deducted {money_value}.")

            # Edits the current players score and displays the updated score
            current_player_score -= int(money_value[1:])
            print(f"{current_player} your score is now ${current_player_score}")

            # Update the score of the previous player with the correct value
            # Switch players and then switch to other players score
            if current_player == player1:
                player1_score = current_player_score
                current_player = player2
                current_player_score = player2_score
            else:
                player2_score = current_player_score
                current_player = player1
                current_player_score = player1_score

            # Allows for other person to attempt to steal question.
            player_answer = input(f"\n{current_player}, do you know the answer?:\n\nWhat is... ")

            if not player_answer:  # if player does not answer they are asked to put something
                print("Please provide an answer.")
                player_answer = input("\nWhat is...").strip()

            # The other player won't be penalized if they skip it because they did not call on the question
            if player_answer.lower() == 'skip':
                print(f"{current_player} has decided to skip the question.\n")
                #Makes sure that if both players skipped this question it just stays as used
                used_clues_list.append(clue)
                modules.update_board(money_values_five, categories, category, money_values, money_value)
                # Shows the answer when both players skip the question
                print(f"Well, the answer was...{jeopardy_data['categories'][category][money_value]['answer']}."
                      " Better luck next time.\n")
                continue  # Exit the inner loop and start a new turn (at the beginning of the first while loop)

            # If the player it switches to gets it right instead of skipping this executes and then
            if modules.check_answer(clue, player_answer, jeopardy_data):
                print(f"\nCorrect answer! You earned {money_value}")
                current_player_score += int(money_value[1:])
                used_clues_list.append(clue)
                modules.update_board(money_values_five, categories, category, money_values, money_value)

                #Adds score
                if current_player == player1:
                    player1_score = current_player_score
                    print(f"Your score is now ${current_player_score}")
                else:
                    player2_score = current_player_score
                    print(f"Your score is now ${current_player_score}")

                if modules.get_win(player1, player1_score, player2, player2_score, money_values_five):
                    game_over = True
                    break
                else:
                    continue  # Exit the inner loop and start a new turn (at the beginning of the first while loop)

            # If the player it switches to gets it right instead of skipping this executes and then
            if modules.check_answer(clue, player_answer, jeopardy_data):
                print(f"\nCorrect answer! You earned {money_value}")
                current_player_score += int(money_value[1:])
                used_clues_list.append(clue)
                modules.update_board(money_values_five, categories, category, money_values, money_value)

                # Adds score
                if current_player == player1:
                    player1_score = current_player_score
                    print(f"Your score is now ${current_player_score}")
                else:
                    player2_score = current_player_score
                    print(f"Your score is now ${current_player_score}")

                if modules.get_win(player1, player1_score, player2, player2_score, money_values_five):
                    game_over = True
                    break
                else:
                    continue

            elif modules.check_answer(clue, player_answer, jeopardy_data) is False:
                print(f"{current_player}, your answer was incorrect. You have been deducted {money_value}.")
                current_player_score -= int(money_value[1:])
                used_clues_list.append(clue)
                print(
                    f"\nWell, the answer was...{jeopardy_data['categories'][category][money_value]['answer']}."
                    " Better luck next time.")

                if current_player == player1:
                    player1_score = current_player_score
                    print(f"{player1} score is now ${player1_score}\n")
                else:
                    player2_score = current_player_score
                    print(f"{player2} score is now ${player2_score}\n")

                modules.update_board(money_values_five, categories, category, money_values, money_value)

                if modules.get_win(player1, player1_score, player2, player2_score, money_values_five):
                    game_over = True
                    break
                else:
                    continue
        break  # This break statement is outside of any loop, so it effectively terminates the while loop.

# Run the game
main()
