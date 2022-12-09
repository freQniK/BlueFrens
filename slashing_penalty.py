#!/bin/env python3

import json

with open('delegators_at-jail-time.json', 'r') as DELEGATORSFILE:
    delegators = json.load(DELEGATORSFILE)
    
    
SLASHING_FACTOR=0.0001
SATOSHI=1000000
SLASHING_DVPN=0

SLASHING_REFUND_CSV = open('slashing-refund.csv', 'w')

for d in delegators['delegation_responses']:
    delegator = d['delegation']['delegator_address']
    # Skip team's delegation
    #if "sent1vv8kmwrs24j5emzw8dp7k8satgea62l7knegd7" in d['delegation']['delegator_address']:
    #    continue
    #else:
    # Delegation percent of total delegated by delegator
    delegation_dvpn  = round(float(int(d['balance']['amount']) / SATOSHI),12)
    delegation_mudvpn  = int(d['balance']['amount'])
    SLASHING_PENALTY_DVPN = round(float(delegation_dvpn*SLASHING_FACTOR),6)
    SLASHING_PENALTY_MUDVPN = int(delegation_mudvpn*SLASHING_FACTOR)
    SLASHING_DVPN += SLASHING_PENALTY_DVPN
    SLASHING_REFUND_CSV.write('%s,%sudvpn\n' % (delegator, SLASHING_PENALTY_MUDVPN))
    
print("Slashing Penalty: %s dvpn, %s udvpn" % (SLASHING_DVPN, int(SLASHING_DVPN*SATOSHI)))
SLASHING_REFUND_CSV.flush()
SLASHING_REFUND_CSV.close()