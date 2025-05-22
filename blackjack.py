import random

def calcDeckVal(cards):
    sum = 0
    for card in cards:
        sum+=card
    # Ace calculator
    for card in cards:
        if sum>21 and card==11:
            sum-=10
    return sum

def printResult(players, winners):
    print("-"*100)
    print(f"{'Black Jack'.upper():^{100}}")
    print("-"*100)
    print(f"{'Player Name':<{33}} {'Cards':<{33}} {'Score':<{33}}")
    print('-'*100)
    #players
    for player in players: print(f"{str(player[0]):<{33}} {str(player[1][0]):<{33}} {str(player[1][1]):<{33}}")
    print('-'*100)
    #winners
    print(winners)
    print('-'*100)


def getWinScore(players):
    winners = []
    winScore = 0
    # check for black jack winners
    
    for player in players:
        if player[1][1] == 'Win':
            winners.append(player[0])
    if len(winners) == 0: # if no black jacks
        for player in players:
            if type(player[1][1]) != str:
                if player[1][1] > winScore:
                    winScore = player[1][1]
        for player in players:
            if player[1][1] == winScore:
                winners.append(player[0])
    # Win conditions
    # one winner            
    if len(winners) == 1:
        if "player1" in winners: #if player won
            winners.remove("player1")
            if winScore > 0: printResult(players,f"Congrats you were the closest to black Jack, your cards were {players[4][1][0]} with sum {winScore}")
            if winScore == 0: printResult("Congrats you were the only one to get Black Jack")
        else: #if player lost
            if winScore > 0 :printResult(players,f"Better luck next time {winners[0]} Won with a score of {winScore}; Your score was {players[4][1][1]} with these cards {players[4][1][0]}")
            if winScore == 0: printResult(players,f"Better luck next time {winners[0]} was the only one to get Black Jack")
    # more than one winner
    if len(winners) > 1:
        if "player1" in winners:
                winners.remove("player1")
                if winScore > 0: printResult(players,f"congrats you tied with {winners} with a score of {winScore}")
                if winScore == 0: printResult(players,f"congrats you and {winners} got blackjack")
        else:
                if winScore > 0: printResult(players,f"Better luck next time {winners} were the closest to Black Jack with a score of {winScore}")
                if winScore == 0: printResult(players,f"Better luck next time {winners[0]} was the closest to Black Jack with a score of {winScore}")

def gameResult(decision,cards,players):
    score = calcDeckVal(cards)
    if(decision == "HIT"):
        cards.append(random.randint(1,11))
        score = calcDeckVal(cards)
        if score > 21:
            players.append(["player1", [cards, 'Bust']])
            getWinScore(players)
        elif score == 21:
            players.append(["player1", [cards, 'Win']])
            getWinScore(players)
        else:
            gameResult(input(f"your cards are {cards}. Hit or Stand?").upper(), cards, players)
    elif(decision == "STAND"):
        players.append(["player1", [cards, score]])
        getWinScore(players)
    else:
        print("wrong spelling try again")

def npcResult(cards, numHit):
    if(numHit != 0):
        for x in range(0,numHit):
            cards.append(random.randint(1,11))
    score = calcDeckVal(cards)
    if score > 21:
        return cards, 'Bust'
    elif score == 21:
        return cards, 'Win'
    else: return cards, score

def npc(numHit):
    c1 = random.randint(1,11)
    c2 = random.randint(1,11)
    cards = [c1,c2]
    return npcResult(cards, numHit)

#assign random number corresponding to times player hits
npc1 = random.randint(0,3)
npc2 = random.randint(0,3)
npc3 = random.randint(0,3)
npc4 = random.randint(0,3)
#make a list that includes the players name with their cards
players = [['dealer',npc(npc1)],['npc2', npc(npc2)],['npc3', npc(npc3)],['npc4', npc(npc4)]]

c1 = random.randint(1,11)
c2 = random.randint(1,11)
cards = [c1,c2]
decision = input(f"your cards are {cards}. Hit or Stand?").upper()
gameResult(decision, cards, players)