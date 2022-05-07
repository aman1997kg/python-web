from peewee import *
from peewee import SqliteDatabase

db: SqliteDatabase = SqliteDatabase('tourist.db')

class BaseClass(Model):
    id = PrimaryKeyField(
        unique=True,
        index=True
    )

    company  = CharField(
        max_length=255,
        index=True
    )


class Inner_flights(BaseClass):

    from_region = CharField(
        max_length=255,
        index=True,
        default='Airport',
        help_text='Бул жерге уча турган жерди жазасыз.'
    )

    to_destionation =  CharField(
        max_length=255,
        index=True,
        default='Airport',
        help_text='Бул жерге учуп бара турган жерди жаз.'
    )

    AIR_COMPANY_NAME = (
        (1, 'Airobus'),
        (2, 'Air Manas'),
    )

    quantity = IntegerField(
        null=True,
        constraints=[Check('quantity >= 0')],
        help_text='Жүргүнчүлөрдүн санын жаз.'
    )

    class Meta:
        database = db
        order_by = 'id'
        table_db = 'Ички учуу'


class Outer_flights(BaseClass):

    from_country = CharField(
        max_length=255,
        index=True,
        default='Мамлекет',
        help_text='Бул жерге уча турган мамлекетти жазасыз.'
    )

    to_country =  CharField(
        max_length=255,
        index=True,
        default='Мамлекет',
        help_text='Бул жерге учуп бара турган мамлекетти жаз.'
    )

    TYPE = (
        (1, 'Жүк ташуучу'),
        (2, 'Киши ташуучу'),
    )

    flight_type = CharField(
        max_length=255,
        choices=TYPE,
        help_text='Учуу тиби'
    )

    neighbors = IntegerField(
        null=True,
        help_text='Канча мамлекетти аралайт'
    )

    class Meta:
        database = db
        order_by = 'id'
        table_db = 'Сырткы учуу'