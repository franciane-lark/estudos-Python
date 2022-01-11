!pip install pyautogui
!pip install pyperclip
#https://pyautogui.readthedocs.io/en/latest/quickstart.html

# Passo a passo para resolver o nosso desafio
import pyautogui
import pyperclip
import time
# tempo/delay
pyautofran.PAUSE = 1

# Passo 1: Entrar no sistema da empresa (link do drive)
pyautogui.hotkey("ctrl","t") # abrindo uma aba
pyperclip.write("https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbWVLMnkxRDBuekZ0NHFXUkNUdEU4NFY3c09MUXxBQ3Jtc0ttNWFfSWI3TzdSRk1lVG5veUszZ1BadUpPMHZNOVFKbHM5Nm5KbUNOV3RWX2UxX0Z0N1dOX1VYaUlTekVNNnQ2NWpKZkw2c2pIT1NzS1drUDFMMzc0Y2txeUF4Vm4zM0Z2ZVdXa09LNFhhZGpKTWVhdw&q=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F149xknr9JvrlEnhNWO49zPcw0PW5icxga%3Fusp%3Dsharing") # copiando o link
pyautogui.hotkey("ctrl","v") # colando o link
pyperclip.press("enter") # entrando no sistema

# Passo 2: Navegar no Sistema (até a pasta Expotar)
time.sleep(5)
# Passo 3: Fazer Download da base de vendas
pyautogui.click(x=974, y=676) # clicar no arquivo
pyautogui.click(x=3339,y=404 ) # clicar nos 3 pontos
pyautogui.click(x=2890,y=1406) # clicar em fazer download

time.sleep(5) # esperar o download
# Passo 4: Importar a base de vendas pro Python

# Passo 5: Calcular o faturamento e quantidade de produtos vendidos (os indicadores)

# Passo 6: Enviar email para diretoria
