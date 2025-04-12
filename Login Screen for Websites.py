import os 

print("---TELA LOGIN SITE---")

senha = ""
email = ""

while True:
    try:
        escolha = int(input(
            "PAINEL\n[1] - Criar conta\n[2] - Entrar na conta\n[3] - Sair (Salvar dados)\n[4] - Sair (Sem salvar dados)\nEscolha: "
        ))
        os.system("Cls")

        if escolha == 1:
            while True:
                email_conta_criada = input(
                    "Digite seu email: "
                    )
                
                if "@gmail.com" not in email_conta_criada:
                    print(
                        "Seu email está faltando '@gmail.com'. Tente Novamente."
                        )
                    continue
                email = email_conta_criada
                break

            while True:
                senha_conta_criada = input(
                    "Digite uma senha: "
                    )
                if len(senha_conta_criada) <= 4:
                    print(
                        "Sua senha deve ter mais de 4 caracteres. Tente Novamente."
                        )
                    continue
                senha = senha_conta_criada
                os.system('Cls')
                break 
                
            print("Conta Criada com Sucesso!")

        elif escolha == 2:
            if email == "" or senha == "":
                print(
                    "Você não possui dados cadastrados. Crie uma conta."
                    )
                continue

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
            print("Saindo... DADOS SALVOS :)")
            continue

        elif escolha == 4:
            print("Saindo... SEM SALVAR OS DADOS!")
            break

        else:
            print("Escolha uma opção válida.")

    except ValueError:
        os.system('Cls')
        print("Escolha sua opção em forma numérica.")
