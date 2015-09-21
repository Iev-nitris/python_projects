__author__ = 'Ievgen'

class TransactionDao(object):

    def __init__(self, defaultTransactionID):
        self.__defaultTransactionID = defaultTransactionID

    def __new__(cls, *args, **kwargs):
        raise StandardError

    def getTransactionByDefID(self):
        raise StandardError

    def getListOfTransacForCurrentDate(self):
        raise StandardError

    def getListOfTransacForDate(self):
        raise StandardError

    def getDictOfTransactions(self):
        raise StandardError