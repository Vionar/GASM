# GASM
GASM - GUI Apache2 Server Manager

Version: tm-0.1

Works **only on Linux**

# What it is?
GASM is GUI Apache2 server manager. It helps you work with apache2. It has low functional now, but soon it will grow up.

You can already now:
- Start, restart, turn off apache2
- Create virtual hosts just in one click
- See list of already created hosts

It needs python3 and apache2 pre-installed

# Get started

### > You have to know
It's very stupid application and all of it's functional is now under develpment

To get started you'll need **pre-installed apache2**

For some commands, such as creating folders and giving the program access to them you'll need to **enter sudo password**. So **check the terminal line**.

### > Donwload and install

Git code:

``git clone https://github.com/Vionar/GASM.git``

Go to directory:

``cd GASM``

Open the programm:

``python3 main.py``

That's all! You can now use GASM!

### > Python libs

GASM uses simple python **libs**, which are **already pre-installed with python**:
- sys, os
- tkinter

You don't need to install them.

However, if you somehow don't have tkinter pre-installed, you can install manually

**For Debian-based Linux:**

``sudo apt-get install python-tk``


**For Arch-based Linux:**

``sudo pacman -S tk``


**For Fedora-based Linux:**

``sudo dnf install python3-tkinter``


**For RHEL, CentOS, Oracle Linux:**

``sudo yum install -y tkinter tk-devel``
