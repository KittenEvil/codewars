#!/usr/bin/python

# string = "01:09:02,684 --> 01:09:03,601 Run Forrest, run!"  
# subs_offset_apply(string, 3663655)
# output: "02:10:06,339 --> 02:10:07,256 Run Forrest, run!"
# 
# "00:43:22,074 --> 00:43:24,159 No, I am your father."
# subs_offset_apply(string, 1789)   
# output: "00:43:23,863 --> 00:43:25,948 No, I am your father." 
# 
# "00:03:06,241 --> 00:03:07,618 I'll be back."
# subs_offset_apply(string, -21789) 
# output: "00:02:44,452 --> 00:02:45,829 I'll be back."

import re

def explode_millis(utime):
  result = [ utime % 1000 ]
  utime //= 1000
  result += [ utime % 60 ]
  utime //= 60
  result += [ utime % 60 ]
  utime //= 60
  result += [ utime ]
  return list(map(str,result[::-1]))


def subs_offset_apply(string, offset):
  # parse string
  string_regex = re.compile('(?P<h1>\d+):(?P<m1>\d+):(?P<s1>\d+),(?P<ms1>\d+) --> (?P<h2>\d+):(?P<m2>\d+):(?P<s2>\d+),(?P<ms2>\d+) (?P<msg>.*$)')

  # Parse times to millis
  m = string_regex.search(string)
  start_time=int(m.group('ms1'))+1000*int(m.group('s1'))+1000*60*int(m.group('m1'))+1000*60*60*int(m.group('h1'))
  end_time=int(m.group('ms2'))+1000*int(m.group('s2'))+1000*60*int(m.group('m2'))+1000*60*60*int(m.group('h2'))
  msg = m.group('msg')

  start_time += offset
  end_time += offset

  # check for errors
  if start_time < 0 or end_time > 999 + 59*1000 + 59*60*1000 + 99*60*60*1000:
    return "Invalid offset"

  start_times=explode_millis(start_time)
  end_times=explode_millis(end_time)
  return("{0:0>2}:{1:0>2}:{2:0>2},{3:0>3} --> {4:0>2}:{5:0>2}:{6:0>2},{7:0>3} {8}".format(*(start_times+end_times+[msg])))
