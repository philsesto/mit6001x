def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    options = ['n', 'r', 'e']
    options2 = ['u', 'c']
    gameRunning = True
    handsDealt = 0

    while gameRunning:
        success = False
        while not success:
            try:
                gameFlow = input('Enter n to deal a new hand, r to replay the last hand, or e to end the game: ')
                if gameFlow not in options:
                    raise IndexError
                assert not (handsDealt == 0 and gameFlow == 'r')
                success = True
            except AssertionError: # handsDealt == 0 and gameFlow == 'r'
                print('You have not played a hand yet. Please play a new hand first\n')
                continue
            except IndexError: # user input something else
                print('Invalid command.')
                continue
        
        if gameFlow == 'e':
            gameRunning = False
            break
        else:
            success2 = False
            while not success2:
                try:
                    playerSelect = input('\nEnter u to have yourself play, c to have the computer play: ')
                    print()
                    assert playerSelect in options2
                    success2 = True
                except AssertionError:
                    print('Invalid command.')
                    continue

        if gameFlow == 'n':
            hand = dealHand(HAND_SIZE)
            handsDealt += 1
            if playerSelect =='c':
                compPlayHand(hand, wordList, HAND_SIZE)
            else:
                playHand(hand, wordList, HAND_SIZE)
        elif gameFlow == 'r':
            if playerSelect == 'c':
                compPlayHand(hand, wordList, HAND_SIZE)
            else:
                playHand(hand, wordList, HAND_SIZE)