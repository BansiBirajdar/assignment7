'''1.Write a program which contains one class named as BookStore.
BookStore class contains two instance variables as Name ,Author.
That class contains one class variable as NoOfBooks which is initialise to 0.
There is one instance methods of class as Display which displays name , Author and number of
books.
Initialise instance variable in init method by accepting the values from user as name and author.
Inside init method increment value of NoOfBooks by one.
After creating the class create the two objects of BookStore class as
Obj1 = BookStore(“Linux System Programming”, “Robert Love”)
Obj1.Display() # Linux System Programming by Robert Love. No of books : 1
Obj2 = BookStore(“C Programming”, “Dennis Ritchie”)
Obj2.Display() # C Programming by Dennis Ritchie. No of books : 2'''

class BookStore:
    NoOfBooks=0
    def __init__(self,name,author):
        BookStore.NoOfBooks+=1
        self.Name=name
        self.Author=author
    
    def Display(self):
        print("     Book  Name  Is=",self.Name)
        print("Book Author Name Is=",self.Author)
        print("         No Of Book=",BookStore.NoOfBooks)

def main():
    list=[]
    no=int(input("etner the how many number  of object= "))
    for i in range(0,no):
        name=input("enter the book name = ")
        author=input("enter the book author name =")
        obj=BookStore(name,author)
        print()
        print("           ---Display---")
        obj.Display()
    
if __name__=="__main__":
    main()