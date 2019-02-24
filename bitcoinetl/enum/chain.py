class Chain:
    BITCOIN = 'bitcoin'
    BITCOIN_CASH = 'bitcoin_cash'
    BITCOIN_GOLD = 'bitcoin_gold'
    DOGECOIN = 'dogecoin'
    LITECOIN = 'litecoin'
    DASH = 'dash'
    ZCASH = 'zcash'

    ALL = [BITCOIN, BITCOIN_CASH, BITCOIN_GOLD, DOGECOIN, LITECOIN, DASH, ZCASH]
    # Old API doesn't support verbosity for getblock which doesn't allow querying all transactions in a block in 1 go.
    HAVE_OLD_API = [BITCOIN_CASH, DOGECOIN, DASH]
