# TROJAN HORSE

## Idea:
It is a disguised software into a software such as a game. Differently from a virus, the trojan horse is not meant to cause any damage. Indeed, it fetch some kind of data from the infected computer and sends it to the hacker.

## Note:
A real world trojan horse would be implemented with a lower lever, more disguisable, thus compiled language such as C++.
However, for the purpose of learning and understanding the internal mechanism, I used python.

## How to Reproduce:
1. clone repo
2. adjust ip address both in server.py and spyware.py to your own
3. from terminal #1 execute server.py
4. from terminal #2 execute main.py
    * the "Guess a Number" game will be prompted. Behind the curtains a connection is established between server and spyware (it runs on a different thread respect to the game)
5. from server's terminal try these commands:
    * infect - will print in the client terminal a quircky message
    * chat on - will enable the possibility to send any custom text message in the client terminal
    * chat off - return to default mode