  #This is your SRPN file. Make your changes here.

def process_command(command):
    if command == "=":
        return "0"
    else:
        return None


#This is the entry point for the program.
#Do not edit the below
if __name__ == "__main__": 
    while True:
        try:
            cmd = input()
            pc = process_command(cmd)
            if pc != None:
                print(str(pc))
        except:
            exit()
