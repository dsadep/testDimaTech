from app.dao.base import BaseDAO
from app.payments.models import Transactions


class TransactionsDAO(BaseDAO):
    model = Transactions