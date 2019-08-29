import unittest
import logger
from logger import Logger


''' Target dummy class '''
class Target:
    def set_text(self,text):
        self.text = text
    
    def get_text(self):
        return self.text
        

class LoggerTest(unittest.TestCase):   
    ''' Tests logger.info function '''
    def test_info(self):
        target = Target()
        log = Logger(target.set_text)
        log.info("Info Message")
        self.assertEqual("[INFO] Info Message", target.get_text())
                
    
    def test_error(self):
        ''' Tests logger.error function '''
        target = Target()
        log = Logger(target.set_text)
        log.error("Error Message")
        self.assertEqual("[WARNING] Error Message", target.get_text())

if __name__ == '__main__':
    unittest.main()