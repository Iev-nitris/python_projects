from python_projects.dao.transaction.transactionDao import TransactionDao

__author__ = 'Ievgen'

class FileTransactionDao(TransactionDao):

    def __init__(self, defaultTransactionID):
        super(FileTransactionDao, self).__init__(defaultTransactionID)

    def getTransactionByDefID(self):
        pass