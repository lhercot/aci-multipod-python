#!/usr/bin/env python
'''
MultiPod script used for complete fabric deployment from scratch
'''

# List of imports
import functionLibrary as lib
from cobra.internal.codec.xmlcodec import toXMLStr
import config

moList = []

# Log into an APIC and create a directory object
moDirectory = lib.getMoDirectoryFromApic(config.apic)

# Get mo object from the createFabricNodes function with added nodes
moList.append(lib.createFabricNodes(moDirectory, config.fabricNodes))
# moList.append(lib.removeFabricNodes(moDirectory))

moList.append(lib.configOobMgmt(config))
moList.append(lib.createPodPolicy(config))

moList.append(lib.createIpnOspfIfPolicy(config.ospfIfPolicyName))
moList.append(lib.createTEPPools(moDirectory, config.podTepPools))

moList.append(lib.createVlanPool(config.l3OutName, 4, 4))
moList.append(lib.createL3Domain(config.l3OutName,
                                 vlanPoolName=config.l3OutName))
moList.append(lib.createAAEP(config.l3OutName,
                             lib.getExtL3DomDnFromDomainName(config.l3OutName))
              )

moList.append(lib.createLinkLevelPolicy(config.linkLevelPolicyList))
moList.append(lib.createCdpPolicy())
moList.append(lib.createLldpPolicy())
moList.append(lib.createLacpPolicy())

moList.append(lib.createSpineInterfacePolGroup('SpineIPN_IntPolicyGroup',
                                               'CDP_Enable', '40G_auto',
                                               lib.getAAEPDnFromDomainName(
                                                   config.l3OutName)))
moList.append(lib.createSpineInterfaceProfile(
    'SpineIPN_IntProfile',
    'SpineIPN_IntPolicyGroup',
    config.fabricNodes['pods'][1][4]['l3Out']['interfaces']))
moList.append(lib.createSpineSwitchProfile(config.fabricNodes,
                                           lib.getSpineIntProfileDnFromName(
                                               'SpineIPN_IntProfile')))

moList.append(lib.createIpnL3Out(config))
moList.append(lib.createExportEncryptionKey(config))
moList.append(lib.configureBackupPolicy(config.backup))

# For each of the modified objects, print the object and push it to APIC
for mo in moList:
    # Print Mo in XML
    print(toXMLStr(mo))

    # Commit the generated code to APIC
    lib.pushMoToApic(mo, moDirectory)
