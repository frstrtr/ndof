
"""
genesis = 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks'
blockchain = [1,2,3,4,5,6,7,8,9,10]
print(genesis)
"""
# Initializing our blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_ammount, last_transaction):
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :transaction_ammount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    if last_transaction == None:
        last_transaction = [1]
    
    #blockchain.append([last_transaction, transaction_ammount])


def mine_block():
    pass


def get_transaction_value():
    """
    Returns the input of the user (a new transaction amount) as a float.
    """
    return float(input('Your transaction ammount please: '))


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-'*20)


def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True

        else:
            is_valid = False

            break
    """ for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        if block[0] == blockchain[block_index - 1]:
            is_valid = True
            block_index += 1
        else:
            is_valid = False
            block_index += 1
            break """
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Output the blockchain blocks')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid Blockchain!')
        waiting_for_input = False
else:
    print('User left!')

print('Done!')
