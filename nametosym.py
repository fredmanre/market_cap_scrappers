# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:34:10 2018

@author: arnaldo
@modify: fredmanre
"""

import requests
import json


def get_data(cant):
    resource = "https://api.coinmarketcap.com/v1/ticker/?limit="
    r = requests.get(resource + "{}".format(cant))
    coins = r.json()
    names_to_sym = {}
    names_to_sym['Basic Attenti...'] = "BAT"
    names_to_sym['Experience Po...'] = "XP"
    names_to_sym['Walton'] = "WTC"
    names_to_sym['RaiBlocks'] = 'NANO'
    names_to_sym['Santiment Net...'] = "SAN"
    names_to_sym['GXShares'] = "GXS"
    names_to_sym['Raiden Networ...'] = "RDN"
    names_to_sym['Medibloc'] = "MED"
    names_to_sym['Agoras Tokens'] = "AGRS"
    names_to_sym['Storjcoin X'] = "SJCX"
    names_to_sym['YbCoin'] = 'YBC'  # no active
    names_to_sym['SysCoin'] = "SYS"
    names_to_sym['CureCoin'] = "CURE"
    names_to_sym['Global Curre...'] = "GSR"
    names_to_sym['BilShares'] = "BILS"  # inactive
    names_to_sym['StabilityShares'] = "XSI"  # inactive
    names_to_sym['ZcCoin'] = "ZCC"  # inactive
    names_to_sym['UnionCoin'] = "UNC"
    names_to_sym['WildBeastBit...'] = "WBB"
    names_to_sym['Applecoin'] = "APC"  # inactive
    names_to_sym['BitSwift'] = "SWIFT"
    names_to_sym['Horizon'] = "HZ"
    names_to_sym['Mastercoin (...'] = "OMNI"
    names_to_sym['GetGems'] = "GEMZ"  # inactive
    names_to_sym['Scotcoin'] = "SCOT"  # inactive
    names_to_sym['Global Curre...'] = "GCR"
    names_to_sym['TileCoin'] = "XTC"  # inactive
    names_to_sym['EmerCoin'] = "EMC"
    names_to_sym['Nas'] = "NAS"
    names_to_sym['Crypto Bullion'] = "CBX"  # inactive
    names_to_sym['Electronic G...'] = "EFL"
    names_to_sym['Obits'] = "OBITS"
    names_to_sym['NeuCoin'] = "NEU"  # inactive
    names_to_sym['Vanillacoin'] = "VNL"  # inactive
    names_to_sym['ARCHcoin'] = "ARCH"
    names_to_sym['Crypti'] = "XCR"  # inactive
    names_to_sym['NautilusCoin'] = "NAUT"  # inactive
    names_to_sym['Xiaomicoin'] = "MI"  # inactive
    names_to_sym['BlockShares'] = "BKS"  # inactive
    names_to_sym['DogeCoinDark'] = "XVG"
    names_to_sym['InstantDEX'] = "DEX"  # inactive
    names_to_sym['Tickets'] = "TIX"
    names_to_sym['CoinoUSD'] = "XUSD"  # inactive
    names_to_sym['Safe Exchang...'] = "SAFEX"
    names_to_sym['Voxels'] = "VOX"  # inactive
    names_to_sym['Loyyal'] = "LYL"  # inactive
    names_to_sym['Wild Beast B...'] = "WBB"
    names_to_sym['Jinn'] = "JINN"  # inactive
    names_to_sym['The DAO'] = "DAO"  # inactive
    names_to_sym['NAV Coin'] = "NAV"
    names_to_sym['jl777hodl'] = "JLH"  # inactive
    names_to_sym['SkyNET'] = "SNET"  # inactive
    names_to_sym['MMNXT'] = "MMNXT"  # inactive
    names_to_sym['EvergreenCoin'] = "EGC"
    names_to_sym['Ethereum Cla...'] = "ETC"
    names_to_sym['LIQUID'] = "LQD"  # inactive
    names_to_sym['Swiscoin'] = "SCN"  # inactive
    names_to_sym['SARCoin'] = "SAR"  # inactive
    names_to_sym['Stellar Lumens'] = "XLM"
    names_to_sym['Global Curren...'] = "GCR"
    names_to_sym['AntShares'] = "NEO"
    names_to_sym['Golem Network...'] = "GNT"
    names_to_sym['Round'] = "ROUND"  # inactive
    names_to_sym['Hacker Gold'] = "HKG"  # inactive
    names_to_sym['Xenixcoin'] = "XEN"  # inactive
    names_to_sym['Byteball'] = "GBYTE"
    names_to_sym['First Blood'] = "1ST"
    names_to_sym['BelaCoin'] = "BELA"
    names_to_sym['Colossuscoin V2'] = "CV2"  # inactive
    names_to_sym['Waves Communi...'] = "WCT"
    names_to_sym['Quantum Resis...'] = "QRL"
    names_to_sym['OmiseGo'] = "OMG"
    names_to_sym['Bitquence'] = "BQX"
    names_to_sym['Safe Exchange...'] = "SAFEX"
    names_to_sym['Delta'] = "DECRE"
    for coin in coins:
        names_to_sym[coin['name']] = coin['symbol']

    return names_to_sym


def main():
    print(get_data(200))

if __name__ == '__main__':
    main()