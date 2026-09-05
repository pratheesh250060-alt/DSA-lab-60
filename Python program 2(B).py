def fibonnaci(n):
    if n <= 1:
        return n
    else:
        return(fibonnaci(n-1) + fibonnaci(n-2))
    
n1= 20

if n1 <= 0:
  print("invalid input!please inout a positve value")
else:
  print("fibonnaci series:")
  for i in range(n1):
     print(fibonnaci(i))
        
