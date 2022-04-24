from tkinter import *

from tkinter import messagebox

import psycopg2
from psycopg2 import Error

# from modules import databaseModule, utils, VideoPlayerModule
import conexion

class Login:

   def __init__(self,root):
    self.root=root

    self.root.title("Login and registration system for Apps")

    self.root.geometry("1366x700+0+0")

    self.root.resizable(False,False)

    self.loginform()

   def loginform(self):

    Frame_login=Frame(self.root,bg="white")

    Frame_login.place(x=0,y=0,height=700,width=1366)
    

    frame_input=Frame(self.root,bg='white')

    frame_input.place(x=320,y=130,height=450,width=350)

    label1=Label(frame_input,text="Login Here",font=('impact',32,'bold'), fg="black",bg='white')

    label1.place(x=75,y=20)

    label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

    label2.place(x=30,y=95)

    self.email_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')

    self.email_txt.place(x=30,y=145,width=270,height=35)

    label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

    label3.place(x=30,y=195)

    self.password=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')

    self.password.place(x=30,y=245,width=270,height=35)

 

    btn1=Button(frame_input,text="forgot password?",cursor='hand2',font=('calibri',10),bg='white',fg='black',bd=0)

    btn1.place(x=125,y=305)



    btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

    btn2.place(x=90,y=340)

      

    btn3=Button(frame_input,command=self.Register,text="Not Registered?register",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)

    btn3.place(x=110,y=390)

#login
   def login(self):

    if self.email_txt.get()=="" or self.password.get()=="":

      messagebox.showerror("Error","All fields are required",parent=self.root)

    else:
     try:
       
        #con=psycopg2.connect(user="postgres", password="NYARLATHOTEP", host="localhost", port="5432", database="Proyecto2")
        con=psycopg2.connect(user="postgres", password="123", host="localhost", port="5432", database="Proyecto2")

        cur=con.cursor()
        
        cur.execute('select * from cuenta where correo=%s and pssword=%s',(self.email_txt.get(),self.password.get()))

        row=cur.fetchone()
        if row==None:
         messagebox.showerror('Error','Invalid Username And Password',parent=self.root)
         self.loginclear()
         self.email_txt.focus()
        else:
         self.appscreen()

         con.close()

     except Exception as es:
       
      messagebox.showerror('Error',f'Error Due to : {str(es)}',parent=self.root)

#área de registro 
   def Register(self):

    Frame_login1=Frame(self.root,bg="white")

    Frame_login1.place(x=0,y=0,height=700,width=1366)

    frame_input2=Frame(self.root,bg='white')

    frame_input2.place(x=320,y=130,height=450,width=630)

    label1=Label(frame_input2,text="Register Here",font=('impact',32,'bold'),fg="black",bg='white')

    label1.place(x=45,y=20)

    label6=Label(frame_input2,text="TYPE OF ACCOUNT 1=Basica 2=Estandar 3=Avanzada",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

    label6.place(x=30,y=195)

    self.Finish=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

    self.Finish.place(x=30,y=245,width=270,height=35)

    if self.Finish.get()=="":

      messagebox.showerror("Error","Need to fill the search field",parent=self.root)

    else:
       if self.Finish.get()=="1":
          #AQUI ES PARA EL TIPO DE CUENTA
          print("OPCION 1")
       if self.Finish.get()=="2":
          #AQUI ES PARA EL TIPO DE CUENTA
          print("OPCION 2")
       else:
          #AQUI SETEAMOS QUE PUES SE TERMINO DE REPRODUCIR EL VIDEO
          print("OPCION 3")

    label2=Label(frame_input2,text="E-mail",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

    label2.place(x=30,y=95)

    self.entry=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

    self.entry.place(x=30,y=145,width=270,height=35)

    

    label3=Label(frame_input2,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

    label3.place(x=30,y=195)

    self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

    self.entry2.place(x=30,y=245,width=270,height=35)



    label4=Label(frame_input2,text="Email-id",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

    label4.place(x=330,y=95)

    self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

    self.entry3.place(x=330,y=145,width=270,height=35)

     

    label5=Label(frame_input2,text="Confirm Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

    label5.place(x=330,y=195)

    self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')

    self.entry4.place(x=330,y=245,width=270,height=35)

    btn2=Button(frame_input2,command=self.register,text="Register",cursor="hand2",font=("times new roman",15),fg="white",

    bg="orangered",bd=0,width=15,height=1)

    btn2.place(x=90,y=340)

    btn3=Button(frame_input2,command=self.loginform,

    text="Already Registered?Login",cursor="hand2",

    font=("calibri",10),bg='white',fg="black",bd=0)

    btn3.place(x=110,y=390)


#Resgitro de cuenta
   def register(self):

    if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":

      messagebox.showerror("Error","All Fields Are Required",parent=self.root)

    elif self.entry2.get()!=self.entry4.get():

      messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=self.root)

    else:

       try:

        #con=psycopg2.connect(user="postgres", password="NYARLATHOTEP", host="localhost", port="5432", database="proyecto2")
        con=psycopg2.connect(user="postgres", password="123", host="localhost", port="5432", database="Proyecto2")

        cur=con.cursor()

        cur.execute("select * from cuenta where correo=%s",self.entry3.get())


        row=cur.fetchone()

        if row!=None:

           messagebox.showerror("Error"

           ,"User already Exist,Please try with another Email",parent=self.root)

           self.regclear()

           self.entry.focus()

        else:

          cur.execute("insert into cuenta values(%s,%s,%s,%s)",(self.entry.get(),self.entry3.get(),self.entry2.get(),self.entry4.get()))          
          con.commit()

          con.close()

          messagebox.showinfo("Success","Register Succesfull",parent=self.root)

          self.regclear()

       except Exception as es:

        messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)





























   def appscreen(self):

    Frame_login=Frame(self.root,bg="white")

    Frame_login.place(x=0,y=0,height=700,width=1366)

    label1=Label(Frame_login,text="Hi! Welcome ORANGE YOUTUBE",font=('times new roman',32,'bold'),fg="black",bg='white')

    label1.place(x=375,y=100)

    btn1=Button(Frame_login,text="Search",command=self.searchMi,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

    btn1.place(x=90,y=340)

    btn3=Button(Frame_login,text="ShowList",command=self.ShowList,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

    btn3.place(x=90,y=500)

    isadm = False
    #MOMO: Aqui en la variable tenes que poner el query para distinguir si es admin o no
    queryAn = "INSERTE EL QUERY PARA LA RESPUESTA"
    if(queryAn == ''):
      isadm = True
    else:
      isadm = False

    isadm = False

    if(isadm == True):
      btn4=Button(Frame_login,text="Upgrade",command=self.upgrade,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

      btn4.place(x=90,y=580)
    else:
      btn4=Button(Frame_login,text="Stadistics",command=self.stad,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

      btn4.place(x=90,y=580)

    btn5=Button(Frame_login,text="Logout",command=self.loginform,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

    btn5.place(x=1000,y=10)

    


























#ShowList
   def ShowList(self):
    Frame_login=Frame(self.root,bg="white")

    Frame_login.place(x=0,y=0,height=700,width=1366)

    btn2=Button(Frame_login,text="Go back",command=self.appscreen,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=20,height=1)

    btn2.place(x=400,y=340)
    
    try:
         
      #con=psycopg2.connect(user="postgres", password="NYARLATHOTEP", host="localhost", port="5432", database="proyecto2")
      con=psycopg2.connect(user="postgres", password="123", host="localhost", port="5432", database="Proyecto2")

      #AQUI TENEMOS QUE PONER JUNTO A UN NUMERO EL TITULO QUE SE ENCONTRO DE LA BUSQUEDA PARA QUE LUEGO LE PEDIMOS QUE INGRESE UN NUMERO 
      #PARA PODER SABER QUE CONTENIDO VAMOS A REPRODUCIR
      # label1=Label(frame_input,text="TITULOS ENCONTRADOS!",font=('impact',32,'bold'), fg="black",bg='white')

      # label1.place(x=75,y=20)

      #    con.close()

      con = ['a','b']#MOMO: ES UN ARRAY SIMULADO, PARA QUE SE PONGA EL QUERY PARA QUE VENGA LA INFO DE LOS CONTENIDOS

      for x in con:

         label4=Label(Frame_login,text=con[x],font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

         label4.place(x=30,y=195)

    except Exception as es:
         
      messagebox.showerror('Error',f'Error Due to : {str(es)}',parent=self.root)



























#upgrade
   def upgrade(self):
    Frame_login=Frame(self.root,bg="white")

    Frame_login.place(x=0,y=0,height=700,width=1366)

    label1=Label(Frame_login,text="Want to upgrade?",font=('times new roman',32,'bold'),fg="black",bg='white')

    label1.place(x=375,y=100)

    btn1=Button(Frame_login,text="UPGRADE DADDY?",command=self.upgradeMake,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=20,height=1)

    btn1.place(x=100,y=340)

    btn2=Button(Frame_login,text="Go back",command=self.appscreen,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=20,height=1)

    btn2.place(x=400,y=340)

#upgrade make
   def upgradeMake(self):

    Frame_login=Frame(self.root,bg="white")

    Frame_login.place(x=0,y=0,height=700,width=1366)

    #MOMO: Meter el query para hacer el upgrade

    btn9=Button(Frame_login,text="CLICK TO COMPLETE",command=self.appscreen,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=20,height=1)

    btn9.place(x=150,y=340)



























#stadisticas
   def stad(self):

    Frame_login=Frame(self.root,bg="white")

    Frame_login.place(x=0,y=0,height=700,width=1366)

    frame_input=Frame(self.root,bg='white')

    frame_input.place(x=320,y=130,height=450,width=350)

    label3=Label(frame_input,text="CONTENTS",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

    label3.place(x=30,y=195)

    btn9=Button(Frame_login,text="GO BACK",command=self.appscreen,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

    btn9.place(x=1000,y=10)



























#Search by director, actor y nombre de título
   def searchMi(self):

    frame_input=Frame(self.root,bg='white')

    frame_input.place(x=0,y=0,height=700,width=1366)

    label3=Label(frame_input,text="Search",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

    label3.place(x=30,y=30)

    label3=Label(frame_input,text="1.estelares\n2.director\n3.categoria\n4.genero\n5.premios\n6.estreno\n7.nombre",font=("times new roman",10),fg='black',bg='white')

    label3.place(x=30,y=60)

    label3=Label(frame_input,text="INSERTE UNA OPCION PARA BUSCAR",font=("Goudy old style",13,"bold"),fg='black',bg='white')

    label3.place(x=30,y=200)

    self.search_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')

    self.search_txt.place(x=30,y=250,width=270,height=35)

    label3=Label(frame_input,text="INSERTE LO QUE DESEA BUSCAR",font=("Goudy old style",13,"bold"),fg='black',bg='white')

    label3.place(x=500,y=200)

    self.content_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')

    self.content_txt.place(x=500,y=250,width=270,height=35)

    btn1=Button(frame_input,text="SEARCH NOW",command=self.searchGenreInfo,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

    btn1.place(x=550,y=10)

    btn2=Button(frame_input,text="Go back",command=self.appscreen,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

    btn2.place(x=1000,y=10)

#Search by director, actor y nombre de título AQUI PROCESAMOS LA INFO Y MOTRAMOS CONTENIDO
   def searchMiInfo(self): 
    Frame_login=Frame(self.root,bg="white")

    Frame_login.place(x=0,y=0,height=700,width=1366)

    frame_input=Frame(self.root,bg='white')

    frame_input.place(x=320,y=130,height=450,width=350)
    
    if self.search_txt.get()=="":

      try:

         if(self.search_txt.get() == '1'):
            query = ("SELECT nombre, link from contenido where nombre = %s;")
            data = (self.content_txt.get(),)
            resultadoQ = conexion.executeQuery(query,data,True)

         elif(self.search_txt.get() == '2'):
            query = ("SELECT nombre, link from contenido where nombre = %s;")
            data = (self.content_txt.get(),)
            resultadoQ = conexion.executeQuery(query,data,True)
            
         elif(self.search_txt.get() == '3'):
            query = ("SELECT nombre, link from contenido where nombre = %s;")
            data = (self.content_txt.get(),)
            resultadoQ = conexion.executeQuery(query,data,True)

         elif(self.search_txt.get() == '4'):
            query = ("SELECT nombre, link from contenido where nombre = %s;")
            data = (self.content_txt.get(),)
            resultadoQ = conexion.executeQuery(query,data,True)

         elif(self.search_txt.get() == '5'):
            query = ("SELECT nombre, link from contenido where nombre = %s;")
            data = (self.content_txt.get(),)
            resultadoQ = conexion.executeQuery(query,data,True)

         elif(self.search_txt.get() == '6'):
            query = ("SELECT nombre, link from contenido where nombre = %s;")
            data = (self.content_txt.get(),)
            resultadoQ = conexion.executeQuery(query,data,True)
            
         elif(self.search_txt.get() == '7'):
            query = ("SELECT nombre, link from contenido where nombre = %s;")
            data = (self.content_txt.get(),)
            resultadoQ = conexion.executeQuery(query,data,True)

         for x in con:
            #AQUI PONEMOS EL CONTENIDO Y EL NUMERO QUE LE VAMOS A ASIGNAR EN UN ARRAY
            label4=Label(frame_input,text=x + "." + con[x],font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

            label4.place(x=30,y=195)

         label3=Label(frame_input,text="Number of the content?",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

         label3.place(x=30,y=50)

         self.contentNumber=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')

         self.contentNumber.place(x=30,y=100,width=270,height=35)

         con = ['a','b']#MOMO: ES UN ARRAY SIMULADO, PARA QUE SE PONGA EL QUERY PARA QUE VENGA LA INFO DE LOS CONTENIDOS

         btn9=Button(Frame_login,text="GO BACK",command=self.appscreen,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

         btn9.place(x=1000,y=10)

         btn4=Button(frame_input,text="See Content",command=self.Player,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

         btn4.place(x=1000,y=50)

      except Exception as es:
         
         messagebox.showerror('Error',f'Error Due to : {str(es)}',parent=self.root)
    else:
       messagebox.showerror('Error',f'Neceistas llenar el campo')

       btn2=Button(Frame_login,text="Go back",command=self.searchMi,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

       btn2.place(x=1000,y=10)


























#Search by Genre
   def searchGenre(self):
    Frame_login=Frame(self.root,bg="white")

    Frame_login.place(x=0,y=0,height=700,width=1366)

    frame_input=Frame(self.root,bg='white')

    frame_input.place(x=320,y=130,height=450,width=350)

    label3=Label(frame_input,text="Search",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

    label3.place(x=30,y=195)

    self.search_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')

    self.search_txt.place(x=30,y=145,width=270,height=35)

    btn1=Button(Frame_login,text="SEARCH NOW",command=self.searchGenreInfo,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

    btn1.place(x=90,y=340)

    btn2=Button(Frame_login,text="Go back",command=self.appscreen,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

    btn2.place(x=1000,y=10)

#Search by Genre AQUI PROCESAMOS LA INFO Y MOTRAMOS CONTENIDO
   def searchGenreInfo(self): 
    Frame_login=Frame(self.root,bg="white")

    Frame_login.place(x=0,y=0,height=700,width=1366)
    try:

      #MOMO: USAR EL search_txt PARA LA RESPUESTA DEL SEARCH
      
      #con=psycopg2.connect(user="postgres", password="NYARLATHOTEP", host="localhost", port="5432", database="proyecto2")
      con=psycopg2.connect(user="postgres", password="123", host="localhost", port="5432", database="Proyecto2")

      #AQUI TENEMOS QUE PONER JUNTO A UN NUMERO EL TITULO QUE SE ENCONTRO DE LA BUSQUEDA PARA QUE LUEGO LE PEDIMOS QUE INGRESE UN NUMERO 
      #PARA PODER SABER QUE CONTENIDO VAMOS A REPRODUCIR

      frame_input=Frame(self.root,bg='white')

      frame_input.place(x=320,y=130,height=450,width=350)

      label3=Label(frame_input,text="Number of the content?",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

      label3.place(x=30,y=50)

      self.contentNumber=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')

      self.contentNumber.place(x=30,y=100,width=270,height=35)

      con = ['a','b']#MOMO: ES UN ARRAY SIMULADO, PARA QUE SE PONGA EL QUERY PARA QUE VENGA LA INFO DE LOS CONTENIDOS

      btn9=Button(Frame_login,text="GO BACK",command=self.appscreen,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

      btn9.place(x=1000,y=10)

      for x in con:
         #AQUI PONEMOS EL CONTENIDO Y EL NUMERO QUE LE VAMOS A ASIGNAR EN UN ARRAY
         label4=Label(frame_input,text=x + "." + con[x],font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

         label4.place(x=30,y=195)


      btn4=Button(frame_input,text="See Content",command=self.Player,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

      btn4.place(x=1000,y=50)

    except Exception as es:
      
      messagebox.showerror('Error',f'Error Due to : {str(es)}',parent=self.root)


























#Search Player
   def Player(self):
          
    frame_input=Frame(self.root,bg="white")

    label3=Label(frame_input,text="Finish the content? Y = yes N = No",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

    label3.place(x=30,y=195)

    self.Finish=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')

    self.Finish.place(x=30,y=245,width=270,height=35)

    
    if self.Finish.get()=="Y":
      #AQUI SETEAMOS QUE PUES NO SE TERMINO DE REPRODUCIR EL VIDEO
      self.appscreen()
    else:
      #AQUI SETEAMOS QUE PUES SE TERMINO DE REPRODUCIR EL VIDEO
      self.appscreen()

   def regclear(self):

    self.entry.delete(0,END)

    self.entry2.delete(0,END)

    self.entry3.delete(0,END)

    self.entry4.delete(0,END)



   def loginclear(self):

    self.email_txt.delete(0,END)

    self.password.delete(0,END)



root=Tk()

ob=Login(root)

root.mainloop()