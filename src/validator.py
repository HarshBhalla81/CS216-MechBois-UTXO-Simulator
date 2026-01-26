from transaction import transaction
from utxo_manager import UTXOManager
from mempool import MEMPOOL
def is_Valid_transaction(transaction) :
    utxo = UTXOManager
    TX_ID = transaction["tx_id"]
    Inputs = transaction["inputs"]
    Outputs = transaction["outputs"]

    #so lets assume for now that there exist a mempool which will have a sort of dictionary like appearace
    #the mempool will store some of the uncofirmed transaction in the form of key value pair
    #the key will be (tx_id , index) and the corresponding value will be (amount , owner)
    #so for this transaction to be valid all the inputs must not exist in the mempool

    for inp in Inputs:
        prev_tx = inp["prev_tx"]
        index = inp["index"]

        if MEMPOOL.exists(prev_tx, index):
            print("Invalid: input UTXO is already used in mempool")
            return False
    
    seen_inputs = set()
    sum_inputs = 0

    for inp in Inputs:
        prev_tx = inp["prev_tx"]
        index = inp["index"]
        claimed_owner = inp["owner"]

        # Check UTXO exists
        if not UTXOManager.exists(prev_tx, index):
            print("Invalid: referenced UTXO does not exist")
            return False

        # Fetch UTXO data
        amount, real_owner = UTXOManager.utxo_set[(prev_tx, index)]

        # Check ownership
        if claimed_owner != real_owner:
            print("Invalid: input owner does not match UTXO owner")
            return False

        # Check double spend within same transaction
        if (prev_tx, index) in seen_inputs:
            print("Invalid: double spending within transaction")
            return False

        seen_inputs.add((prev_tx, index))
        sum_inputs += amount
    
    sum_outputs = 0
    # 3. Validate outputs
    for out in Outputs:
        amount = out["amount"]

        if amount < 0:
            print("Invalid: negative output amount")
            return False

        sum_outputs += amount

    if sum_inputs < sum_outputs:
        print("Invalid: output amount exceeds input amount")
        return False
    
    print("Transaction is valid")
    return True