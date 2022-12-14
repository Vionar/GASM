# P.S. Я давно хотел это сделать. Эту программу я буду доробатывать.
from tkinter import *
from tkinter import ttk
import sys, os
from stat import S_IREAD, S_IRGRP, S_IROTH

window = Tk()
window.geometry('700x800')
window.title('Create Virtual Hosts APACHE2')



def startApache():
	os.system('sudo systemctl start apache2')
	os.system('sudo service apache2 start')
	print('> Apache started!')
	btn_start['text'] = 'Apache2 запущен'

	def reloadApache():
		os.system('sudo systemctl reload apache2')
		os.system('sudo service apache2 restart')
		print('> Apache reloaded!')

	btn_reload = Button(
		text = 'Перезапустить Apache2',
		font = ('Arial', 14),
		borderwidth = 0,
		relief = 'flat',
		bg = '#c5c5c5',
		command = reloadApache
	)
	btn_reload.place(x = 0, rely = 0, relwidth = 1)


btn_start = Button(
	text = 'Запустить Apache2',
	font = ('Arial', 14),
	borderwidth = 0,
	relief = 'flat',
	bg = '#c5c5c5',
	command = startApache
)
btn_start.place(x = 0, y = 0, relwidth = 1)


pipe = os.popen('ls /etc/apache2/sites-available')


hosts = Label(
	text = f'Доступные виртуальные хосты:\n {pipe.read()}',
	font = ('Arial', 14),
)
hosts.place(relx=0, y=80, relwidth = 1)


txt_createHostTitle = Label(text = f'Создать новый хост',font = ('Arial', 15))
txt_createHostTitle.place(x = 5, y = 400, relwidth = 1)

txt_createHost = Label(text = f'Введите название (example.domain)',font = ('Arial', 14))
txt_createHost.place(x = 5, y = 450, relwidth = 1)


entry = Entry(
	font = ('Arial', 14),
)
entry.place(x= 5, y= 500, relwidth = 1)


def createHost():
	name = entry.get()
	os.system(f'sudo mkdir -p /var/www/{name}/')
	os.system(f'sudo chown -R $USER:$USER /var/www/{name}/')
	os.system(f'sudo chmod -R 755 /var/www/')

	mainHtml = open(f'/var/www/{name}/index.html', 'w')
	mainHtml.write(f'''
		<!DOCTYPE html>
		<html>
			<head>
				<title>Welcome to your new site!</title>
			</head>
			<body>
				<h1>Welcome to your new website!</h1>
				<p>We feel that something great will soon going on on <a href="{name}">{name}</a> ;)</p>
			</body>
		</html>
	''')
	mainHtml.close()

	os.system(f'sudo chmod 777 /etc/apache2/sites-available')
	confFile = open(f'/etc/apache2/sites-available/{name}.conf', 'w')
	confFile.write(f'''
		<VirtualHost *:80>
			ServerAdmin admin@invs.ru
			ServerName {name}
			DocumentRoot /var/www/{name}/
		</VirtualHost>
	''')
	confFile.close()

	os.system(f'sudo a2ensite {name}.conf')
	os.system('sudo service apache2 restart')
	os.system('sudo systemctl reload apache2')

	isdoneText['text'] = f'Создан новый домен: {name}'


btn_create = Button(
	text = 'Создать домен',
	font = ('Arial', 14),
	borderwidth = 3,
	command = createHost
)
btn_create.place(x= 5, y= 550, relwidth = 1)

isdoneText = Label(
	text = '',
	font = ('Arial', 14)
)
isdoneText.place(x= 5, y = 630, relwidth = 1)


window.mainloop()
# Только не крадите мой код, пожалуйста.