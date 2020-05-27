from dbmodel.connection import db_mongodb, db_mysql, db_redis
import config


class BaseModel(object):

    redis_db = db_redis.Connection(host=config.REDIS_HOST,port=config.REDIS_PORT)

    db_mongodb = db_mongodb.Connection(host=config.MONGO_HOST, port=config.MONGO_PORT, database=config.MONGO_DATABASE)

    db_mysql = db_mysql.Connection(host=config.MYSQL_HOST, port=config.MYSQL_PORT, user=config.MYSQL_USER, password=config.MYSQL_PASSWORD, database=config.MYSQL_DATEBASE)

    def __init__(self):

        self.redis_time = 60*60*24
        self.redis_key_prefix = 'xxx_'

    def produce_redis_keys(self, prefix, id):
        redis_key = self.redis_key_prefix + str(prefix) + '_' + str(id)
        return redis_key