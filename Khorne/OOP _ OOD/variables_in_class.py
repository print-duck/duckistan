'''class Library:
     var='books'
     def reader_cse(self):
          print('cse guy, will read', Library.var)
     def reader_eie(self):
          print('eie guy, will read', Library.var)


l=Library()
l.reader_cse()
l.reader_eie()'''


#roll_no =12
'''def dinesh():
     roll_no=23
     def praveen():
          nonlocal roll_no
          roll_no=33
          print('roll no of praveen is', roll_no)
     print('roll no of dinesh is', roll_no)
     praveen()
dinesh()
#print(roll_no)'''



'''class Library:
     dept='cse'
     def dinesh(self):
          roll_no=23
          print('roll no of dinesh is', roll_no,Library.dept)
     def praveen(self):
          print('roll no of praveen is', roll_no,Library.dept)
l=Library()
l.dinesh()
l.praveen()     
'''


'''weather = 'raining'
class Report:
     def today(self):
          print('Today is', weather)
     def yesterday(self):
          print('Yesterday it was,',weather,'but i had a umberlla')
r=Report()
r.today()
r.yesterday()'''
