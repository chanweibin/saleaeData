from saleae import automation
import saleae
import os
import os.path
from datetime import datetime
import time

s = saleae.Saleae()

while not (s.is_analyzer_complete):
    print("Waiting for Saleae to finish analyzing...")
    time.sleep(10)
    
s.export_analyzer(1, "C:/Users/wc896667/Downloads/1.csv", True, False)