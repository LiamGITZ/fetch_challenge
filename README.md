# fetch_challenge
Assumptions / Reasoning:

1)  Transactions can not be negative themselves unless they are spend calls

    This was decided for the fact that if transactions could be negative we may recieve a negative transaction before we recieved the positive value. This would result in the inability to tell valid transactions from invalid ones and would also interfere with the condition of no payer having negative points.

2)  Spend actions do not retroactivley depend on transactions that have not yet been recieved

    If spend actions required the earliest transactions to be used even if they had not been recieved yet then we would need to recalculate spend actions every time we recieved transactions that were older than the ones used in completeing the spend action. This would cause the spend actions to change greatly and change which accounts the money was taken from. From an accounting standpoint this would be a nightmare as any information we have on spend actions could be subject to change in the future and would increase the computational complexity of adding transactions with the need to implement methods such as cahing and saving spending snapshots so that we could efficiently calculate the new corrected spends.
