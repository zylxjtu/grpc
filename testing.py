import threading 
import logging

def gfg(): 
    print("GeeksforGeeks\n") 

def run():  
    while True:
        timer = threading.Timer(5.0, gfg) 
        timer.start() 

if __name__ == '__main__':
    # logging.basicConfig()
    run()