import smtplib

hostname='smtp.gmail.com'
email='ashiverma1917@gmail.com'
password='ksid ylvh gsmb vidz'

with smtplib.SMTP(host=hostname) as connection:
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs=email,
        msg=f'Subject:Test Python Email\n\n hii ashii , going great!'
    )