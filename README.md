# O365API---Sending-Email
Automate sending html based Email using O365 API

Please follow the process:

1. Register you app to use the O365 API. Follow the link https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade
2.Create an app. Set a name.
3.In Supported account types choose "Accounts in any organizational directory and personal Microsoft accounts (e.g. Skype, Xbox, Outlook.com)", if you are using a personal account.
4.Set the redirect uri (Web) to: https://login.microsoftonline.com/common/oauth2/nativeclient and click register. This is the default redirect uri used by this library, but you can use any other if you want.
5. Write down the Application (client) ID. You will need this value.
6.Under "Certificates & secrets", generate a new client secret. Set the expiration preferably to never.
7. Write down the value of the client secret created now. It will be hidden later on.
8.Under Api Permissions add the delegated permissions for Microsoft Graph you want (see scopes), as an example, to read and send emails use:
Mail.ReadWrite
Mail.Send
User.Read 

#Using the code :

Please look into the python file where I have demonstrated how we can add html code to send html mails. I have used tables as an example.

m.to.add() - method for the recepients.
m.subject() - to add subject
m.send() - to send email

Please note this can be integrated with the servicenow automation which I had demostrated in my past publications.


Thanks for reading :)

