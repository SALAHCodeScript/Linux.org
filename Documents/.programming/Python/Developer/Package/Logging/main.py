#!/usr/bin/python3
import logging

# Configure logging to write to a file
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Log some messages
logging.debug('Debug information')
logging.info('General information')
logging.warning('Warning message')
logging.error('Error occurred')
logging.critical('Critical issue')
