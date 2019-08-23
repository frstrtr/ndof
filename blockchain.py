
"""
genesis = 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks'
blockchain = [1,2,3,4,5,6,7,8,9,10]
print(genesis)
"""

blockchain = [[1]]

def add_value():
    blockchain.append([blockchain[-1],[5.3]])
    print(blockchain)

add_value()
add_value()
add_value()
