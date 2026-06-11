# Horário das aulas no SIGA com Selenium

Script simples em Python que usa **Selenium** para acessar o portal do SIGA
e navegar automaticamente até a tela de horário de aula.

O login na Microsoft é feito automaticamente; a confirmação em duas etapas (2FA)
você aprova no celular e o script segue sozinho.

## Requisitos

- Python 3
- Google Chrome instalado
- Bibliotecas:

```bash
pip3 install selenium python-dotenv
```

## Configuração

Crie um arquivo `.env` na pasta do projeto com suas credenciais:

```
SIGA_EMAIL=seu.email@aluno.cps.sp.gov.br
SIGA_SENHA=suasenha
```

> O `.env` não é versionado (está no `.gitignore`).

## Como rodar

```bash
python3 horario_siga.py
```

1. O Chrome abre no portal do SIGA.
2. Email e senha são preenchidos automaticamente.
3. **Aprove o 2FA no celular** — o script aguarda e continua sozinho.
4. Navega até a tela de horário (Meu Curso → Horário).
5. Aperte ENTER no terminal para fechar.
