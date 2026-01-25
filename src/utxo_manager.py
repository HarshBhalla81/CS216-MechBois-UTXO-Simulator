class UTXOManager :
    def __init__(self) :
        self.utxo_set = {}

    # Each tx_id , index map to a transaction amount and the owner of the utxo
    # The index represent one of the outputs of a transaction since there may be many smaller transaction corresponding to a utxo
    # Each smaller transaction is represented by the index indicating the owner to whom the amount was paid
    def add_utxo(self , tx_id , index , amount , owner) :
        self.utxo_set[tx_id , index] = amount , owner

    # the utxo_set tries to find the key : (tx_id , index) in the dictionary and deletes the (key , value) pair using delete keyword
    def remove_utxo(self , tx_id , index) :
        del self.utxo_set[tx_id , index]

    # We initialize balance variable which will store the balance for a parrticular owner
    # We iterate over the utxo_set and check whether the transaction owner(tx_owner) for (tx_id , index) key is the required owner or not
    # If yes we add the amount corresponding to that transaction into the ownere balance variable
    # At last we return the balance
    def get_balance(self , owner) :
        balance = 0
        amount = 0
        tx_owner = ""
        for tx_id , index in self.utxo_set :
            amount , tx_owner = self.utxo_setcd[tx_id , index]
            if(tx_owner == owner) :
                balance += amount
        return balance
    
    # To check if the tx_id , index exist or not we try to find the key in the utxo set using 'in' keyword
    def exists(self , tx_id , index) :
        if( (tx_id , index) in self.utxo_set) :
            return True
        else :
            return False
    
    # We search for the required owner in the utxo_set and then append the pair of tx_id , index in the list
    # After iterating we return the list of utxos_owned
    def get_utxos_for_owner(self , owner) :
        utxos_owned = []
        for tx_id , index in self.utxo_set :
            amt , tx_owner = self.utxo_set[tx_id , index]
            if(owner == tx_owner) :
                utxos_owned.append((tx_id , index))
        return utxos_owned
    