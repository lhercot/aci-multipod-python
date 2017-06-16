#!/usr/bin/env python
'''
List of ACI functions available in the lib
(used for Testing and sometimes deployment)
'''

# List of imports
import lib as lib
from cobra.internal.codec.xmlcodec import toXMLStr
import configSoLab as config

jsonDbFile = 'dbEpToEPG.json'
dbEpToEpgDict = lib.readJsonDb(jsonDbFile)

moList = []

# Log into an APIC and create a directory object
moDirectory = lib.getMoDirectoryFromApic(config.apic)

# Get mo object from the createFabricNodes function with added nodes
# moList.append(lib.createFabricNodes(moDirectory, config.fabricNodes))
moList.append(lib.removeFabricNodes(moDirectory))
# moList.append(lib.configOobMgmt(config))
# moList.append(lib.createPodPolicy(config))
#
# moList.append(lib.createIpnOspfIfPolicy(config.ospfIfPolicyName))
# moList.append(lib.createTEPPools(moDirectory, config.podTepPools))
#
# moList.append(lib.createVlanPool(config.l3OutName, 4, 4))
# moList.append(lib.createL3Domain(config.l3OutName,
#                                  vlanPoolName=config.l3OutName))
# moList.append(lib.createAAEP(
#   config.l3OutName, lib.getExtL3DomDnFromDomainName(config.l3OutName)))

# moList.append(lib.createLinkLevelPolicy(config.linkLevelPolicyList))
# moList.append(lib.createCdpPolicy())
# moList.append(lib.createLldpPolicy())
# moList.append(lib.createLacpPolicy())
# moList.append(lib.createVlanPool('BXL-LAB', 2000, 2100, 'dynamic'))
# moList.append(lib.addVlanBlockToPool(moDirectory, 'BXL-LAB', 100, 199))
physDomName = 'K8S-VM'
# moList.append(lib.createVlanPool(physDomName, 100, 199))
# moList.append(lib.createPhysDomain(physDomName, physDomName))
# moList.append(lib.createAAEP(physDomName,
#                              lib.getPhysDomDnFromDomainName(physDomName)))

# moList.append(lib.getVlanPool(moDirectory, 'BXL-LAB_vlans'))

# moList.append(lib.createSpineInterfacePolGroup(
#    'SpineIPN_IntPolicyGroup', 'CDP_Enable', '40G_auto',
#    lib.getAAEPDnFromDomainName(config.l3OutName)))
# moList.append(lib.createSpineInterfaceProfile(
#   'SpineIPN_IntProfile', 'SpineIPN_IntPolicyGroup',
#   config.fabricNodes['pods'][1][3]['l3Out']['interfaces']))
# moList.append(lib.createSpineSwitchProfile(
#   config.fabricNodes,
#   lib.getSpineIntProfileDnFromName('SpineIPN_IntProfile')))
#
# moList.append(lib.createVpcInterfacePolGroup(
#   'UCS-05_ESXi_vPC_10G', 'CDP_Enable', 'LLDP_Enable', '10G_auto',
#   'LACP_Active', lib.getAAEPDnFromDomainName(physDomName)))
# moList.append(lib.createLeafInterfaceProfile('UCS-05_ESXi_vPC_10G',
#                                              [{'name': 'eth1/1'}]))
#
# moList.append(lib.createLeafSwitchProfile([101, 102],
#               'UCS-05_ESXi_vPC_10G_IntProfile'))

# moList.append(lib.createVpcDomainPairs(moDirectory, config.vpcList))

# vmmDomain = lib.createVmmDomain(
#   moDirectory, lib.getVlanPool(moDirectory, 'BXL-LAB_vlans').dn,
#   config.vSphere)
# aaep = lib.createAAEP(vmmDomain.name, vmmDomain.dn)
# moList.extend([vmmDomain, aaep])
# moList.append(lib.createVpcInterfacePolGroup(
#   'UCS-05_ESXi_vPC_10G', 'CDP_Enable', 'LLDP_Enable', '10G_auto',
#   'LACP_Active', aaep.dn))

# moList.append(lib.addVswitchPol(
#   moDirectory, 'uni/vmmp-VMware/dom-ACI-VDS/ctrlr-vSphere6_Lab'))
# moList.append(lib.createIpnL3Out(config))
# moList.append(lib.createExportEncryptionKey(config))
# moList.append(lib.configureBackupPolicy(config.backup))

# lib.getL1Ifs(moDirectory)
# moList.append(lib.setDescrL1If(
#    moDirectory, 'topology/pod-1/node-1101/sys/phys-[eth1/48]', 'test'))

# dbDict = lib.readJsonDb('db.json')
# ifList = lib.getL1IfList(moDirectory, 'eq(l1PhysIf.portT, "leaf")')
# dbDict = lib.mergeDbWithIfList(dbDict, ifList)
# lib.writeJsonDb('db.json', dbDict)
# print lib.readJsonDb('db.json')
# moList.append(lib.shutInterface(moDirectory, lib.pathEpDnFromL1PhysIfDn(
#    'topology/pod-1/node-1101/sys/phys-[eth1/48]')))
# moList.append(lib.unShutInterface(moDirectory, lib.pathEpDnFromL1PhysIfDn(
#    'topology/pod-1/node-1101/sys/phys-[eth1/48]')))
# dnToEpgMap = lib.getIfDnToEpgMapping(dbEpToEpgDict)
# print dnToEpgMap


# discoveryIfList = lib.getDiscoveryInterfaceList(moDirectory)
# for ifDn in discoveryIfList:
#     if ifDn in dnToEpgMap:
#         epgDn = dnToEpgMap[ifDn]
#         print '{} --- {}'.format(ifDn, epgDn)
#         moList.append(lib.setStaticBindingForEpg(
#            moDirectory, ifDn, epgDn, dbEpToEpgDict[epgDn]['vlanId'],
#            dbEpToEpgDict[epgDn]['physDomain']))

# For each of the modified objects, print the object and push it to APIC
for mo in moList:
    # Print Mo in XML
    print(toXMLStr(mo))

    # Commit the generated code to APIC
    lib.pushMoToApic(mo, moDirectory)
