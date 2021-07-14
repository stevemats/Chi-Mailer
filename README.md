#  [ℭ𝔥𝔦-𝔐𝔞𝔦𝔩𝔢𝔯](https://stevemats.github.io/Chi-Mailer/)

### About:

Chi_Mailer is a free open source bulk email software. With it you can forget the hustle of having to send messages an email after another on a scenarion where you have a large list of emails to send a message to. Writing E-mails is quite tasking as time has become a very valuable resource when it comes to businesses and enterprises.
With Chi-Mailer, all you have to do, is write your message and then easily automate it to all your target emails with one command. How cool is that! :)

# New Features!
 - Ability to send bulk/mass emails
 - Input your server's credential at script startup so that you don't have to stress yourself with script alteration.
 - Hides Server passwords at input.
 - Ability to use the script with or with no python knowledge.
 
# Installation & Usage
chi_mailer requires [python3+](https://python.org/) at the moment

## Linux users:

Run the following command in the project's root folder via terminal(.i.e after
extracting chi_mailer, open the chi_mailer folder and right-click to open the
terminal, that way you'll be in the projects root folder and type python Qi.py)
```
Method 2:
$ git clone https://github.com/stevemats/chi_mailer.git
   Now Change directory using the 'cd' command to enter into the project's folder
$ cd chi_mailer         (To enter into the project's directory)
$ ls                    (To view the content in the directory)
$ python3 Qi.py
```
## Windows users:

Method 1
After extracting the chi_mailer download, double click to enter to the project's
root folder, and hold shift and right click to open powershell or cmd(command prompt)
```
Method 2:
Open your command prompt via startbar and type the following:
>git clone git clone https://github.com/stevemats/chi_mailer.git
   Now Change directory using the 'cd' command to enter into the project's folder
> cd downloads
> ls                    (To view the content in the directory)
> cd chi_mailer         (Change directory to ch_mailer folder)
> python3 Qi.py         (run our python script)
```

The message.txt is where your message should be put as a simple and fast way of calling our message  which uses a concept known as templating string within our document from the script and avoiding code alteration.
The mass mails where the message will be sent to should be put in contacts.txt    document following the sample.txt format.

## Contribution

The project is open for contribution.

### Todos

 - Convert all user input mails to lowercase. (Humans are prone to errors/typos)
 - Set all mails as high priority
 - Support most of the servers 
 - Time interval to enable code to send mails and repeat again after a certain time
 - Code Compatibility to enable all users(both py2 and py3 users) to use the script.

License
----

[MIT license](https://opensource.org/licenses/MIT)

N.B.// _The server mail needs to be given privilege for your script to act as a stand alone,
        visit( https://myaccount.google.com/security ) and enable less secure apps to give your
        script power. Mail server is set to use gmail at default._


                   **Stay Safe and Enjoy Your New free Mass Mailer!**
