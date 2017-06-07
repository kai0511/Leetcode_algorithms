def lsao(s):
  '''prints the longest substring of s in which the letters occur in alphabetical order. 
  For example, if s = 'azcbobobegghakl', then your program should print "beggh"
  '''
  tmp_str, max_str = str(), str()

  tmp_str = s[0]
  for i in range(1,len(s)):     
      if s[i-1] <= s[i]:
          tmp_str += s[i]
          if i == (len(s) - 1) and len(max_str) < len(tmp_str):
              max_str = tmp_str
      else:
          if len(max_str) < len(tmp_str):
              max_str = tmp_str            
          tmp_str = s[i]
  print('Longest substring in alphabetical order is: ', max_str)
