import os
import socket
import time

while True:
  hostname = socket.gethostname()
  item = os.environ.get('STORE_ITEM_KEY')
  print ("I'm the shop {} and i sell {}".format(hostname, item))
  time.sleep(1)
