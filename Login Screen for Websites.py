import os 
from time import sleep

print("---TELA LOGIN SITE QUALQUER---")

senha = ""
email = ""

def limpar_tela(): 
    os.system("Cls")

while True:
    try:
        escolha = int(input(
            "PAINEL\n[1] - Criar conta\n[2] - Entrar na conta\n[3] - Sair (Salvar dados)\n[4] - Sair (Sem salva dados)\nEscolha: "
        ))
        limpar_tela()

        if escolha == 1:
            while True:
                print (
                    "Criando conta..."
                )
                email_conta_criada = input(
                    "Digite seu email: "
                    ).strip().lower()
                try: 
                    if email_conta_criada[0] is "@" or "": 
                        limpar_tela()
                        print (
                            "Seu email não existe, tente um email válido."
                        )
                        sleep(1)
                        limpar_tela()
                        continue
    
                except IndexError:
                    print (
                        "Digite algo."
                    )

                if "@gmail.com" not in email_conta_criada:
                    limpar_tela()
                    print(
                        "Seu email está faltando '@gmail.com'. Tente Novamente."
                        )
                    sleep(1)
                    limpar_tela()
                    continue
                email += email_conta_criada
                break

            while True:
                senha_conta_criada = input(
                    "Digite uma senha: "
                    )
                if len(senha_conta_criada) <= 4:
                    limpar_tela()
                    print(
                        "Sua senha deve ter mais de 4 caracteres. Tente Novamente."
                        )
                    sleep(1)
                    limpar_tela()
                    continue

                if "@" not in senha_conta_criada and "#" not in senha_conta_criada:
                    limpar_tela()
                    print (
                        "Sua senha deve ter um caractere especial como '@ ou #'. Tente novamente."
                    )
                    sleep(1)
                    limpar_tela()
                    continue

                senha += senha_conta_criada
                limpar_tela()
                break 
                
            print("Conta Criada com Sucesso!")

        elif escolha == 2:
            if email == "" or senha == "":
                limpar_tela()
                print(
                    "Você não possui dados cadastrados. Crie uma conta."
                    )
                sleep(1)
                limpar_tela()
                continue

            print (
                "Entrando na conta..."
            )
            email_login = input(
                "Digite seu email: "
                )
            senha_login = input(
                "Digite sua senha: "
                )

            if email_login == email and senha_login == senha:
                limpar_tela()
                print("Logado(a) com sucesso!")
            else:
                limpar_tela()
                print("Email ou senha incorretos.")

        elif escolha == 3:
            limpar_tela()
            while True:
                print (
                    "Fora do site..."
                )
                escolha_voltar_site = input(
                        "Deseja entrar no site novamente? [s/n]: "
                        ).strip().lower()
                if escolha_voltar_site == "s":
                        limpar_tela()
                        break
                elif escolha_voltar_site == "n":
                    limpar_tela()
                    print(
                        "Você escolheu sair. Encerrando..."
                        )
                    sleep(2)
                    limpar_tela()
                else:
                    limpar_tela()
                    print(
                        "Opção inválida. Voltando ao menu principal."
                    )  
                    sleep(1)
                    limpar_tela()
                    break

        elif escolha == 4:
            print("Saindo... SEM SALVAR OS DADOS!")
            break

        else:
            limpar_tela()
            print("Escolha uma opção válida.")
            sleep(1)
            limpar_tela()

    except ValueError: 
        limpar_tela()
        print("Escolha sua opção em forma numérica.")
        sleep(1)
        limpar_tela()