from python_projects.dao.daoFactory import DaoFactory

__author__ = 'Ievgen'

class SQLDaoFactory(DaoFactory):
    CONNECTION_STRING = ""
    SDS_CONNECTION_STRING = ""
    SSO = ""
    LOGIN = ""
    PASS = ""

    @staticmethod
    def getConnection(self):
        pass

    def getTransactionDao(self):
        pass

    def getCpartyDao(self):
        pass

    def getCpartyMapDao(self):
        pass

    def getCpartyHierarchyDao(self):
        pass