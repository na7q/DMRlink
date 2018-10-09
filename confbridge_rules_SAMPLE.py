'''
THIS EXAMPLE WILL NOT WORK AS IT IS - YOU MUST SPECIFY YOUR OWN VALUES!!!

This file is organized around the "Conference Bridges" that you wish to use. If you're a c-Bridge
person, think of these as "bridge groups". You might also liken them to a "reflector". If a particular
system is "ACTIVE" on a particular conference bridge, any traffic from that system will be sent
to any other system that is active on the bridge as well. This is not an "end to end" method, because
each system must independently be activated on the bridge.

The first level (e.g. "WORLDWIDE" or "STATEWIDE" in the examples) is the name of the conference
bridge. This is any arbitrary ASCII text string you want to use. Under each conference bridge
definition are the following items -- one line for each System as defined in the main DMRlink
configuration file.

    * SYSTEM - The name of the sytem as listed in the main dmrlink configuration file (e.g.dmrlink.cfg)
        This MUST be the exact same name and case as in the main config file!!!
    * TS - Timeslot used for matching traffic to this confernce bridge
    * TGID - Talkgroup ID used for matching traffic to this conference bridge
    * ON and OFF are LISTS of Talkgroup IDs used to trigger this system off and on. Even if you
        only want one (as shown in the ON example), it has to be in list format. None can be
        handled with an empty list, such as " 'ON': [] ".
    * RESET is a list of Talkgroup IDs that, in addition to the ON and OFF lists will cause a running
        timer to be reset. This is useful   if you are using different TGIDs for voice traffic than
        triggering. If you are not, there is NO NEED to use this feature.
    * TO_TYPE is timeout type. If you want to use timers, ON means when it's turned on, it will
        turn off afer the timout period and OFF means it will turn back on after the timout
        period. If you don't want to use timers, set it to anything else, but 'NONE' might be
        a good value for documentation!
    * TIMOUT is a value in minutes for the timout timer. It MUST have a value. No,
	I won't make it 'seconds', so don't ask. Timers are performance "expense".

'''

# CONFIGURATION ITEMS SPECIFICALLY FOR confbridge.py
#
# REPORT:
#     True or False. True if you want to write a pickle file of the current rule file
#     state. This is useful (and necessary) for reporting features to be active.
#     The path follows the reporting path in the main dmrlink.cfg file.
BRIDGE_CONF = {
    'REPORT': True,
    }

# TRUNK IPSC Systems -- trunk bypasses the contention handler and always transmits traffic
#
# This is a python LIST data type. It needs to be here, but just leave it empty if not used.
# The contents are a quoted, comma separated list of IPSC systems that are traffic trunks.
# Example: TRUNKS = ['MASTER-1', 'CLIENT-2']
TRUNKS = []

BRIDGES = {
    'WORLDWIDE': [
            {'SYSTEM': 'MASTER-1',    'TS': 1, 'TGID': 1,    'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'ON',   'ON': [2,], 'OFF': [9,10], 'RESET': []},
            {'SYSTEM': 'CLIENT-1',    'TS': 1, 'TGID': 3100, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'ON',   'ON': [2,], 'OFF': [9,10], 'RESET': []}
        ],
    'ENGLISH': [
            {'SYSTEM': 'MASTER-1',    'TS': 1, 'TGID': 13,   'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE', 'ON': [3,], 'OFF': [8,10], 'RESET': []},
            {'SYSTEM': 'CLIENT-2',    'TS': 1, 'TGID': 13,   'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE', 'ON': [3,], 'OFF': [8,10], 'RESET': []}
        ],
    'STATEWIDE': [
            {'SYSTEM': 'MASTER-1',    'TS': 2, 'TGID': 3129, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE', 'ON': [4,], 'OFF': [7,10], 'RESET': []},
            {'SYSTEM': 'CLIENT-2',    'TS': 2, 'TGID': 3129, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE', 'ON': [4,], 'OFF': [7,10], 'RESET': []}
        ]
}

if __name__ == '__main__':
    from pprint import pprint
    pprint(BRIDGES)
