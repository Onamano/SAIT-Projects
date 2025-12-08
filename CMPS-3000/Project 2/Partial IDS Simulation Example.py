
trafficTestData = [
    {'SrcIP':'', 'DstIP':'', 'Ports':'', 'Protocol':'', 'Signature':'A7H2K8', 'Encrypted': True, 'isEncrypted': None, 'unencryptedAlert': None, 'signatureAlert': None},
    {'SrcIP':'', 'DstIP':'', 'Ports':'', 'Protocol':'', 'Signature':'B5K1H2', 'Encrypted': False, 'isEncrypted': None, 'unencryptedAlert': None, 'signatureAlert': None},
    {'SrcIP':'', 'DstIP':'', 'Ports':'', 'Protocol':'', 'Signature':'C2Y9J4', 'Encrypted': True, 'isEncrypted': None, 'unencryptedAlert': None, 'signatureAlert': None},
    {'SrcIP':'', 'DstIP':'', 'Ports':'', 'Protocol':'', 'Signature':'D9F5N1', 'Encrypted': False, 'isEncrypted': None, 'unencryptedAlert': None, 'signatureAlert': None},
    {'SrcIP':'', 'DstIP':'', 'Ports':'', 'Protocol':'', 'Signature':'E6V9R8', 'Encrypted': True, 'isEncrypted': None, 'unencryptedAlert': None, 'signatureAlert': None},
    {'SrcIP':'', 'DstIP':'', 'Ports':'', 'Protocol':'', 'Signature':'F2U4B9', 'Encrypted': False, 'isEncrypted': None, 'unencryptedAlert': None, 'signatureAlert': None}
]

#Known digital signatures
signatures = [
    {'Signature': 'A7H2K8'},
    {'Signature': 'D9F5N1'},
    {'Signature': 'E6V9R8'}
]

#Checks traffic test data for encryption and sets isEncrypted to True or False accordingly
def encryptionCheck(trafficTestData):
    for traffic in trafficTestData:
        if 'Encrypted' in traffic and traffic['Encrypted'] == True:
            traffic['isEncrypted'] = True
        if 'Encrypted' in traffic and traffic['Encrypted'] == False:
            traffic['isEncrypted'] = False

#Sets unencryptedAlert to True or False depending on the status of isEncrypted (IDS Flag)
def trafficLog(trafficTestData):
    for traffic in trafficTestData:
        if 'isEncrypted' in traffic and traffic['isEncrypted'] == True:
            traffic['unencryptedAlert'] = False
        if 'isEncrypted' in traffic and traffic['isEncrypted'] == False:
            traffic['unencryptedAlert'] = True
            #Would proceed to perform a deep packet analysis of the unencrypted traffic

#Sets signatureAlert to True or False depending if the traffic signature is known (IDS Flag)
def signatureCheck(trafficTestData, signatures):
    for traffic in trafficTestData:
        traffic['signatureAlert'] = True
        for sig in signatures:
            if 'Signature' in traffic and traffic['Signature'] == sig['Signature']:
                traffic['signatureAlert'] = False
                break

#Provides a simple summary of traffic received and what has been flagged
def flaggedTrafficOutput():
    unencryptedCount = 0
    signatureCount = 0
    print("---IDS Alerts---")
    print(f"Instances of Traffic: {len(trafficTestData)}")
    for traffic in trafficTestData:
        if traffic['unencryptedAlert'] == True:
            unencryptedCount += 1
        if traffic['signatureAlert'] == True:
            signatureCount += 1
    print(f"Instances of Unencrypted Traffic: {unencryptedCount}")
    print(f"Instances of Traffic with Unknown Signatures: {signatureCount}")

encryptionCheck(trafficTestData)
trafficLog(trafficTestData)
signatureCheck(trafficTestData, signatures)
flaggedTrafficOutput()
