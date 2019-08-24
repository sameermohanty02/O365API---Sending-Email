from O365 import Account

credentials = ('client_id', 'client_secret')

account = Account(credentials)
m = account.new_message()
m.to.add('to_example@example.com')
m.subject = 'Testing!'
m.body = """<html><p>Hello Leads,<br><br>Please find the ticket list :</p><table border="1">
<tr><th>Ticket</th><th>Queue</th><th>Open Duration</th></tr>"""
m.send()