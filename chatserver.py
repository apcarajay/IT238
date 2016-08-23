# Tcp Chat server

from Tkinter import * 
import socket, select

def main():
    print("Running GUI Demo")

    # Instantiate class for UI
    ui = App()
    
    # Run the UI, and capture CTRL-C to terminate
    try:
        ui.start()
    except KeyboardInterrupt:
        print("Caught CTRL-C, shutting down client")
        ui.eventDeleteDisplay()
    
    print("GUI Demo exiting")

class App():

    def __init__(self):
        self.first_click = True;

    def start(self):
        print("Starting clientUI...")

        self.master = Tk()
        self.master.title("PORT NUMBER")
       
        self.portno = Label(self.master, text="Port:")
        self.portno.grid(row=1,column=0)

        self.usertext = StringVar()
        self.myentry = Entry(self.master, textvariable=self.usertext)
        self.myentry.grid(row=1, column=1)

        self.mybutton = Button(self.master, text="Enter", command=self.printMessage)
        self.mybutton.grid(row=2, column=1)

        self.counter = 0
        self.master.mainloop()

    def printMessage(self):
        PORT = int(self.usertext.get())
       
        self.counter = self.counter+1;

        if self.counter>=1:
          self.mybutton.config(state=DISABLED)
        
        
        # List to keep track of socket descriptors
        CONNECTION_LIST = []
        RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
           
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # this has no effect, why ?
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR , 1)
        server_socket.bind(("0.0.0.0", PORT))
        server_socket.listen(10)
     
        # Add server socket to the list of readable connections
        CONNECTION_LIST.append(server_socket)
     
        print "Chat server started on port " + str(PORT)
     
        while 1:
            # Get the list sockets which are ready to be read through select
            read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
     
            for sock in read_sockets:
                #New connection
                if sock == server_socket:
                    # Handle the case in which there is a new connection recieved through server_socket
                    sockfd, addr = server_socket.accept()
                    CONNECTION_LIST.append(sockfd)
                    print "Client (%s, %s) connected" % addr
                     
                    broadcast_data(sockfd, "[%s:%s] entered room\n" % addr)
                 
                #Some incoming message from a client
                else:
                    # Data recieved from client, process it
                    try:
                        #In Windows, sometimes when a TCP program closes abruptly,
                        # a "Connection reset by peer" exception will be thrown
                        data = sock.recv(RECV_BUFFER)
                        if data:
                            broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)                
                     
                    except:
                        broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                        print "Client (%s, %s) is offline" % addr
                        sock.close()
                        CONNECTION_LIST.remove(sock)
                        continue
         
        server_socket.close()


        # Event handler - User closed program via window manager or CTRL-C
    def eventDeleteDisplay(self):
        print("UI: Closing")

        # Continuing closing window now
        self.master.destroy()
        

    #Function to broadcast chat messages to all connected clients
    def broadcast_data (sock, message):
        #Do not send the message to master socket and the client who has send us the message
        for socket in CONNECTION_LIST:
            if socket != server_socket and socket != sock :
                try :
                    socket.send(message)
                except :
                    # broken socket connection may be, chat client pressed ctrl+c for example
                    socket.close()
                    CONNECTION_LIST.remove(socket)
     
    #def startConnect(self):
     
        

if __name__ == "__main__":
    sys.exit(main())