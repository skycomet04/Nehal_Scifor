def guess_no(user,comp_no,point):
  if comp_no==user:
    point+=1
    ans=f"no is equal"
  elif user>comp_no:
    print(f"no is smaller than {user}")
  else:
    print(f"no is greater than {user}")
  return point
