import time
import time

from MuseServer import MuseServer

try:
    server = MuseServer()
    print "Started Muse Server"
except ServerError, err:
    print str(err)
    sys.exit()


server.start()

if __name__ == "__main__":
    while 1:
        time.sleep(1)
