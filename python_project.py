#PYTHON PROJECT
#Nehal Birla
#16CSU225

#Database
pid='P.ID.,,'
lname='Last Name,,'
fname='First Name,,'
pno='Phone Number,,'
add='Address,,'
city='City\n'
table = []
index = None
def createDatabase() :
#checking if file exist or not
    import os.path
    if not os.path.isfile('pythonDB.txt') :
        #if file doesn't exist then creating a new file
        fo = open('pythonDB.txt','w')
        fo.close()
    else : 
        print('Database is already created')


#making my own error to use while inserting the data
#for not null constraint
class NotNull(Exception) :
    pass
#for limiting the size of the input
class OverFlow(Exception) :
    pass
class UnderFlow(Exception) :
    pass
class UniqueConstraint(Exception) :
    pass


#craeting a function to write in file
def writeFile(row) :
    try :
        #checking if file exist or not
        import os.path
        #if file doesn't exist  then raising an error
        if not os.path.isfile('pythonDB.txt') :
            raise FileNotFoundError
        #if file exist then wrting the value in tuple iti the file
        else :
            fa = open('pythonDB.txt','a')
            for i in row :
                fa.write(i)
            fa.close()
    except FileNotFoundError :
        print('database does not exist !! create a new database')

def readFile() :
    try :
        with open('pythonDB.txt','r') as fr :
            l = [tuple(map(str, i.split(',,'))) for i in fr]
        return l
    except FileNotFoundError :
            print('database does not exist')
        
#creating a function to insert values into the table
def insertTable(pid,fname,lname,pno,add,city,pic) : 
    try :

        flag = 0

        #inserting pid
        pid = pid.strip()
        pid = pid.upper()
        z = readFile()
        for i in range(len(z)) :
            if pid == z[i][0] :
                flag = 1
                break
            else :
                flag = 0
        if flag == 1 :
            n='P.ID.'
            raise UniqueConstraint('')
        #checking for not null constraint
        elif len(pid) == 0 :
            n = 'P.ID.'
            raise NotNull('')
        #checking for length of size
        elif len(pid) > 5 :
            n = 5
            raise OverFlow('')
        else :
            #added ',,' at last so that while reading from file i can seperate out the values
            pid = pid.upper()+',,'
           #HAVE TO  ADD UNIQUNESS CONSTRAINT HERE

        #inserting first name
        if len(fname) == 0 :
            n = 'First Name'
            raise NotNull('')
        elif len(fname) > 10 :
            n = 10
            raise OverFlow('')
        #checking if first name contains only alphabets
        elif not fname.isalpha() :
            n = 'alphabets'
            raise ValueError('')  
        else :
            fname = fname.capitalize()+',,'

        #inserting last name
        if len(lname) == 0 :
            n = 'Last Name'
            raise NotNull('')
        elif len(lname) > 10 :
            n = 10
            raise OverFlow('')
        elif not lname.isalpha() :
            n = 'alphabets'
            raise ValueError('')  
        else :
            lname = lname.capitalize()+',,'

        #inserting phone number
        if len(pno) == 0 :
            n = 'Phone Number'
            raise NotNull('')
        elif not pno.isdigit() :
            n = 'numbers'
            raise ValueError
        elif len(pno) < 10 :
            n = 10
            raise UnderFlow('')
        elif len(pno) > 10 :
            n = 10
            raise OverFlow('')
        else :
            pno = pno+',,'

        #inserting address
        if len(add) > 50 :
            n = 50
            raise OverFlow('')
        elif len(add) == 0 :
            n = 'Address'
            raise NotNull('')
        else :
            add = add+',,'

        #inserting city
        city = city.strip()
        if len(city) > 15 :
            n = 15
            raise OverFlow('')
        elif len(city) == 0 :
            n = 'City'
            raise NotNull('')
        #here checking that only city contains alphabets and blankspace
        elif not(city.isalpha() or any(i == ' ' for i in city)) :
            n = '"alphabets" or " "'
            raise ValueError('')
        else :
            city = city.title()+',,'

         #checking for not null constraint
        if len(pic) == 0 :
            n = 'name of image'
            raise NotNull('')
        if '\n' not in pic :
            pic = pic+'\n'
        z = readFile()
        for i in range(len(z)) :
            if pic == z[i][6] :
                if pic == '-\n' :
                    flag = 0
                else :
                    flag = 1
                break
            else :
                flag = 0
        if flag == 1 :
            n='name of image'
            raise UniqueConstraint('')
       
            
            
        #inserting all the values in tuple
        t=(pid,fname,lname,pno,add,city,pic)
        #calling the write in  file function to insert all the entries scanned from user
        writeFile(t)        
        print(t)
        return('tuple added')


    except NotNull :
        print(n,'cannot be null')
        return(str(n)+' cannot be null')
    except OverFlow :
        print('word limit is ',n)
        return('word limit is '+str(n))
    except ValueError :
        print('input should contain only',n)
        return('input should contain only '+str(n))
    except UnderFlow :
        print('length of input should not be less than',n)
        return('length of input should not be less than '+str(n))
    except UniqueConstraint :
        print(n,'should be unique')
        return(str(n)+' should be unique')
    


def printTable() :
    try :
        l = readFile()
        l.sort()
        global pid,fname,lname,pno,add,city
        pid='P.ID.'
        lname='Last Name'
        fname='First Name'
        pno='Phone Number'
        add='Address'
        city='City\n'
        t=(pid,fname,lname,pno,add,city)
        l.insert(0,t)
        for i in l :
            print(i)
        return l
    
    except FileNotFoundError :
        print('database does not exist create a new database!!')



def search(p) :
    try :

        p = p.upper()
        '''with open('pythonDB.txt','r') as fr :
            l = [tuple(map(str, i.split(',,'))) for i in fr]
        l.sort()'''
        l = readFile()
        l.sort()
        flag = 0
        for i in range(len(l)) :
            if p == l[i][0] :
                flag = 1
                break
        if flag == 1 :
            print(l[i])
            return [l[i],i+1]
        else :
            print('no entry found')
            return('no entry found')

    except FileNotFoundError :
            print('database does not exist create a new database!!')

        

def firstTuple() :
    try :
        l = readFile()
        l.sort()
        print(l[0])
        global index
        index = 0
        return(l[0])
    except FileNotFoundError :
            print('database does not exist create a new database!!')
    except  IndexError :
        print('database is empty')


def lastTuple() :
    try :
        l = readFile()
        l.sort()
        print(l[len(l)-1])
        global index
        index = len(l)-1
        return l[index]
    
    except FileNotFoundError :
            print('database does not exist create a new database!!')
    except  IndexError :
        print('database is empty')

def nextTuple(idx) :
    try :
        l = readFile()
        l.sort()
        global index
        if index == len(l)-1 :
            print('table finished')
        elif index == None :
            print('select a row first')
        else :
            if idx != None :
                index = idx-1
            index += 1
            print(l[index])
            return(l[index])
    except FileNotFoundError :
        print('database does not exist')

def prevTuple() :
    try :
        l = readFile()
        l.sort()
        global index
        if index == 0 :
            print('table finished')
        elif index == None :
            print('select a row first')
        else :
            index -= 1
            print(l[index])
            return(l[index])
    except FileNotFoundError :
        print('database does not exist')



def delete(p) :
    try :
        l = readFile()

        p = p.upper()
        for i in range(len(l)) :
            if  p == l[i][0] :
                flag = 1
                print('got')
                break
            else :
                flag = 0
        if flag == 1 :
            del(l[i])
            l1=[]
            for j in l :
                l1.append(',,'.join(j))
            with open('pythonDB.txt','w') as fw :
                fw.writelines(l1)
            return 'deleted'
        else :
            print('no data found')
            return 'no data found with P.Id. '+p
    except FileNotFoundError:
        print('database not found')




def update(p,fname,lname,pno,add,city,pic) :

    delete(p)
    insertTable(p,fname,lname,pno,add,city,pic)
'''try :
        l = readFile()

        p = p.upper()
        for i in range(len(l)) :
            if  p == l[i][0] :
                flag = 1
                print('got')
                break
            else :
                flag = 0
        if flag == 1 :
            del(l[i])
            l1=[]
            for j in l :
                l1.append(',,'.join(j))
            with open('pythonDB.txt','w') as fw :
                fw.writelines(l1)
                
            #inserting first name
            if len(fname) == 0 :
                n = 'First Name'
                raise NotNull('')
            elif len(fname) > 10 :
                n = 10
                raise OverFlow('')
            #checking if first name contains only alphabets
            elif not fname.isalpha() :
                n = 'alphabets'
                raise ValueError('')  
            else :
                fname = fname.capitalize()+',,'

            #inserting last name
            if len(lname) == 0 :
                n = 'Last Name'
                raise NotNull('')
            elif len(lname) > 10 :
                n = 10
                raise OverFlow('')
            elif not lname.isalpha() :
                n = 'alphabets'
                raise ValueError('')  
            else :
                lname = lname.capitalize()+',,'

            #inserting phone number
            if len(pno) == 0 :
                n = 'Phone Number'
                raise NotNull('')
            elif not pno.isdigit() :
                n = 'numbers'
                raise ValueError
            elif len(pno) < 10 :
                n = 10
                raise UnderFlow('')
            elif len(pno) > 10 :
                n = 10
                raise OverFlow('')
            else :
                pno = pno+',,'

            #inserting address
            if len(add) > 50 :
                n = 50
                raise OverFlow('')
            elif len(add) == 0 :
                n = 'Address'
                raise NotNull('')
            else :
                add = add+',,'

            #inserting city
            city = city.strip()
            if len(city) > 15 :
                n = 15
                raise OverFlow('')
            elif len(city) == 0 :
                n = 'City'
                raise NotNull('')
            #here checking that only city contains alphabets and blankspace
            elif not(city.isalpha() or any(i == ' ' for i in city)) :
                n = '"alphabets" or " "'
                raise ValueError('')
            else :
                city = city.title()+',,'

             #checking for not null constraint
            if len(pic) == 0 :
                n = 'name of image'
                raise NotNull('')
            pic = pic+'\n'
            z = readFile()
            for i in range(len(z)) :
                if pic == z[i][6] :
                    if pic == '-\n' :
                        flag = 0
                    else :
                        flag = 1
                    break
                else :
                    flag = 0
            if flag == 1 :
                n='name of image'
                raise UniqueConstraint('')


        
            pid=p+',,'
            #inserting all the values in tuple
            t=(pid,fname,lname,pno,add,city,pic)
            #calling the write in  file function to insert all the entries scanned from user
            writeFile(t)        
            print(t)
            return('tuple updated')


    except NotNull :
        print(n,'cannot be null')
        return(str(n)+' cannot be null')
    except OverFlow :
        print('word limit is ',n)
        return('word limit is '+str(n))
    except ValueError :
        print('input should contain only',n)
        return('input should contain only '+str(n))
    except UnderFlow :
        print('length of input should not be less than',n)
        return('length of input should not be less than '+str(n))
    except UniqueConstraint :
        print(n,'should be unique')
        return(str(n)+' should be unique')'''

'''
import sys
while(True) :
    try :
        a = int(input('\n1\tcreate table\n2\tinsert in table\n3\tprint table\n4\tprint first row of table\n5\tprint last row of table\n6\tsearch\n7\tprint next row\n8\tprint previous row\n9\tupdate\n10\tdelete\n11\texit\nenter\t'))
        if a == 1 :
            createDatabase()
        elif a == 2 :
            insertTable()
        elif a == 3 :
            printTable()
        elif a== 4 :
            firstTuple()
        elif a == 5 :
            lastTuple()
        elif a == 6 :
            search()
        elif a== 7 :
            nextTuple()
        elif a == 8 :
            prevTuple()
        elif a == 9 :
            update()
        elif a == 10 :
            delete()
        elif a== 11 :
            sys.exit()
        else :
            print("enter value from 1 to 11")
    except ValueError :
        print("enter value correctly")
'''
