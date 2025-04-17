import os 
from time import sleep

def limpar_tela(): 
    os.system("Cls")

print("---TELA LOGIN SITE QUALQUER---")

senha = ""
email = ""

while True:
    try:
        escolha = int(input(
            "PAINEL\n[1] - Criar conta\n[2] - Entrar na conta\n[3] - Sair (Salvar dados)\n[4] - Sair (Sem salva dados)\nEscolha: "
        ))
        os.system("Cls")

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
                        os.system('Cls')
                        print (
                            "Seu email não existe, tente um email válido."
                        )
                        sleep(1)
                        os.system('Cls')
                        continue
    
                except IndexError:
                    print (
                        "Digite algo."
                    )

                if "@gmail.com" not in email_conta_criada:
                    os.system('Cls')
                    print(
                        "Seu email está faltando '@gmail.com'. Tente Novamente."
                        )
                    sleep(1)
                    os.system('Cls')
                    continue
                email += email_conta_criada
                break

            while True:
                senha_conta_criada = input(
                    "Digite uma senha: "
                    )
                if len(senha_conta_criada) <= 4:
                    os.system('Cls')
                    print(
                        "Sua senha deve ter mais de 4 caracteres. Tente Novamente."
                        )
                    sleep(1)
                    os.system('Cls')
                    continue

                if "@" not in senha_conta_criada and "#" not in senha_conta_criada:
                    os.system('Cls') 
                    print (
                        "Sua senha deve ter um caractere especial como '@ ou #'. Tente novamente."
                    )
                    sleep(1)
                    os.system('Cls')
                    continue

                senha += senha_conta_criada
                os.system('Cls')
                break 
                
            print("Conta Criada com Sucesso!")

        elif escolha == 2:
            if email == "" or senha == "":
                os.system('Cls')
                print(
                    "Você não possui dados cadastrados. Crie uma conta."
                    )
                sleep(1)
                os.system('Cls')
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
                os.system('Cls')
                print("Logado(a) com sucesso!")
            else:
                os.system('Cls')
                print("Email ou senha incorretos.")

        elif escolha == 3:
            os.system('Cls')
            while True:
                print (
                    "Fora do site..."
                )
                escolha_voltar_site = input(
                        "Deseja entrar no site novamente? [s/n]: "
                        ).strip().lower()
                if escolha_voltar_site == "s":
                        os.system('Cls')
                        break
                elif escolha_voltar_site == "n":
                    os.system('Cls')
                    print(
                        "Você escolheu sair. Encerrando..."
                        )
                    sleep(2)
                    os.system('Cls')
                else:
                    os.system('Cls')
                    print(
                        "Opção inválida. Voltando ao menu principal."
                    )  
                    sleep(1)
                    os.system('Cls')
                    break

        elif escolha == 4:
            print("Saindo... SEM SALVAR OS DADOS!")
            break

        else:
            os.system('Cls')
            print("Escolha uma opção válida.")
            sleep(1)
            os.system('Cls')

    except ValueError: 
        os.system('Cls')  
        print("Escolha sua opção em forma numérica.")
        sleep(1)
        os.system('Cls')