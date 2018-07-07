#!/usr/bin/env python3
# coding: utf-8

version='1.0.0'

import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='check for broken anchors',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("f", help='file to check')
parser.add_argument("-v", help="increase output verbosity", action="store_true")
args=parser.parse_args()

f = args.f
v = args.v

soup = BeautifulSoup(open(f, 'rb'),"lxml")
elem_set = set()
for elem in soup.find_all():
  elem_id = elem.get('id')
  if elem_id:
    elem_set.add(elem_id)
elem_sorted = sorted(elem_set)
if v:
  print("Full list of ids:")
  for es in elem_sorted:
    print(es)

broken_href = set()
for link in soup.find_all('a'):
  href = link.get('href')
  if href is not None and href.startswith("#"):
    href2 = href[1:]
    if href2 not in elem_set:
      broken_href.add(href2)

broken_href_sorted = sorted(broken_href)
print("List of broken anchors:")
for bhs in broken_href_sorted:
  print(bhs)
