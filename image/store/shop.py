import threading
import os
import socket

def print_advertising():
  hostname = socket.gethostname()
  item = os.environ.get('STORE_ITEM_KEY')
  threading.Timer(1.0, print_advertising).start()
  print ("I'm the shop {} and i sell {}".format(hostname, item))

print_advertising()
