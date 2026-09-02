import datetime
def save_history(calculation):

     now = datetime.datetime.now()
     date_time = now.strftime("%d-%m-%Y | %I:%M %p")
     today_date = now.strftime("%d-%m-%Y")
     
     existing_history = read_history()

     if existing_history is None:

          with open("history.txt","a") as file:
                         file.write("===========================\n"
                         f"{date_time}\n"
                         "===========================\n")
                         file.write(calculation +"\n")
          
     elif today_date in existing_history:
          with open("history.txt","a")as file:
               file.write(calculation + "\n")

     else:
          with open("history.txt","a") as file:
               file.write("===========================\n"
               f"{date_time}\n"
               "===========================\n")
               file.write(calculation +"\n")

def read_history():
     try:

          with open ("history.txt","r") as file:
               result =file.read()
               return result
     except FileNotFoundError:
          return None
     
def clear_history():
     with open ("history.txt","w")as file:
          return file.write()


    