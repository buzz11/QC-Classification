from clustering import run as run1
from pca import run as run2
from training import run as run3
from predict import run as run4
import os
import logging
from datetime import datetime
import random
random.seed(11)

'''
load data, cluster, decompose, train
'''

def make_dirs():
    a = os.path.join('..','data', 'clusters')
    b = os.path.join('..','data', 'models', 'clusters')
    c = os.path.join('..','data', 'models', 'pca')
    d = os.path.join('..','data', 'pca')
    e = os.path.join('..','data', 'pca_map')
    f = os.path.join('..','data', 'logs')
    dirs = [a,b,c,d,e,f]
    for d in dirs:
        if not os.path.isdir(d):
            os.makedirs(d)

make_dirs()

dt_path = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join('..','data', 'logs', dt_path+'.log'), 'a')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter.datefmt = '%m/%d/%Y %I:%M:%S %p'
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_formatter = logging.Formatter('%(name)s - %(message)s')
stream_handler.setFormatter(stream_formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.info('STARTING - clustering.py')
run1(logger)
logger.info('STARTING - pca.py')
run2(logger)
logger.info('STARTING - training.py')
run3(logger)
logger.info('STARTING - predict.py')
run4(logger)
