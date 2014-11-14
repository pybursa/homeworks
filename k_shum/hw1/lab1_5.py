#!/usr/bin/env python
# -*- coding: utf-8 -*-

def typer(var):
  return type(var).__name__

print typer(666)
print typer("666")
print typer(typer)
