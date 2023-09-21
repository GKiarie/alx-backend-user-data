Personal Data
Personally identifiable information (PII) and personal data are two classifications of data that often cause confusion for organizations that collect, store and analyze such data. 
PII is used in the US but no single legal document defines it.
On the other hand, personal data has one legal meaning, which is defined by the General Data Protection Regulation (GDPR), accepted as law across the European Union (EU). 

******************************************************
What is personally identifiable information (PII)?
definition is provided by the National Institute of Standards and Technology (NIST):

PII is any information about an individual maintained by an agency, including (1) any information that can be used to distinguish or trace an individual‘s identity, such as name, social security number, date and place of birth, mother‘s maiden name, or biometric records; and (2) any other information that is linked or linkable to an individual, such as medical, educational, financial, and employment information.

What pieces of information are considered PII?
PII can be divided into two categories: 
-> linked information
-> linkable information.

Linked information is more direct. It could include any personal detail that can be used to identify an individual. Examples of this kind of PII include:
Full name
Home address
Email address
Social security number
Passport number
Driver’s license number
Credit card numbers
Date of birth
Telephone number
Owned properties e.g. vehicle identification number (VIN) 
Login details
Processor or device serial number* 
Media access control (MAC)*
Internet Protocol (IP) address*
Device IDs*  
Cookies*

NIST states that linked information can be “Asset information, such as Internet Protocol (IP) or Media Access Control (MAC) address or other host-specific persistent static identifier that consistently links to a particular person or small, well-defined group of people”. That means cookies and device ID fall under the definition of PII.

Linkable information is indirect and on its own may not be able to identify a person, but when combined with another piece of information could identify, trace or locate a person. 

examples of PII that can be considered linkable information:

First or last name (if common)
Country, state, city, zip code
Gender
Race
Non-specific age (e.g. 30-40 instead of 30)
Job position and workplace

What is non-PII?
Non-personally identifiable information (non-PII) is data that cannot be used on its own to trace, or identify a person.Examples of non-PII include, but are not limited to:

Aggregated statistics on the use of product / service
Partially or fully masked IP addresses

***************************************************************************
What is personal data?
Personal data is a legal term that the General Data Protection Regulation defines as the following:

‘personal data’ means any information relating to an identified or identifiable natural person (‘data subject’); an identifiable natural person is one who can be identified, directly or indirectly, in particular by reference to an identifier such as a name, an identification number, location data, an online identifier or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity of that natural person;

This definition applies not only to a person’s name and surname, but to details that could identify that person. That’s the case when, for instance, you’re able to identify a visitor returning to your website with the help of a cookie or login information. 

Under the GDPR you can consider cookies as personal data because according to:

Natural persons may be associated with online identifiers provided by their devices, applications, tools and protocols, such as internet protocol addresses, cookie identifiers or other identifiers such as radio frequency identification tags. This may leave traces which, in particular when combined with unique identifiers and other information received by the servers, may be used to create profiles of the natural persons and identify them.

And the definition of personal data covers various pieces of information such as:

transaction history
IP addresses
browser history 
posts on social media
Basically, it’s any information relating to an individual or identifiable person, directly or indirectly.

What is non-personal data?

Following the GDPR General Data Protection Regulation provisions, non-personal data is data that won’t let you identify an individual. The best example is anonymous data.

The principles of data protection should therefore not apply to anonymous information, namely information which does not relate to an identified or identifiable natural person or to personal data rendered anonymous in such a manner that the data subject is not or no longer identifiable.

Other examples of non-personal data include, but are not limited to:

Generalized data, e.i. age range e.g. 20-40
Information gathered by government bodies or municipalities such as census data or tax receipts collected for publicly funded works
Aggregated statistics on the use of a product or service
Partially or fully masked IP addresses 


*******************
Logging
*******************
Logging is a means of tracking events that happen when some software runs.
The software’s developer adds logging calls to their code to indicate that certain events have occurred
An event is described by a descriptive message which can optionally contain variable data (i.e. data that is potentially different for each occurrence of the event). Events also have an importance which the developer ascribes to the event; the importance can also be called the level or severity.

Logging provides a set of convenience functions for simple logging usage.
-> debug()
-> info()
-> warning()
-> error()
-> critical()

To determine when to use logging, see the table below, which states, for each of a set of common tasks, the best tool to use for it.

Task you want to perform    The best tool for the task

1. Display console output for ordinary usage of a command line script or program

        -> print()

2. Report events that occur during normal operation of a program (e.g. for status monitoring or fault investigation)

        -> logging.info() (or logging.debug() for very detailed output for diagnostic purposes)
3.Issue a warning regarding a particular runtime event
        -> warnings.warn() in library code if the issue is avoidable and the client application should be modified to eliminate the warning
        -> logging.warning() if there is nothing the client application can do about the situation, but the event should still be noted
4. Report an error regarding a particular runtime event

        -> Raise an exception

5. Report suppression of an error without raising an exception (e.g. error handler in a long-running server process)

        -> logging.error(), logging.exception() or logging.critical() as appropriate for the specific error and application domain

The logging functions are named after the level or severity of the events they are used to track. The standard levels and their applicability are described below (in increasing order of severity):

Level

When it’s used

DEBUG

Detailed information, typically of interest only when diagnosing problems.

INFO

Confirmation that things are working as expected.

WARNING

An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

ERROR

Due to a more serious problem, the software has not been able to perform some function.

CRITICAL

A serious error, indicating that the program itself may be unable to continue running.

The default level is WARNING, which means that only events of this level and above will be tracked, unless the logging package is configured to do otherwise.

Events that are tracked can be handled in different ways. The simplest way of handling tracked events is to print them to the console. Another common way is to write them to a disk file.

Set logging level from command-line:
--log=INFO


Log Record Attributes:
https://docs.python.org/3/library/logging.html#logrecord-attributes


******************
Resources
*****************
* https://piwik.pro/blog/what-is-pii-personal-data/
* https://docs.python.org/3/library/logging.html
* https://github.com/pyca/bcrypt/
* https://www.youtube.com/watch?v=-ARI4Cz-awo&ab_channel=CoreySchafer

***************
Objectives
*****************
Examples of Personally Identifiable Information (PII)
How to implement a log filter that will obfuscate PII fields
How to encrypt a password and check the validity of an input password
How to authenticate to a database using environment variables


*********************
0. Regex-ing
********************
Write a function called filter_datum that returns the log message obfuscated:

Arguments:
fields: a list of strings representing all fields to obfuscate
redaction: a string representing by what the field will be obfuscated
message: a string representing the log line
separator: a string representing by which character is separating all fields in the log line (message)
The function should use a regex to replace occurrences of certain field values.
filter_datum should be less than 5 lines long and use re.sub to perform the substitution with a single regex.
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))

bob@dylan:~$
bob@dylan:~$ ./main.py
name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;
bob@dylan:~$
Repo:

GitHub repository: alx-backend-user-data
Directory: 0x00-personal_data
File: filtered_logger.py


************************
1. Log formatter
***********************
Copy the following code into filtered_logger.py.

import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
Update the class to accept a list of strings fields constructor argument.

Implement the format method to filter values in incoming log records using filter_datum. Values for fields in fields should be filtered.

DO NOT extrapolate FORMAT manually. The format method should be less than 5 lines long.

bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

import logging
import re

RedactingFormatter = __import__('filtered_logger').RedactingFormatter

message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
formatter = RedactingFormatter(fields=("email", "ssn", "password"))
print(formatter.format(log_record))

bob@dylan:~$
bob@dylan:~$ ./main.py
[HOLBERTON] my_logger INFO 2019-11-19 18:24:25,105: name=Bob; email=***; ssn=***; password=***;
bob@dylan:~$
Repo:

GitHub repository: alx-backend-user-data
Directory: 0x00-personal_data
File: filtered_logger.py


************************
2. Create logger
************************
Use user_data.csv for this task

Implement a get_logger function that takes no arguments and returns a logging.Logger object.

The logger should be named "user_data" and only log up to logging.INFO level. It should not propagate messages to other loggers. It should have a StreamHandler with RedactingFormatter as formatter.

Create a tuple PII_FIELDS constant at the root of the module containing the fields from user_data.csv that are considered PII. PII_FIELDS can contain only 5 fields - choose the right list of fields that can are considered as “important” PIIs or information that you must hide in your logs. Use it to parameterize the formatter.

Tips:

What Is PII, non-PII, and personal data?: https://piwik.pro/blog/what-is-pii-personal-data/
Uncovering Password Habits: https://www.digitalguardian.com/blog/uncovering-password-habits-are-users-password-security-habits-improving-infographic

bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

import logging

get_logger = __import__('filtered_logger').get_logger
PII_FIELDS = __import__('filtered_logger').PII_FIELDS

print(get_logger.__annotations__.get('return'))
print("PII_FIELDS: {}".format(len(PII_FIELDS)))

bob@dylan:~$
bob@dylan:~$ ./main.py
<class 'logging.Logger'>
PII_FIELDS: 5
bob@dylan:~$
Repo:

GitHub repository: alx-backend-user-data
Directory: 0x00-personal_data
File: filtered_logger.py


*************************
3. Connect to secure database
******************************
Database credentials should NEVER be stored in code or checked into version control. One secure option is to store them as environment variable on the application server.

In this task, you will connect to a secure holberton database to read a users table. The database is protected by a username and password that are set as environment variables on the server named PERSONAL_DATA_DB_USERNAME (set the default as “root”), PERSONAL_DATA_DB_PASSWORD (set the default as an empty string) and PERSONAL_DATA_DB_HOST (set the default as “localhost”).

The database name is stored in PERSONAL_DATA_DB_NAME.

Implement a get_db function that returns a connector to the database (mysql.connector.connection.MySQLConnection object).

Use the os module to obtain credentials from the environment
Use the module mysql-connector-python to connect to the MySQL database (pip3 install mysql-connector-python)
bob@dylan:~$ cat main.sql
-- setup mysql server
-- configure permissions
CREATE DATABASE IF NOT EXISTS my_db;
CREATE USER IF NOT EXISTS root@localhost IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON my_db.* TO 'root'@'localhost';

USE my_db;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    email VARCHAR(256)
);

INSERT INTO users(email) VALUES ("bob@dylan.com");
INSERT INTO users(email) VALUES ("bib@dylan.com");

bob@dylan:~$ 
bob@dylan:~$ cat main.sql | mysql -uroot -p
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT COUNT(*) FROM users;" | mysql -uroot -p my_db
Enter password: 
2
bob@dylan:~$ 
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

get_db = __import__('filtered_logger').get_db

db = get_db()
cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM users;")
for row in cursor:
    print(row[0])
cursor.close()
db.close()

bob@dylan:~$
bob@dylan:~$ PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./main.py
2
bob@dylan:~$
Repo:

GitHub repository: alx-backend-user-data
Directory: 0x00-personal_data
File: filtered_logger.py



**************************************
4. Read and filter data
***********************************
Implement a main function that takes no arguments and returns nothing.

The function will obtain a database connection using get_db and retrieve all rows in the users table and display each row under a filtered format like this:

[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=e848:e856:4e0b:a056:54ad:1e98:8110:ce1b; last_login=2019-11-14T06:16:24; user_agent=Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN);
Filtered fields:

name
email
phone
ssn
password
Only your main function should run when the module is executed.

bob@dylan:~$ cat main.sql
-- setup mysql server
-- configure permissions
CREATE DATABASE IF NOT EXISTS my_db;
CREATE USER IF NOT EXISTS root@localhost IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON my_db.* TO root@localhost;

USE my_db;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    name VARCHAR(256), 
        email VARCHAR(256), 
        phone VARCHAR(16),
    ssn VARCHAR(16), 
        password VARCHAR(256),
    ip VARCHAR(64), 
        last_login TIMESTAMP,
    user_agent VARCHAR(512)
);

INSERT INTO users(name, email, phone, ssn, password, ip, last_login, user_agent) VALUES ("Marlene Wood","hwestiii@att.net","(473) 401-4253","261-72-6780","K5?BMNv","60ed:c396:2ff:244:bbd0:9208:26f2:93ea","2019-11-14 06:14:24","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36");
INSERT INTO users(name, email, phone, ssn, password, ip, last_login, user_agent) VALUES ("Belen Bailey","bcevc@yahoo.com","(539) 233-4942","203-38-5395","^3EZ~TkX","f724:c5d1:a14d:c4c5:bae2:9457:3769:1969","2019-11-14 06:16:19","Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30");

bob@dylan:~$ 
bob@dylan:~$ cat main.sql | mysql -uroot -p
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT COUNT(*) FROM users;" | mysql -uroot -p my_db
Enter password: 
2
bob@dylan:~$ 
bob@dylan:~$ PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./filtered_logger.py
[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=60ed:c396:2ff:244:bbd0:9208:26f2:93ea; last_login=2019-11-14 06:14:24; user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36;
[HOLBERTON] user_data INFO 2019-11-19 18:37:59,621: name=***; email=***; phone=***; ssn=***; password=***; ip=f724:c5d1:a14d:c4c5:bae2:9457:3769:1969; last_login=2019-11-14 06:16:19; user_agent=Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30;
bob@dylan:~$
Repo:

GitHub repository: alx-backend-user-data
Directory: 0x00-personal_data
File: filtered_logger.py



*******************************************
5. Encrypting passwords
*******************************************
User passwords should NEVER be stored in plain text in a database.

Implement a hash_password function that expects one string argument name password and returns a salted, hashed password, which is a byte string.

Use the bcrypt package to perform the hashing (with hashpw).

bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

hash_password = __import__('encrypt_password').hash_password

password = "MyAmazingPassw0rd"
print(hash_password(password))
print(hash_password(password))

bob@dylan:~$
bob@dylan:~$ ./main.py
b'$2b$12$Fnjf6ew.oPZtVksngJjh1.vYCnxRjPm2yt18kw6AuprMRpmhJVxJO'
b'$2b$12$xSAw.bxfSTAlIBglPMXeL.SJnzme3Gm0E7eOEKOVV2OhqOakyUN5m'
bob@dylan:~$
Repo:

GitHub repository: alx-backend-user-data
Directory: 0x00-personal_data
File: encrypt_password.py



***********************************
6. Check valid password
********************************
Implement an is_valid function that expects 2 arguments and returns a boolean.

Arguments:

hashed_password: bytes type
password: string type
Use bcrypt to validate that the provided password matches the hashed password.

bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

hash_password = __import__('encrypt_password').hash_password
is_valid = __import__('encrypt_password').is_valid

password = "MyAmazingPassw0rd"
encrypted_password = hash_password(password)
print(encrypted_password)
print(is_valid(encrypted_password, password))

bob@dylan:~$
bob@dylan:~$ ./main.py
b'$2b$12$Fnjf6ew.oPZtVksngJjh1.vYCnxRjPm2yt18kw6AuprMRpmhJVxJO'
True
bob@dylan:~$
Repo:

GitHub repository: alx-backend-user-data
Directory: 0x00-personal_data
File: encrypt_password.py



***************************************
End
*****************************