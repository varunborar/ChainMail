<h2> Chain Mail </h2>

<h3> Description </h3>
<p> This project can be used to send customized mails to a lot of people at once </p>
<ul>
  <li>Create a excel file with first column as email of contacts and rest coulumns for the text that you want to customize</li>
  <li>Create a text file comprisiing of custom text message to be sent in mail</li>
  <li>Start the application and load the files, login with your email and click send.</li>
</ul>

<h3> Creating Excel File </h3>
First column of the file should be named as "Email" and should not consist of any blank rows.
The other fields that are needed to customized should be named in header of each column and the corresponding row should consist of the details
for example a row for a file consisting of email, name and phone number should look like<br> 
someone@example.com Some Name 9876543210

<a href="https://github.com/varunborar/ChainMail/blob/master/contact.xlsx">See example file<a>

<h3> Creating Message Template </h3>
A message template should be saved in a Text document file (*.txt). <br>
All the fields that are to be replaced in message should be enclosed in ${Header}, where Header correspond to the column name in the excel file.

<br>
<a href="https://github.com/varunborar/ChainMail/blob/master/emailTemplate.txt"> See emaple file <a>

<h3> Dependencies </h3>

<ol>
  <li>Pandas </li>
  <li>PYQT5 </li>
  <li>Qt designer </li>
  <li>ppenpyxl / xlrd </li>
  <li>smtplib, ssl </li>
 </ol>
 
<h3> Note </h3>
By default it uses only "smtp.gmail.com" as smtp server for changing server or port use keyword arguments while creating instance of Mail class. <br>

 
