# string function k through email program

# email name k variable (email ki closgest condition -> #g@g.in)
email = input("Enter your Email:") #g@g.in, wscube@gmail.com
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if("@" in email) and (email.count("@")==1):
            # exzor operator ^
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        # k variable bana rha hai
                        k=1
                    elif i.isalpha():
                        if i==i.upper(): # w-- W==W (upper case)
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1

                if k==1 or j==1 or d==1:
                    print("wrong Email 5")
            else:
                print("wrong Email 4")
        else:
            print("wrong Email 3")
    else:
        print("wrong Email 2")
else:
    print("wrong Email 1")
         