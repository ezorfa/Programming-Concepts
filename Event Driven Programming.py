# Example of a event driven programming using a small applicaiton: Chat Bot!
# Author: Mohammed Afroze

class MessageBot:
  def __init__(self):
    self.callbacksDict = {}
    self.registerCallback("Hi", self.respond_to_hi) # Define the function
    self.registerCallback("Hello", self.respond_to_hello) # Define the function
    self.registerCallback("How are you", self.respond_to_HowYou) # Define the function
  
  def registerCallback(self, msg, fn):
    if msg not in callbacksDict:
      callbacksDict[msg] = fn
  
  def reply_to_message(self,msg):
    if msg not in self.callbacksDict:
      return "I dont understand your message"
    return self.chooseCallback(msg)()    

  def chooseCallback(self,msg):
    return callbacksDict[msg]


def main():
  bot = MessageBot()
  bot.reply_to_message("Hi!")
  bot.reply_to_message("Good Morning")
  bot.reply_to_message("How are you doing?")
