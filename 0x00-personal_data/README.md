Personal Data
Personally identifiable information (PII) and personal data are two classifications of data that often cause confusion for organizations that collect, store and analyze such data. 
PII is used in the US but no single legal document defines it.
On the other hand, personal data has one legal meaning, which is defined by the General Data Protection regulation (GDPR), accepted as law across the European Union (EU). 

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

What is personal data?
Personal data is a legal term that the GDPR defines as the following:

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

Following the GDPR provisions, non-personal data is data that won’t let you identify an individual. The best example is anonymous data.

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

3. Issue a warning regarding a particular runtime event

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