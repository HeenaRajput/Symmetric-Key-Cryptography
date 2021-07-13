
# importing all libraries

#Libraries and modules for creating GUI applicaions
from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import messagebox

#libraries for cryptography
from Crypto.Cipher import AES
from Crypto import Random

global iv
iv=Random.new().read(AES.block_size)
#Generating initialization Vector





def encryption():
#try block to handle exception
  try:
    file=filedialog.askopenfile(mode='r',filetype=[('jpg file','*.jpg'),('png file','*.png')])
    #taking input from user
    if file is not None:

        file_name=file.name
        #generating key

        global key
        temp1 = entry1.get(1.0,END)
        temp1=temp1*16
        temp=bytes(temp1,'utf-8')
        fin=open("keyfile.bin",'wb')
        fin.write(temp)
        fin.close()

        fin=open('keyfile.bin','rb')
        #AES block size is 16 bytes
        # 16 bytes are read from the file

        key=fin.read(AES.block_size)
        fin.close()
        
        
        
        inputfile=open(file_name,"rb" )
        #open  file for reading purpose
        inputdata=inputfile.read()
        #storing image data into variable "inputdata"
        

        inputfile.close()

        cipher=AES.new(key,AES.MODE_CFB,iv)
        enc_data=cipher.encrypt(inputdata)
        encfile=open("encrypted2.jpg","wb")
        #writing encrypted data into "encrypted.enc file"
        encfile.write(enc_data)
        encfile.close()

       
        #showing user "Encryption done" message
        messagebox.showinfo("Information","Encryption Done")


        

  except Exception as e:
     print('Error caught :',e)
     #print the exception if any occurs




def decryption():
  try:
        
        temp1 = entry2.get(1.0,END)
        temp1=temp1*16
        temp=bytes(temp1,'utf-8')
        fin=open("keyfile2.bin",'wb')
        fin.write(temp)
        fin.close()     

        fin=open('keyfile2.bin','rb')
        k=fin.read(AES.block_size)
        fin.close()
        if(key==k):
        # opening encrypted file

          encfile2=open("encrypted2.jpg","rb")
          encdata2=encfile2.read()
          encfile2.close()
          decipher=AES.new(key,AES.MODE_CFB,iv)

          #decrypting data of encrypted file
          plain_data=decipher.decrypt(encdata2)
          outputfile=open("output3.jpg","wb")

          #writing decrypted data into "output3.jpg" file
          outputfile.write(plain_data)
          outputfile.close()

          #display message "decryption done"
          messagebox.showinfo("Information","Decryption Done")
        
        else:
              #prints message if key entered is not correct as was used while encryption
               messagebox.showinfo("Information","Wrong key entered")

  #printing exception if occured
  except Exception as e:
      print("Error occured:",e)




#creates a main window object
root=Tk(className='Visual Cryptography using AES')
root.geometry("360x360")
root.configure(bg="#66ffcc")


#Displaying title
title="VISUAL CRYPTOGRAPHY"
msgtitle=Message(root,text=title)
msgtitle.config(font=('helvetica',17,'bold'),bg='#66ffcc',fg='black',width=200)
msgtitle.pack()


#Displaying title1
title1="(Image Encryption and Decryption)"
msg=Message(root,text=title1)
msg.config(font=('helvetica',10),bg='#66ffcc',fg='black',width=200)
msg.pack()


#Button for encryption
button1=Button(root,text="Encrypt",bg='black',fg='white',command=encryption,width=25,height=2)
button1.place(x=80,y=150)
#button1.pack(side=LEFT)  
entry1 =Text(root,height=1,width=20)
entry1.place(x=80,y=120)   
  


#Button for decryption
button2=Button(root,text="Decrypt",bg='black',fg='white',command=decryption,width=25,height=2)
#button2.pack(side=RIGHT)
button2.place(x=80,y=230)

entry2 =Text(root,height=1,width=20)
entry2.place(x=80,y=200) 




root.mainloop()




