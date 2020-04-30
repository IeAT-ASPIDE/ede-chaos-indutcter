import logging
from logging.handlers import RotatingFileHandler
import os
# Logging
log = logging.getLogger("eci_control")
log.setLevel(logging.INFO)
log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))

handler = RotatingFileHandler(os.path.join(log_dir, "eci-control_out.log"), maxBytes=100000000, backupCount=5)
form = "%(created)f %(filename)13s:%(lineno)-4d\t%(levelname)-8s %(message)s"
# form2 = '[%(created)f]:[%(name)s]:[%(levelname)s] - %(message)s'
formatter = logging.Formatter(form)
handler.setFormatter(formatter)
consoleHandler = logging.StreamHandler()
log.addHandler(handler)
log.addHandler(consoleHandler)



