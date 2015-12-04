from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['myriad_qubit']
SHARE_PERIOD = 10 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 50 # shares
SPREAD = 30 # blocks
IDENTIFIER = 'fc70135c700a00ee'.decode('hex')
PREFIX = '9472ef181e88efcb'.decode('hex')
P2P_PORT = 5566
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 5567
BOOTSTRAP_ADDRS = 'birdspool.no-ip.org nz.nutty.one mine4free.noip.me tanukifu.ddns.net'.split(' ')
VERSION_CHECK = lambda v: None if 90216 <= v else 'Myriad version too old. Upgrade to 0.9.2.16 or newer!'