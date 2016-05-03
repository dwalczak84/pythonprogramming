# Contacts book Rev0
 
import pickle

address_book = {}

class Contact(object):
    def __init__(self):
        self.password = 'admin'
        
    def ShowCurrentList(self):
        print 'Current entries in address book:'
        print '-------------------------------------------------------------------------------'
        print 'Name and surname    |    Phone     |Street Address     |      e-mail:         |'   
        print '-------------------------------------------------------------------------------'
        for i in address_book:
            print i + (20-len(i)) * ' ' + '|' + address_book[i][0] + \
            (14-len(address_book[i][0])) * ' ' + '|' + address_book[i][1] + \
            (19-len(address_book[i][1])) * ' ' + '|' + address_book[i][2] + \
            (22-len(address_book[i][2])) * ' ' + '|'
        print '-------------------------------------------------------------------------------'

    def AddNewPerson(self, name, phone, address, email):
        if type(name) == str and type(phone) == str and type(address) == str \
        and type(email) == str:
            address_book[name] = [phone, address, email]
            print 'Person added successfully.'
            return
        else:
            print 'entries have to be addes as strings. Please correct entry'
    
    def DeletePerson(self, name, email):
        if any(address_book):
            if name in address_book and email in address_book:
                del address_book[name]
                print 'Person was removed from the Address Book successfully'
                return
            else:
                print 'You have entered invalid details. You must provide'
                print 'Person\'s full name and his or her correct e-mail.'
                print 'Please try again.'
                return
        else:
            print 'The address book is empty. No record can be deleted.'
            print 'Please add at least one new record to the Address Book.'
            return
    
    def SaveCurrentList(self):
        pickle.dump(address_book, open("address_book.p", "wb"))
        print 'Contacts saved to file: address_book successfully.'
        
    def LoadExistingList(self):
        address_book = pickle.load( open("address_book.p", "rb"))
        print 'Contacts read from file: address_book successfully.' 
