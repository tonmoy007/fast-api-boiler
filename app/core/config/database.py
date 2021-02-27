from app.core.config import env


class DB:
    driver: str = env('DB_CONNECTION')
    username: str = env('DB_USERNAME')
    password: str = env('DB_PASSWORD')
    hostname: str = env('DB_HOST')
    port: int = int(env('DB_PORT'))
    database: str = env('DB_DATABASE')

    @staticmethod
    def to_string():
        return DB.driver + '://' + DB.username + ':' + DB.password + '@' + \
               DB.hostname + ':' + str(DB.port) + '/' + DB.database

    @staticmethod
    def to_raw_connection_string():
        return DB.driver + '://' + DB.username + ':' + DB.password + '@' + \
               DB.hostname + ':' + str(DB.port)
