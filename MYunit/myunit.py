import logging
import unittest

from Mydriver.MYdriver import my_driver
from logging import config

File_config = '../config/log.conf'
config.fileConfig(File_config)
logger = logging.getLogger()

class Myunit(unittest.TestCase):
    def setUp(self):
        self.n_dirver = my_driver()
        logger.info('_______w无图形化界面获取驱动_______')
    def tearDown(self):
        self.n_dirver.quit()
        logger.info('_______w无图形化界面关闭驱动_______')
if __name__ == '__main__':
    Myunit.main()