import atexit
from mtgtools.MtgDB import MtgDB
from os import path

atexit.register(input, 'Press Enter to close...')

database_path = './data/mtgtools_db.fs'
legallist_path = './data/comrade_legallist.txt'
decklist_path = 'DECKLIST_TO_CHECK.txt'

database_setup_success = False
legallist_setup_success = False
decklist_setup_success = False

deck_failed_analysis = False

def is_amount_legal(card, amount):
    if card.type_line.find('Basic Land') != -1:
        return True
    else:
        match card.rarity:
            case 'common':
                return (amount <= 4)
            case 'uncommon':
                return (amount <= 3)
            case 'rare':
                return (amount <= 2)
            case 'mythic':
                return (amount <= 1)
            case _:
                return False

print('--- MTG Comrade Deck Legality Checker ---')

# DATABASE SETUP
print('Database connection', end=' ')
mtg_db = MtgDB(database_path)
if path.getsize(database_path) <= 10000:
    print('established, found missing data. Fetching data:')
    try:
        mtg_db.scryfall_update()
        scryfall_cards = mtg_db.root.scryfall_cards
    except:
        print('Could not fetch data from the Scryfall API! CONNECTION ERROR')
    else:
        database_setup_success = True
        print()
else:
    scryfall_cards = mtg_db.root.scryfall_cards
    database_setup_success = True
    print('established.', end=' ')

# LEGALLIST SETUP
if not database_setup_success:
    print('Legal list loading skipped.', end=' ')
else:
    print('Legal list', end=' ')
    comrade_legal_card_names = []
    try:
        with open(legallist_path) as legal_list:
            for line in legal_list:
                comrade_legal_card_names.append(line.strip())
    except:
        print('missing! ERROR')
    else:
        legallist_setup_success = True
        print('loaded.', end=' ')

# DECKLIST SETUP
if not legallist_setup_success:
    print('Deck list reading skipped.')
else:
    print('Deck list', end=' ')
    maindeck_cards, sidedeck_cards = [], []
    try:
        with open(decklist_path) as decklist:
            reading_mainboard = True
            for line in decklist:
                stripped_line = line.strip()
                if stripped_line == 'SIDEBOARD:':
                    reading_mainboard = False
                elif stripped_line != '':
                    split_line = stripped_line.split()
                    split_line.pop() # remove set number
                    set = split_line.pop().strip("()") # take set name
                    amount = int(split_line.pop(0))
                    name = ' '.join(split_line)
                    if reading_mainboard:
                        maindeck_cards.append((name, amount, set))
                    else:
                        sidedeck_cards.append((name, amount, set))
    except:
        print('missing! ERROR')
    else:
        decklist_setup_success = True
        print('read.')


# --- START OF ANALYSIS ---
if not database_setup_success or not legallist_setup_success or not decklist_setup_success:
    print('Could not start analysis due to the errors above.')
else:
    print('Starting analysis:')
    print()

    # CARD AMOUNT CHECK
    maindeck_card_amount, sidedeck_card_amount = 0, 0
    for (name, amount, set) in maindeck_cards:
        maindeck_card_amount += amount
    for (name, amount, set) in sidedeck_cards:
        sidedeck_card_amount += amount
    if maindeck_card_amount < 60:
        print(f'Maindeck needs to be at least 60 cards! (contains only {maindeck_card_amount} cards)')
        deck_failed_analysis = True
    if maindeck_card_amount > 60:
        print(f"[warning: maindeck contains >60 cards: {maindeck_card_amount} cards (does not affect legality)]")
    if sidedeck_card_amount > 15:
        print(f'Sidedeck maximum is 15 cards! (contains {sidedeck_card_amount} cards)')
        deck_failed_analysis = True
    if sidedeck_card_amount < 15 and sidedeck_card_amount != 0:
        print(f"(warning: sidedeck should contain 0 or 15 cards, {sidedeck_card_amount} is technically not allowed)")

    # ILLEGAL CARD CHECK
    # merge maindeck/sidedeck into combineddeck
    combineddeck_cards = maindeck_cards.copy()
    for (name, amount, set) in sidedeck_cards:
        found = False
        for index, (combineddeck_card_name, combineddeck_card_amount, combineddeck_card_set) in enumerate(combineddeck_cards):
            if name == combineddeck_card_name:
                combineddeck_cards[index] = (combineddeck_card_name, combineddeck_card_amount + amount, combineddeck_card_set)
                found = True
        if found == False:
            combineddeck_cards.append((name, amount, set))

    illegal_cards_unique, illegal_cards_cumulative = 0, 0
    for (card_name, card_amount, card_set) in combineddeck_cards:
        if card_name not in comrade_legal_card_names:
            print(f'{card_name} is NOT LEGAL in the Comrade format! (used {card_amount}x)')
            illegal_cards_unique += 1
            illegal_cards_cumulative += card_amount
        else:
            scryfall_card = scryfall_cards.where_exactly(name=card_name, set=card_set)[0]
            if not is_amount_legal(scryfall_card, card_amount):
                print(f"{card_name} is used in an ILLEGAL AMOUNT for its rarity! ({scryfall_card.rarity}, used {card_amount}x)")
                illegal_cards_unique += 1
                illegal_cards_cumulative += card_amount
    if illegal_cards_unique == 0:
        print("All cards seem to be legal in names and amounts.")
    elif illegal_cards_unique == 1:
        deck_failed_analysis = True
    else:
        print(f'Found {illegal_cards_unique} different problem cards, see above! ({illegal_cards_cumulative} when considering amounts)')
        deck_failed_analysis = True

    # VERDICT PRINTOUT
    print()
    if deck_failed_analysis == False:
        print("Analysis finished, verdict: LEGAL. You're good to go. :)")
    else:
        print("Analysis finished, verdict: ILLEGAL! Back to the drawing board you go. :(")