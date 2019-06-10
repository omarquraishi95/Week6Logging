import logging,random

logging.basicConfig(filename='test.log', level=logging.INFO,format='%(levelname)s:%(message)s')


class Company:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName=lastName

        if self.firstName != "" or self.lastName != "":
            logging.info("You have added  {} {} into the employee database; Email: {}".format(self.firstName,self.lastName,self.generateEmail()))
        elif self.firstName == "" or self.lastName == "":
            logging.warning("You have added  {} {} into the employee database; Email: {}".format(self.firstName,self.lastName,self.generateEmail()))


    def newEmployee(self):
        return '{} {} was added in the employee database'.format(self.firstName,self.lastName)

    def generateID(self):
        id = self.firstName[0] + self.lastName + random.sample(random.randint(10),1)

        return 'Hello {} {}, your id number is {}'.format(self.firstName,self.lastName,id)

    def generateEmail(self):
        email = "{}.{}@python.com".format(self.firstName,self.lastName)
        return 'Hello {} {}, your email address is {}'.format(self.firstName,self.lastName,email)



employee1 = Company("John","Jones")

