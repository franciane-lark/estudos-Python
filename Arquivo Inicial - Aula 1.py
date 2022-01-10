!pip install pyautogui
!pip install pyperclip
#https://pyautogui.readthedocs.io/en/latest/quickstart.html

# Passo a passo para resolver o nosso desafio
import pyautogui
import pyperclip

# tempo/delay
pyautofran.PAUSE = 1

# Passo 1: Entrar no sistema da empresa (link do drive)
pyautogui.hotkey("ctrl","t") # abrindo uma aba
pyautogui.write("https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbWVLMnkxRDBuekZ0NHFXUkNUdEU4NFY3c09MUXxBQ3Jtc0ttNWFfSWI3TzdSRk1lVG5veUszZ1BadUpPMHZNOVFKbHM5Nm5KbUNOV3RWX2UxX0Z0N1dOX1VYaUlTekVNNnQ2NWpKZkw2c2pIT1NzS1drUDFMMzc0Y2txeUF4Vm4zM0Z2ZVdXa09LNFhhZGpKTWVhdw&q=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F149xknr9JvrlEnhNWO49zPcw0PW5icxga%3Fusp%3Dsharing") # copiando o link
pyautogui.hotkey("ctrl","v") # colando o link
pyautogui.press("enter") # entrando no sistema

# Passo 2: Navegar no Sistema (até a pasta Expotar)

# Passo 3: Fazer Download da base de vendas

# Passo 4: Importar a base de vendas pro Python

# Passo 5: Calcular o faturamento e quantidade de produtos vendidos (os indicadores)

# Passo 6: Enviar email para diretoria