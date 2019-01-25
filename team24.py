####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Jonathan Winkleys Team' # Only 10 chars displayed.
strategy_name = 'Weighted Betray'
strategy_description = 'Start with colluding. After that turn their history into a percent to determine if choosing c or b'

import random

def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history) == 0:
        return 'c' #if first turn collude
    else:
        #set default values
        weight = 0 
        betrays = 0
        their_length = 0
        for round in range(len(their_history)):
            if their_history[round] == 'b':
                betrays += 1 #add to variable if for each time they have betrayed if ever
            their_length += 1 #keeps track of how long their_history is
        weight = int((betrays/their_length)*100) #calculates weight as an int
        if their_length <= 10:
            weight -= 50 #if first ten turns subtract 50 from weight
        if weight < 0:
            weight = 0 #makes sure weight is not below 0
        if weight >= random.randint(1, 100): #decides wether to betray or collude
            return 'b'
        else:
            return 'c'
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, depending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print ('Test passed')
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             