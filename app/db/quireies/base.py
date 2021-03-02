from sqlalchemy.orm import Query


class BaseQuery(Query):
    def __init__(self, *args, **kwargs):
        super(BaseQuery, self).__init__(*args, **kwargs)
