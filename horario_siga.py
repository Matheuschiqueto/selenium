import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Carrega email e senha do arquivo .env
load_dotenv()
EMAIL = os.getenv("SIGA_EMAIL")
SENHA = os.getenv("SIGA_SENHA")

URL_SIGA = "https://siga.cps.sp.gov.br/sigaaluno/app.aspx"

# Abre o Chrome (Selenium 4 baixa o driver sozinho)
navegador = webdriver.Chrome()
navegador.maximize_window()
espera = WebDriverWait(navegador, 180)  # até 3 min de espera

# Passo 1: abrir o portal
navegador.get(URL_SIGA)

# Passo 2: clicar no botao inicial de acesso
botao_inicial = espera.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="GRID"]/div/div[1]/div/div[2]/div[1]'))
)
botao_inicial.click()

# Passo 3: preencher email e avancar
campo_email = espera.until(EC.element_to_be_clickable((By.ID, "i0116")))
campo_email.send_keys(EMAIL)
espera.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]'))).click()

# Passo 4: preencher senha e iniciar sessao
campo_senha = espera.until(EC.element_to_be_clickable((By.ID, "i0118")))
campo_senha.send_keys(SENHA)
espera.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]'))).click()

# Passo 5: aguardar voce confirmar o 2FA no celular
print(">> Aprove o codigo no celular. Aguardando...")
espera.until(EC.url_contains("sigaaluno"))  # segue sozinho ao logar
print(">> Logado! Selenium retomou o controle.")

# Passo 6: clicar em "Meu Curso"
meu_curso = espera.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="FOOTER"]/div/div[1]/div[1]/center'))
)
meu_curso.click()

# Passo 7: clicar em "Horário"
horario = espera.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="GRID"]/div/section/div[3]'))
)
horario.click()
print(">> Tela de horários aberta.")

# Passo 8: deixar aberto para mostrar
input(">> ENTER para fechar...")
navegador.quit()
