class Person:

    # --Constructor--
    def __init__(self, FirstName, Email=None):  # Overloaded
        # Instance Attributes
        self.FirstName = FirstName
        self.Email = Email

        # --Methods--

    def ToString(self):
        return self.FirstName + ', ' + str(self.Email)


# --End of class--

objP1 = Person("Bob", "BSmith@GoMail.com")
objP2 = Person("Sue")
print(objP1.ToString())
print("-------------")
print(objP2.ToString())
