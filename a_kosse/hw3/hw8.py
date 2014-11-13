#!/usr/bin/env python
# -*- coding: utf-8 -*-




from utils import input_text, consonants

if __name__ == "__main__":
    in_text = list(input_text())
    counter = 0
    for i in range(1, len(in_text) - 1):
        if in_text[i] == 'a':
            if in_text[i-1] in consonants() and in_text[i+1] in consonants():
                counter += 1
    print counter




