
# A transaction is possibly invalid if:

# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.

# Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

#transactions = ["alice,20,800,mtv","alice,50,100,beijing"]


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        inv = []
        tmp = []
        for i in transactions:
            j = i.split(",")
            if int(j[2]) > 1000:
                inv.append(i)
            tmp.append(i.split(","))
        for i in tmp:
            for j in tmp:
                if i[0] == j[0] and abs(int(i[1]) - int(j[1])) <= 60 and i[3] != j[3]:
                    a = ",".join(i)
                    if a not in inv:
                        inv.append(a)
        return inv
