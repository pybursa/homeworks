# -*- coding: utf-8 -*-

def calculate_vowels(text):
  """
    function(str) -> dict
    Counts the number of vowels in each word of text
  """
  def vowels_counter(word):
      vowels = "aeiouy"
      vowels_sum = sum([word.count(char) for char in vowels if char in word])
      return vowels_sum
  words = text.split()
  result = {w: vowels_counter(w) for w in words}
  return result


def sort_text_by_length(text):
  """
    function(str) -> list
    Sorts the text by the number of characters in words
  """
  words = text.split()
  words.sort(key=lambda w: len(w), reverse=True)
  return words



def sum_of_digits(digit):
  """
    function(int) -> int
    Sorts the text by the number of characters in words
  """
  res = 0
  while digit > 0:
      mod = digit % 10
      res = res - mod
      digit = digit // 10
  res = res * -1
  return res



def prime_numbers(max_limit):
    """function(int) -> str
       Calculates sequentially of primes
    """
    lst = [0, 0]
    i=2
    while i <= max_limit:
        lst.append(1)
        i += 1

    i=2
    while i*i <= max_limit:
        if lst[i] == 1:
            i_sqr = i*i
            while i_sqr <= max_limit:
                lst[i_sqr] = 0
                i_sqr += i
        i += 1

    res_lst = []
    for i, v in enumerate(lst):
        if v == 1:
            res_lst.append(str(i))

    return res_lst




def reverse_text(text):
    """function(str) -> str"""
    text_list = list(text)
    text_list.reverse()
    if '.' in text_list[0]:
        text_list.pop(0)

    i = 0
    for k in range(text_list.count(',')):
        i = text_list.index(',', i)
        text_list.pop(i)
        ch = ''
        while ch != ' ':
            i += 1
            ch = text_list[i]
        text_list.insert(i, ',')
        i += 1

    txt_lower_case = ''.join(text_list).lower()
    sentences = txt_lower_case.split('.')
    sentence_list = [line.strip().capitalize()+'. ' for line in sentences]
    result_text = ''.join(sentence_list)
    return result_text


def a_counter(text):
    """function(str) -> int
       Counts the number of character 'A' in the
       text which is surrounded by consonants
    """
    count = 0
    vowels = 'aeiouy'
    for i, v in enumerate(text):
        s = text[i:i+3]
        if len(s) < 3: continue
        if s[1] != 'a': continue
        if not(s[0].isalpha()) or not(s[2].isalpha()): continue
        if s[0].lower() in vowels or s[2].lower() in vowels: continue
        count += 1
    return count
