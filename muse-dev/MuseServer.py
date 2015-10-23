from liblo import *

import sys
import time


class MuseServer(ServerThread):
    #listen for messages on port 5000
    def __init__(self):
        ServerThread.__init__(self, 5000)

    @make_method('/muse/elements/blink', 'i')
    def blink_callback(self, path, args):
        blink = args[0]
        if blink == 1:
            print "Blink"

    @make_method('/muse/elements/jaw_clench', 'i')
    def jaw_callback(self, path, args):
        jaw_clench = args[0]
        if jaw_clench == 1:
            print "Clenched Jaw"
"""
    #receive accelrometer data
    @make_method('/muse/acc', 'fff')
    def acc_callback(self, path, args):
        acc_x, acc_y, acc_z = args
        print "%s %f %f %f" % (path, acc_x, acc_y, acc_z)
"""
"""
    #receive EEG data
    @make_method('/muse/eeg', 'ffff')
    def eeg_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)
"""
"""
    #handle unexpected messages
    @make_method(None, None)
    def fallback(self, path, args, types, src):
        print "Unknown message \
        \n\t Source: '%s' \
        \n\t Address: '%s' \
        \n\t Types: '%s ' \
        \n\t Payload: '%s'" \
        % (src.url, path, types, args)
"""
