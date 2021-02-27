import pandas


class ExcelReader:
    def __init__(self, ExcelFilePath):

        self.ExcelFilePath = ExcelFilePath


    def createHeaders(self, *vargs, sheetName = "Sheet1"):
        file = pandas.ExcelFile(self.ExcelFilePath)
        sheet = file.parse(sheetName)
        self.rows,self.columns = sheet.shape
        # print(self.rows)
        # Headers 
        self.Headers = []
        for header in list(sheet.columns):
            self.Headers.append(header)
        
        return self.Headers

    def retContact(self, rowNumber = 1, *vargs, sheetName = "Sheet1"):
        file = pandas.ExcelFile(self.ExcelFilePath)
        sheet = file.parse(sheetName)
        return list(sheet.iloc[rowNumber])


class MailTemplate:

    def __init__(self, MailTemplatePath, Headers):
        self.MailTemplatePath = MailTemplatePath
        self.Headers = Headers

        for no in range(len(self.Headers)):
            self.Headers[no] = r"${" + self.Headers[no] + r"}"

        Template = open(MailTemplatePath,"r")
        self.message = Template.read()

    def createMessage(self, contactDetails):
        
        newMessage = self.message
        for no in range(len(self.Headers)):
            newMessage = newMessage.replace(self.Headers[no], str(contactDetails[no]))
        
        return newMessage
 


if __name__ == "__main__":

    reader = ExcelReader()
    Headers = reader.createHeaders("some path")
    textReader = MailTemplate("some path", Headers)
    for row in range(reader.rows):
        details = reader.retContact(row)
        print(textReader.createMessage(details))

    

        




        


