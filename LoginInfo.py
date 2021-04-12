class LoginInfo:
  def __init__(self, siteName, login):
    self.__siteName = siteName
    self.__login = login
    self.__password=None
  def getSiteName(self):
    return self.__siteName
  def getLogin(self):
    return self.__login
  def getPassword(self):
    return self.__password
  def setPassword(self,password):
    self.__password=password
  
  

h=(LoginInfo("google.com","hunter"))
print(h)
print(h.getSiteName())
