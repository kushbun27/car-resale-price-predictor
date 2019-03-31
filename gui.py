from tkinter import *
import datetime
import koshish as mdl


class DBike(Exception) :
    pass
class NotNull(Exception) :
    pass
class WrongYear(Exception) :
    pass

def callback1(event) :
    n = name_entry.get('1.0',END)
    print(n)
    if '--Enter Vehicle Name--' in name_entry.get('1.0',END) :
        name_entry.delete('1.0',END)
    

def callback2(event) :
    yr = year_entry.get('1.0',END).replace('\n','')
    if yr.isdigit() == False :
        year_entry.delete('1.0',END)
        print('no num')
    elif int(yr)<datetime.date.today().year-18 or int(yr)>datetime.date.today().year :
        year_entry.delete('1.0',END)
        print('no yr')

def callback3(event) :
    if pp_entry.get('1.0',END).replace('\n','').replace('.','',1).isdigit() == False :
        pp_entry.delete('1.0',END)
        print('no num')

def callback4(event) :
     if km_entry.get('1.0',END).replace('\n','').replace('.','',1).isdigit() == False :
        km_entry.delete('1.0',END)
        print('no num')

top = Tk()
top.title('car bech do')
top.geometry('980x700')
top.resizable(False,False)
m = '#%02x%02x%02x' % (0,162,232)
top.config(bg = 'black')
'''
# create the canvas, size in pixels
canvas = Canvas(width = 300, height = 200, bg = 'yellow')
# pack the canvas into a frame/form
canvas.pack(expand = YES, fill = BOTH)
# load the .gif image file
# put in your own gif file here, may need to add full path
# like 'C:/WINDOWS/Help/Tours/WindowsMediaPlayer/Img/mplogo.gif'
gif1 = PhotoImage(file = 'giphy.gif')
# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(50, 10, image = gif1, anchor = NW)
# run it ...'''
can = Canvas(top)
can.pack()
can.place(x= 570,y = 200)
heading = Label(top,text = 'D.Eye',bg = 'black',foreground = 'yellow')
heading.config(font = ('Times New Roman',50))
heading.pack()
vehicle_label = Text(top,bg = 'black',font = ('Times New Roman',20),height = 0.5,width = 13)
vehicle_label.insert(INSERT,'Vehicle Type*')
vehicle_label.tag_add("start", "1.12", "1.13")
vehicle_label.tag_config("start", foreground="red",font = ('Times New Roman',12),offset = 9)
vehicle_label.config(state = 'disabled',relief = FLAT,foreground = 'yellow')
vehicle_label.pack()
vehicle_label.place(x = 98,y = 150)

note = Text(top,bg = 'black',font = ('arial',9),height = 1.5,width = 45)
note.insert(INSERT,'NOTE : options marked with * are mandatory to fill')
note.tag_add("start", "1.27", "1.28")
note.tag_config("start", foreground="red",font = ('Times New Roman',12))
note.config(state = 'disabled',relief = FLAT,foreground = 'White')
note.pack()
note.place(x=20,y=610)


'''vehicle_label = Label(top,text = 'Vehicle Type',bg = 'black',foreground = 'yellow',font = ('Times New Roman',20))
vehicle_label.pack()
vehicle_label.place(x = 100,y = 150)'''

lst1 = ['4 Wheeler','2 Wheeler']
var1 = StringVar(top)
vehicle_list = OptionMenu(top,var1,*lst1)
var1.set("--choose an option--")
vehicle_list.config(bg = 'black',foreground = 'yellow',font = ('Times New Roman',20))
vehicle_list['menu'].config(bg = 'black',foreground = 'yellow',font = ('Times New Roman',20))
vehicle_list.pack()
vehicle_list.place(x = 270 , y = 145)

name = Label(top,text = 'Vehicle Name',bg = 'black',foreground = 'yellow',font = ('Times New Roman',20))
name.pack()
name.place(x=93,y=220)

name_entry = Text(top,bg = 'black',font = ('Times New Roman',20),height = 0.5,width = 19)
name_entry.config(fg = 'yellow',highlightthickness=2,insertbackground = 'white', highlightcolor = 'aqua')
name_entry.insert(INSERT,'--Enter Vehicle Name--')
name_entry.bind('<Button-1>',callback1)
name_entry.pack()
name_entry.place(x = 270, y = 215)

year = Text(top,bg = 'black',font = ('Times New Roman',20),height = 0.5,width = 13)
year.insert(INSERT,'Year of Model*')
year.tag_add("start", "1.13", "1.14")
year.tag_config("start", offset = 9,foreground="red",font = ('Times New Roman',12))
year.config(state = 'disabled',relief = FLAT,foreground = 'yellow')
year.pack()
year.place(x=85,y=290)

year_entry = Text(top,bg = 'black',font = ('Times New Roman',20),height = 0.5,width = 19)
year_entry.config(fg = 'yellow',highlightthickness=2,insertbackground = 'white', highlightcolor = 'aqua')
year_entry.insert(INSERT,  '  --Enter Model Year--')
year_entry.bind('<Button-1>',callback2)
year_entry.pack()
year_entry.place(x = 270, y = 283)

pp = Text(top,bg = 'black',font = ('Times New Roman',20),height = 0.5,width = 14)
pp.insert(INSERT,'Showroom Price*')
pp.tag_add("start", "1.14", "1.15")
pp.tag_config("start", offset = 9,foreground="red",font = ('Times New Roman',12))
pp.config(state = 'disabled',relief = FLAT,foreground = 'yellow')
pp.pack()
pp.place(x=65,y=360)

pp_entry = Text(top,bg = 'black',font = ('Times New Roman',20),height = 0.5,width = 19)
pp_entry.config(fg = 'yellow',highlightthickness=2,insertbackground = 'white', highlightcolor = 'aqua')
pp_entry.insert(INSERT,  ' --Enter price in lakhs--')
pp_entry.bind('<Button-1>',callback3)
pp_entry.pack()
pp_entry.place(x = 270, y = 353)

km = Text(top,bg = 'black',font = ('Times New Roman',20),height = 0.5,width = 15)
km.insert(INSERT,'Kilometer Driven*')
km.tag_add("start", "1.16", "1.17")
km.tag_config("start", offset = 9,foreground="red",font = ('Times New Roman',12))
km.config(state = 'disabled',relief = FLAT,foreground = 'yellow')
km.pack()
km.place(x=60,y=430)

km_entry = Text(top,bg = 'black',font = ('Times New Roman',20),height = 0.5,width = 19)
km_entry.config(fg = 'yellow',highlightthickness=2,insertbackground = 'white', highlightcolor = 'aqua')
km_entry.insert(INSERT,  '-Total distance covered-')
km_entry.bind('<Button-1>',callback4)
km_entry.pack()
km_entry.place(x = 270, y = 423)

fuel = Text(top,bg = 'black',font = ('Times New Roman',20),height = 0.5,width = 15)
fuel.insert(INSERT,'Fuel Type*')
fuel.tag_add("start", "1.9", "1.10")
fuel.tag_config("start", offset = 9,foreground="red",font = ('Times New Roman',12))
fuel.config(state = 'disabled',relief = FLAT,foreground = 'yellow')
fuel.pack()
fuel.place(x=138,y=500)

lst2 = ['Petrol','Diesel']
var2 = StringVar(top)
fuel_list = OptionMenu(top,var2,*lst2)
var2.set("--choose an option--")
fuel_list.config(bg = 'black',foreground = 'yellow',font = ('Times New Roman',20))
fuel_list['menu'].config(bg = 'black',foreground = 'yellow',font = ('Times New Roman',20))
fuel_list.pack()
fuel_list.place(x = 270 , y = 493)

trans = Text(top,bg = 'black',font = ('Times New Roman',20),height = 0.5,width = 15)
trans.insert(INSERT,'Transmission*')
trans.tag_add("start", "1.12", "1.13")
trans.tag_config("start", offset = 9,foreground="red",font = ('Times New Roman',12))
trans.config(state = 'disabled',relief = FLAT,foreground = 'yellow')
trans.pack()
trans.place(x=50,y=570)

lst4 = ['Manual','Automatic']
var4 = StringVar(top)
trans_list = OptionMenu(top,var4,*lst4)
var4.set("--choose an option--")
trans_list.config(bg = 'black',foreground = 'yellow',font = ('Times New Roman',20))
trans_list['menu'].config(bg = 'black',foreground = 'yellow',font = ('Times New Roman',20))
trans_list.pack()
trans_list.place(x = 220, y = 563)

own = Text(top,bg = 'black',font = ('Times New Roman',20),height = 0.5,width = 15)
own.insert(INSERT,'Owner*')
own.tag_add("start", "1.5", "1.6")
own.tag_config("start", offset = 9,foreground="red",font = ('Times New Roman',12))
own.config(state = 'disabled',relief = FLAT,foreground = 'yellow')
own.pack()
own.place(x=540,y=570)

lst3 = ['First Hand','Second Hand','Third Hand','Fourth & above']
var3 = StringVar(top)
own_list = OptionMenu(top,var3,*lst3)
var3.set("--choose an option--")
own_list.config(bg = 'black',foreground = 'yellow',font = ('Times New Roman',20))
own_list['menu'].config(bg = 'black',foreground = 'yellow',font = ('Times New Roman',20))
own_list.pack()
own_list.place(x = 640 , y = 563)

def sale() :
    ans = Label(top,text = 'Please be paitient Calculating... .. .',bg = 'black',foreground = 'aqua',font = ('Times New Roman',20))
    ans.pack()
    ans.place(x=230,y=80)
    l = []
    vtype = var1.get()

    yr = year_entry.get('1.0',END).replace('\n','')
    print(yr)
    n = None
    try :
        if 'choose' in var1.get() :
            raise NotNull
        print(yr)
        
        n = 'integer'
        if yr == '' :
            l = []
            raise NotNull
        elif int(yr)<datetime.date.today().year-18 or int(yr)>datetime.date.today().year :
            n = 'year'
            l = []
            raise WrongYear
        else :
            l.append(int(yr))
            print(l)

        cp = pp_entry.get('1.0',END).replace('\n','')
        if cp == '' :
            l = []
            raise NotNull
        elif cp.replace('.','',1).isdigit() == False :
            l = []
            n = 'numeric'
            raise ValueError
        else  :
            l.append(float(cp))
            print(l)

        kms = km_entry.get('1.0',END).replace('\n','')
        if kms == '' :
            l =[]
            raise NotNull
        elif kms.replace('.','',1).isdigit() == False :
            l = []
            n = 'numeric'
            raise ValueError
        else :
            l.append(round(float(kms)))
            print(l)


        if 'choose' in var2.get() :
            l =[]
            raise NotNull
        else :
            if 'Petrol' in var2.get() and '4' in var1.get() :
                ftype = 1
            elif 'Diesel' in var2.get() and '4' in var1.get() :
                ftype = 0
            elif 'Petrol' in var2.get() and '2' in var1.get() :
                ftype = 0
            elif 'Diesel' in var2.get() and '2' in var1.get() :
                l = []
                raise DBike
            l.append(ftype)
            '''if 'Petrol' in var2.get() :
                l.pop()'''
            print(l)
            
        if 'choose' in var4.get() :
            l = []
            raise NotNull
        else :
            if 'Manual' in var4.get() :
                otype = "1"
            elif 'Automatic' in var4.get() :
                otype = '0'

            l.append(int(otype))
            print(l)

        if 'choose' in var3.get() :
            l = []
            raise NotNull
        else :
            if 'First' in var3.get() :
                otype = "0"
            elif 'Second' in var3.get() :
                otype = '1'
            elif 'Third' in var3.get() :
                otype = '2'
            elif '&' in var3.get() :
                otype = '3'
            l.append(int(otype))
            print(l)

        ans.config(text = 'Please be paitient Calculating... .. .                     ')


        if '4' in vtype :
            Range = mdl.carModel(l)
        elif '2' in vtype :
            Range = mdl.bikeModel(l)

        
        Range[0] = "{:.2f}".format(Range[0])
        
        Range[2] = "{:.2f}".format(Range[2])

        mml = str(Range[0])+" "+Range[1]+" "+str(Range[2])+" lakhs"
            
        print(Range)
        ans.config(text ="                 "+mml+"                                                                                                                                    ")

            
        
    except NotNull :
        ans.config(text = 'Value can not be null                                                            ')
        print('value can not be null')
    except WrongYear :
        st = 'enter right '+n+' value                                                                               '
        print('enter right '+n+' value')
        ans.config(text = st)
    except ValueError :
        ans.config(text = "Value should be "+n+"                                         ")
        print('Value should be numeric ')
    except DBike :
        ans.config(text = 'Choose Petrol with 2 wheelers.                      ') 
    except :
        ans.config(text = "sorry an error occured                                    ")

            

    

find = Button(top,text = 'Find',height = 1,width = 10,bg = 'black',foreground = 'red',activeforeground = 'white',activebackground = m,font = ('Times New Roman',20),command = sale)
find.pack()
find.place(x=400,y = 630)












#car_entry = Entry(top,height = 20)
#car_entry.insert(0,'enter car name')
#car_entry.pack()
mainloop()
