book_details=[] 
def push(book_details): 
    book_number=int(input("Enter book number")) 
    book_name=input("Enter book name") 
    price=int(input("enter price") )
    x=[book_number,book_name,price] 
    book_details.append(x) 
def pop(book_details): 
    if book_details==[]: 
      return None 
    else: 
      return book_details.pop() 
def display(book_details): 
  if book_details==[]: 
    return None 
  else: return book_details 
def menu(): 
  while True: 
    print("1:Push") 
    print("2:Pop") 
    print("3:DispLay") 
    print("4:Exit") 
    i=int(input("enter the choice")) 
    if i==1: 
      push(book_details) 
    elif i==2: 
      print(pop(book_details)) 
    elif i==3: 
      print(display(book_details)) 
    elif i==4: 
      break 
    else: 
      print("InvaLid choice") 
menu()