__author__ = "EdenRock"
__version__ = "1.0"

import enetsdk as Enet

def ScriptMain(script_data,reserved):
    targets = script_data.GetTargets()
    for target in targets:
        print "Cell Name: ", target.GetName()
        print "Cell Location: ", target.GetLocation()
        print "Cell Azimuth: ", target.GetAzimuth()
        print "Cell DN: ", target.GetDn()
        print "Cell UID: ", target.uid
        print "Cell Technology:", target.technology
        print "Cell IDN: ", target.idn
        print "Cell Band ID: ", target.band_id

        if isinstance(target,Enet.GSMCell) :
            print target.GetName(), " is GSM cell."
            print "NCC: ", target.ncc
            print "BCC: ", target.bcc
            print "LAC: ", target.lac
            print "BCCH Frequency: ", target.bcch_frequency
        elif isinstance(target,Enet.UMTSCell) :
            print target.GetName(), " is UMTS cell."
            print "Scrambling Code: ", target.sc
            print "UARFCN: ", target.uarfcn
        elif isinstance(target,Enet.LTECell) :
            print target.GetName(), " is LTE cell."
            print "PCI: ", target.pci
            print "EARFCN: ", target.earfcn





#=============================================================
# Framework Functions
#=============================================================

def GetEventTypes():
    """Return a list of trigger types"""
    return []


def GetDesc():
    """Return the description of this module"""
    return "This is a hello world SON module."


def GetVersion():
    """Return the current version of this module"""
    return __version__
