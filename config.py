apic = {'url': 'https://__APIC_URL_OR_IP__', 'user': 'admin', 'password': '__APIC_USER_PASSWORD__'}

changeIdDict = {}
lastChangeId = 1000

fabricNodes = {'pods': {
    1: [
        {'name': 'leaf1101_i08-n93180-01', 'serial': '__SERIAL__', 'nodeId': '1101', 'addr': '172.16.0.188/22', 'v6Addr': '::', 'rr': False },
        {'name': 'leaf1102_i08-n93180-02', 'serial': '__SERIAL__', 'nodeId': '1102', 'addr': '172.16.0.189/22', 'v6Addr': '::', 'rr': False },
        {'name': 'leaf1103_i08-n93108-01', 'serial': '__SERIAL__', 'nodeId': '1103', 'addr': '172.16.0.207/22', 'v6Addr': '::', 'rr': False },
        {'name': 'leaf1104_i07-n93108-01', 'serial': '__SERIAL__', 'nodeId': '1104', 'addr': '172.16.0.206/22', 'v6Addr': '::', 'rr': False },
        {
            'name': 'spine1201_i08-n9336-01',
            'serial': '__SERIAL__',
            'nodeId': '1201',
            'addr': '172.16.0.181/22',
            'v6Addr': '::',
            'rr': True,
            'l3Out': {
                'routerId': '11.11.11.11',
                'interfaces': [
                    {'name': 'eth1/35', 'addr': '201.1.1.1/30'},
                    {'name': 'eth1/36', 'addr': '201.1.1.5/30'}
                ]
            }
        },
        {
            'name': 'spine1202_i08-n9336-02',
            'serial': '__SERIAL__',
            'nodeId': '1202',
            'addr': '172.16.0.182/22',
            'v6Addr': '::',
            'rr': True,
            'l3Out' :{
                'routerId': '12.12.12.12',
                'interfaces': [
                    {'name': 'eth1/35', 'addr': '201.1.1.9/30'},
                    {'name': 'eth1/36', 'addr': '201.1.1.13/30'}
                ]
            }
        }
    ],
    2: [
        {'name': 'leaf2101_i07-n93180-01', 'serial': '__SERIAL__', 'nodeId': '2101', 'addr': '172.16.0.183/22', 'v6Addr': '::', 'rr': False },
        {'name': 'leaf2102_i07-n93180-02', 'serial': '__SERIAL__', 'nodeId': '2102', 'addr': '172.16.0.184/22', 'v6Addr': '::', 'rr': False },
        {
            'name': 'spine2201_i07-n9336-01',
            'serial': '__SERIAL__',
            'nodeId': '2201',
            'addr': '172.16.1.28/22',
            'v6Addr': '::',
            'rr': True,
            'l3Out': {
                'routerId': '21.21.21.21',
                'interfaces': [
                    {'name': 'eth1/35', 'addr': '202.1.1.1/30'},
                    {'name': 'eth1/36', 'addr': '202.1.1.5/30'}
                ]
            }
        },
        {
            'name': 'spine2202_i07-n9336-02',
            'serial': '__SERIAL__',
            'nodeId': '2202',
            'addr': '172.16.1.27/22',
            'v6Addr': '::',
            'rr': True,
            'l3Out': {
                'routerId': '22.22.22.22',
                'interfaces': [
                    {'name': 'eth1/35', 'addr': '202.1.1.9/30'},
                    {'name': 'eth1/36', 'addr': '202.1.1.13/30'}
                ]
            }
        }
    ]
}}

podTepPools = {1: '10.1.0.0/16', 2: '10.2.0.0/16'}
podProxyTepIp = {1: '201.11.1.1/32', 2: '202.11.1.1/32'}
ipnSubnetList = ['201.1.0.0/16', '202.1.0.0/16']

mgmtOob = {'gw': '172.16.0.1', 'v6Gw': '::'}
bgpAsn = 100
ntpList = [{'name': '172.16.0.1', 'preferred': 'true', 'descr': 'NTP Server'}]
timezone = 'p120_Europe-Brussels'

ospfIfPolicyName = 'IPN_OSPF_IfPolicy'
ospfArea = {'type': 'regular', 'id': '0'}
l3OutName = 'multipod'
l3Label = 'prov_mp1'
routeTarget = 'extended:as2-nn4:29:12'

backup = {
    'path': {
        'name': 'External_FTP_Backups',
        'descr': 'in /FTP-TFTP/path/to/backup/dir/ folder',
        'user': 'anonymous',
        'password': '__USER_PASS_FOR_FTP__',
        'host': '__FTP_SERVER_IP__',
        'port': '21',
        'protocol': 'ftp',
        'remotePath': '/FTP-TFTP/path/to/backup/dir/'
    },
    'schedule': {'name': 'Daily-Fabric-Backup', 'period': 'Daily', 'hour': '2'},
    'name': 'DailyBackupToExternal',
    'descr': 'save backups on external FTP server'
}

linkLevelPolicyList = [
    {'name': '100G_auto', 'autoNeg': 'on', 'speed': '100G'},
    {'name': '40G_auto', 'autoNeg': 'on', 'speed': '40G'},
    {'name': '25G_auto', 'autoNeg': 'on', 'speed': '25G'},
    {'name': '10G_auto', 'autoNeg': 'on', 'speed': '10G'},
    {'name': '1G_auto', 'autoNeg': 'on', 'speed': '1G'}
]

# # # GOLF
golfAsn = 3
golfTtl = 10
golfPeerList = [
    {'ip': '5.5.5.5', 'podId': 'all'},
    {'ip': '6.6.6.6', 'podId': 'all'},
    {'ip': '7.7.7.7', 'podId': 'all'},
    {'ip': '8.8.8.8', 'podId': 'all'}
]
golfLabel = 'golf'
