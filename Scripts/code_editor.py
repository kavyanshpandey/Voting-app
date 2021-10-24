from  pywebio.input import*
from pywebio.output import *

idle = textarea('CODE EDITOR', code={
    'mode':"python",
    'theme':'dracula'
})

def B(a):
    return a

print(B(idle))
