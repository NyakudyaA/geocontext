import sys
import psycopg2
from django.db import models


# Create your models here.

class CollectionName(models.Model):

    @staticmethod
    def db_connection(db_name, db_user, db_host, db_pass, db_port, latitude, longitude):

        try:
            conn = psycopg2.connect("dbname=%s user=%s host=%s password='%s'\
             port=%s" % (db_name, db_user, db_host, db_pass, db_port))
        except psycopg2.OperationalError as e:
            print(e)
            sys.exit(1)
        cursor = conn.cursor()
        cursor.callproc('finder', [latitude, longitude])
        results = cursor.fetchall()
        cursor.close()
        return [CollectionName(*row) for row in results]
