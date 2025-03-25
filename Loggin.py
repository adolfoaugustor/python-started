#loggin
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(levelname)s %(asctime)s: %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S'
)

logger = logging.StreamHandler()
logging.getLogger('').addHandler(logger)

logging.debug('isso é um debug')
logging.info('isso é um info')
logging.warning('isso é um warning')
logging.error('isso é um error')
logging.critical('isso é um critical')