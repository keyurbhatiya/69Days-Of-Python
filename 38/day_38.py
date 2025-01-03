################################## Day 38: 69 Days of Python #####################################

# slot machine game using random module
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMNS = 3

symbol_count = {
    "A" : 2 ,
    "B" : 4 ,
    "C" : 6 ,
    "D" : 8
}

symbol_value = {
    "A" : 5 ,
    "B" : 4 ,
    "C" : 3 ,
    "D" : 2
}


def check_winning(columns , lines , bet , values) :
    winnings = 0
    winning_lines = []
    for line in range (lines) :
        symbol = columns[0][line]
        for column in columns :
            symbol_to_check = column[line]
            if symbol != symbol_to_check :
                break
        else :
            winnings += values[symbol] * bet
            winning_lines.append (line + 1)

    return winnings , winning_lines


def get_slot_machine_spin(rows , cols , symbols) :
    all_symbols = []
    for symbol , count in symbols.items ( ) :
        all_symbols.extend ([symbol] * count)

    columns = []
    for _ in range (cols) :
        column = random.sample (all_symbols , rows)  # Use random.sample to avoid removing elements manually
        columns.append (column)

    return columns


def print_slot_machine(columns) :
    for row in range (len (columns[0])) :
        for i , column in enumerate (columns) :
            if i != len (columns) - 1 :
                print (column[row] , end = " | ")
            else :
                print (column[row] , end = "")
        print ( )


def deposit() :
    while True :
        amount = input ("What would you like to deposit? : ")
        if amount.isdigit ( ) :
            amount = int (amount)
            if amount > 0 :
                return amount
            else :
                print ("Amount must be greater than 0.")
        else :
            print ("Please enter a number.")


def get_number_of_lines() :
    while True :
        lines = input (f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit ( ) :
            lines = int (lines)
            if 1 <= lines <= MAX_LINES :
                return lines
            else :
                print (f"Enter a valid number of lines (1-{MAX_LINES}).")
        else :
            print ("Please enter a number.")


def get_bet() :
    while True :
        amount = input (f"What would you like to bet on each line (between {MIN_BET} - {MAX_BET})? : ")
        if amount.isdigit ( ) :
            amount = int (amount)
            if MIN_BET <= amount <= MAX_BET :
                return amount
            else :
                print (f"Amount must be between {MIN_BET} and {MAX_BET}.")
        else :
            print ("Please enter a number.")


def spin(balance) :
    lines = get_number_of_lines ( )
    while True :
        bet = get_bet ( )
        total_bet = bet * lines
        if total_bet > balance :
            print (f"You do not have enough balance to bet that amount. Your current balance is: {balance}")
        else :
            break
    print (f"You are betting {bet} on {lines} lines. Total bet is: {total_bet}")

    slots = get_slot_machine_spin (ROWS , COLUMNS , symbol_count)
    print_slot_machine (slots)
    winnings , winnings_lines = check_winning (slots , lines , bet , symbol_value)
    print (f"You won {winnings}.")
    if winnings_lines :
        print ("You won on lines:" , *winnings_lines)
    return winnings - total_bet


def main() :
    balance = deposit ( )
    while True :
        print (f"Current balance: {balance}")
        play = input ("Press Enter to play (q to quit): ")
        if play.lower ( ) == 'q' :
            break
        balance += spin (balance)
    print (f"You left with {balance}")


if __name__ == "__main__" :
    main ( )
