from django.test import TestCase
from store.settings import base


class SettingsImportCase(TestCase):
    def test_db_url_is_correct(self):
        db_url = 'postgres://admin-user:13sd1d2dsc3cd2c@?*&^$@127.0.0.1:5432/sql_db'
        self.assertTrue(base.check_db_url(db_url))

        db_url = 'postgres://n3d2sl.-_s4n432cln22as1232:kjsdhfksd@alcasnlkjsdnkljnsd.com:0000/l4k4an4c4444l1231skdn-_as51da321'
        self.assertTrue(base.check_db_url(db_url))

        db_url = 'postgres://adminuser:kbkjbm3$#^&@$*#@localhost:3626/cmbdsacdsbncsdc'
        self.assertTrue(base.check_db_url(db_url))

        db_url = 'postgres://:@:/'
        self.assertFalse(base.check_db_url(db_url))

        db_url = ''
        self.assertFalse(base.check_db_url(db_url))

        db_url = 'postgres://USER:PASSWORD@HOST:PORT/'
        self.assertFalse(base.check_db_url(db_url))

        db_url = 'postgres://USER:PASSWORD@HOST:/NAME'
        self.assertTrue(base.check_db_url(db_url))

        db_url = 'postgres://USER:PASSWORD@:PORT/NAME'
        self.assertFalse(base.check_db_url(db_url))

        db_url = 'postgres://USER:@HOST:PORT/NAME'
        self.assertFalse(base.check_db_url(db_url))

        db_url = 'postgres://:PASSWORD@HOST:PORT/NAME'
        self.assertFalse(base.check_db_url(db_url))

        db_url = 'postgres://USER:PASSWORD@HOST:0212154/NAME'
        self.assertFalse(base.check_db_url(db_url))

        db_url = 'postgres://USER:PASSWORD@lsjlkdsj-_./:/NAME'
        self.assertTrue(base.check_db_url(db_url))

        db_url = 'pstgres://USER:PASSWORD@HOST:/NAME'
        self.assertFalse(base.check_db_url(db_url))

        db_url = 'pstgresUSERPASSWORDHOSTNAME'
        self.assertFalse(base.check_db_url(db_url))
