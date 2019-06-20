#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:10:21 2019

@author: sichong
"""
import argparse
from ezProtocol import Protocol, Deck

def main():
    parser = argparse.ArgumentParser(description='Process command line arguments for ezProtocol')
    parser.add_argument('--protocol', '-p', action='store', required=True, help='path to protocol file')
    parser.add_argument('--deck', '-d', action='store', required=True, help='path to deck file')
    parser.add_argument('--out', '-o', action='store', required=True, help='file the generated script will be saved at')
    args = parser.parse_args()

    protocol = Protocol.Protocol(args.protocol,args.deck)

    protocol.saveScript(args.out)

if __name__ == '__main__':
    main()
