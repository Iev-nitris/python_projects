from python_projects.dao.fileDaoFactory import FileDaoFactory
from python_projects.dao.sqlDaoFactory import SQLDaoFactory
from python_projects.dao.excelDaoFactory import ExcelDaoFactory

__author__ = 'Ievgen'


class DaoFactory(object):
    FILE = 1
    SQL = 2
    EXCEL = 3

    def __new__(cls, *args, **kwargs):
        raise StandardError

    def getTransactionDao(self):
        raise StandardError

    def getTypeCheckDao(self):
        raise StandardError

    def getMandatoryDao(self):
        raise StandardError

    def getCpartyDao(self):
        raise StandardError

    def getCpartyMapDao(self):
        raise StandardError

    def getCpartyHierarchyDao(self):
        raise StandardError

    @staticmethod
    def getDaoFactory(whichFactory=0):
        if whichFactory == 1:
            return FileDaoFactory()
        elif whichFactory == 2:
            return SQLDaoFactory()
        elif whichFactory == 3:
            return ExcelDaoFactory()
        else:
            return None