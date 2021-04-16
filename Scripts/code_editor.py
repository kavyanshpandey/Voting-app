from  pywebio.input import*
from pywebio.output import *

idle = textarea('CODE Editor', code={
    'mode':"python",
    'theme':'dracula'
})

def A(a):
    return a

print(A(idle))