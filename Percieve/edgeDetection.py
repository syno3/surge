### importing necessary modules
try:
    import numpy as np ## numpy for matrix calcs
    import cv2 as cv ## for computer vision
    import pandas as pd ## work with some data
    import matplotlib.pyplot as plt## plot images
    import logging## produce error messages
except Exception as e:
    logging.critical('you are missing some modules {}').format(e)

