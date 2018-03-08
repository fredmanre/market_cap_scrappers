# import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
import psyycopg2


def market_caps():
    """
    Script for get values in official pages over markets and current supply.
    """