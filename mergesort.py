import time
import random

arr2 = None

def iter_merge():
  pass

def rec_merge(lo,hi):
  """recursive mergesort with global variables"""
  if lo+1>=hi: return [arr2[lo]]
  else:
    ans,i,j = list(),0,0
    mid = lo + ((hi-lo)>>1)

    left = rec_merge(lo,mid) ; len_l = len(left)
    right = rec_merge(mid,hi) ; len_r = len(right)

    while i < len_l or j < len_r:
      if i >= len_l: 
        for b in right[j:]: ans.append(b)
        j = len_r
      elif j >= len_r: 
        for b in left[i:]: ans.append(b)
        i = len_l
      elif left[i] <= right[j]: 
        ans.append(left[i]) ; i+=1
      else: 
        ans.append(right[j]) ; j+=1
    return ans

def rec_merge_v2(arr):
  """recursive mergesort without global variables"""
  if len(arr)<=1: return arr
  else:
    ans,i,j = list(),0,0
    mid = len(arr)>>1

    left = rec_merge_v2(arr[:mid]) ; len_l = len(left)
    right = rec_merge_v2(arr[mid:]) ; len_r = len(right)

    while i < len_l or j < len_r:
      if i >= len_l: 
        for b in right[j:]: ans.append(b)
        j = len_r
      elif j >= len_r: 
        for b in left[i:]: ans.append(b)
        i = len_l
      elif left[i] <= right[j]: 
        ans.append(left[i]) ; i+=1
      else: 
        ans.append(right[j]) ; j+=1
    return ans

def main():
  global arr2
  #arr2 = [6,5,3,1,8,7,2,4]
  #print("recursive: ",rec_merge(0,len(arr2)))
  #print("recursive v2: ", rec_merge_v2(arr2))

  N,vector,ans1,ans2 = 100000,list(),list(),list()
  for _ in range(N): vector.append([random.randint(1,20) for _ in range(10)])

  t0 = time.time()
  for v in vector:
    arr2 = list(v) ; ans1.append(rec_merge(0,len(arr2)))
  t1 = time.time() ; print(t1-t0)
  for v in vector: 
    ans2.append(v.sort())
    #ans2.append(rec_merge_v2(v))
  print(time.time()-t1)

  """
  for i in range(N):
    for j in range(1,len(vector[i])):
      assert ans1[i][j] >= ans1[i][j-1] and ans2[i][j] >= ans2[i][j-1]
  """

main()