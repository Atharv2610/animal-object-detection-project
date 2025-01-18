from animal_detection.logger import logging
from animal_detection.exception import objectException
import sys
#logging.info("Welcome to the project")

try:
    a= 7/'9'
except Exception as e:
    raise objectException(e,sys)from e