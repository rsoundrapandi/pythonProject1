# from PIL import Image

# Image = Image.open("C:\\Users\\Public\\Pictures\\Sample Pictures\\Desert.jpg")
# rotate= Image.rotate(45)
# Image.save("C:\\Users\\Public\\Pictures\\Sample Pictures\\Desert2.jpg")


# import smtplib
# from email.message import EmailMessage
# email=EmailMessage()
# email['from'] = 'rsoundrapandi@gmail.com'
# email['to'] = 'rsoundrapandi@gmail.com'
# email['subject'] = 'I am a bot'
# email.set_content('This is a bot email')
#
# with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('rsoundrapandi@gmail.com','Easwari@123')
#     smtp.send_message(email)
#     print('Mail sent')


# import requests
# url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"
# querystring = {"country":"India"}
# headers = {'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",'x-rapidapi-key': "06caedb4ecmsha598b4fa137ab19p19771cjsne879c4977c8f"}
# response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.text)


import PyPDF2

temp = PyPDF2.PdfFileReader(open('C:\\Users\\gkalivar\\Desktop\\pdf\\dummy.pdf', 'rb'))
water = PyPDF2.PdfFileReader(open('C:\\Users\\gkalivar\\Desktop\\pdf\\wtr.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

for i in range(temp.getNumPages()):
    page = temp.getPage(i)
    page.mergePage(water.getPage(0))
    output.addPage(page)

with open('C:\\Users\\gkalivar\\Desktop\\pdf\\watermarked_output.pdf', 'wb') as file:
    output.write(file)
