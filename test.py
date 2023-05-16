import time

def decorator(function):
  def wraper():
    print('I will say hello to you winthin 3 seconds')
    time.sleep(3)
    function()
    time.sleep(1)
    print('I did say hello')
  return wraper

@decorator
def hello():
  print("Hello")

hello()