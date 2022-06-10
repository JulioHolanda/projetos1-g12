import csv

def media(valor1, valor2):
    media = (valor1 + valor2)/2

    return media


def pergunta_filtro():
    print("Deseja procurar por:")
    print("Nome [1]")
    print("Matrícula [2]\nTurma [3]")
    print("Nota 1 [4]\nNota 2 [5]")

def pergunta_filtro_prof():
    print("Deseja procurar por:")
    print("Nome [1]\nCadastro [2]\nMatéria [3]\nTurma [4]")

def resp_filtro(x):
    if x == 1:
        resp = input("Insira o nome: ").upper()
    elif x == 2:
        resp = input("insira o número da matrícula: ")
    elif x == 3:
        resp = input("insira a turma: ").upper()
    elif x == 4:
        resp = input("insira a NOTA 1 (com casa decimal): ")
    elif x == 5:
        resp = input("insira a Nota 2 (com casa decimal): ")
        print()

    return resp

def resp_filtro_prof(x):
    if x == 1:
        resp = input("Insira o nome: ").upper()
    elif x == 2:
        resp = input("insira o número dde cadastro: ")
    elif x == 3:
        resp = input("insira a matéria: ")
    elif x == 4:
        resp = input("insira a turma: ").upper()
        print()

    return resp


def procura():

    # FILTRO COMEÇA AQUI
    existe = 0

    pergunta_filtro()
    i = int(input())
    print()

    while i < 1 and i > 5:
        print("\nINSIRA UM VALOR VÁLIDO\n")
        pergunta_filtro()
        i = int(input())
        print()

    data_hunt = resp_filtro(i)
# FILTRO TERMINA AQUI

    with open('studentData.csv', 'r') as readData_file:
        reader = csv.reader(readData_file)

        # realiza a leitura das linhas
        for line in reader:
            if line[i-1] == data_hunt:
                print(line)
                existe += 1

        readData_file.close()

        if existe == 0:
            print("\nDado errado ou não cadastrado")
    print()

def procura_prof():

    # FILTRO COMEÇA AQUI
    existe = 0

    pergunta_filtro_prof()
    i = int(input())
    print()

    while i < 1 and i > 4:
        print("\nINSIRA UM VALOR VÁLIDO\n")
        pergunta_filtro_prof()
        i = int(input())
        print()

    data_hunt = resp_filtro_prof(i)
# FILTRO TERMINA AQUI

    with open('profData.csv', 'r') as readData_file:
        reader = csv.reader(readData_file)

        # realiza a leitura das linhas
        for line in reader:
            if line[i-1] == data_hunt:
                print(line)
                existe += 1

        readData_file.close()

        if existe == 0:
            print("\nDado errado ou não cadastrado")
    print()

# addstd = add student
def addstd(nome, matricula, turma, nota1, nota2):

    list = [nome, matricula, turma, nota1, nota2]

    with open('studentData.csv', 'a') as data_adder:
        writer_object = csv.writer(data_adder)
        writer_object.writerow(list)

        data_adder.close()

def addtch(nome, cadastro, materia, turma, comentario):

    list = [nome, cadastro, materia, turma, comentario]

    with open('profData.csv', 'a') as data_adder:
        writer_object = csv.writer(data_adder)
        writer_object.writerow(list)

        data_adder.close()

def novos_dados():
    print("Insira os dados do novo estudante:")
    nome = input("NOME: ").upper()
    matrc = int(input("MATRÍCULA: "))
    turma = input("TURMA: ").upper()
    nota1 = float(input("1ª nota: "))
    nota2 = float(input("2ª nota: "))

    addstd(nome, matrc, turma, nota1, nota2)

def novos_dados_prof():
    print("Insira os dados do novo professor(a):")
    nome = input("NOME: ").upper()
    cadastr = int(input("CADASTRO: "))
    materia = float(input("MATÉRIA: "))
    turma = input("TURMA: ").upper()
    coment = float(input("COMENTÁRIO: "))

    addstd(nome, cadastr, materia, turma, coment)


def del_data():

    # FILTRO COMEÇA AQUI
    existe = 0

    pergunta_filtro()
    i = int(input())
    print()

    while i < 1 and i > 5:
        print("\nINSIRA UM VALOR VÁLIDO\n")
        pergunta_filtro()
        i = int(input())
        print()

    data_hunt = resp_filtro(i)
# FILTRO TERMINA AQUI

    with open('studentData.csv', 'r') as original:
        reader = csv.reader(original)

        with open('transferData.csv', 'w', newline='') as rewrite:
            writer = csv.writer(rewrite)

            with open('junkData.csv', 'a', newline='') as data_junk:
                junk = csv.writer(data_junk)

                # realiza a leitura das linhas
                for line in reader:
                    if line[i-1] == data_hunt:
                        junk.writerow(line)
                        existe += 1
                        print(f"DELETADO: {line}")
                    else:
                        writer.writerow(line)

                data_junk.close()
            rewrite.close()
        original.close()

    with open('transferData.csv', 'r') as give:
        transfer = csv.reader(give)

        with open('studentData.csv', 'w', newline='') as recieve:
            reciver = csv.writer(recieve)

            for line in transfer:
                reciver.writerow(line)

            recieve.close()
        give.close()

        if existe == 0:
            print("\nDado errado ou não cadastrado")
    print()

def del_data_prof():

    # FILTRO COMEÇA AQUI
    existe = 0

    pergunta_filtro_prof()
    i = int(input())
    print()

    while i < 1 and i > 4:
        print("\nINSIRA UM VALOR VÁLIDO\n")
        pergunta_filtro_prof()
        i = int(input())
        print()

    data_hunt = resp_filtro_prof(i)
# FILTRO TERMINA AQUI

    with open('profData.csv', 'r') as original:
        reader = csv.reader(original)

        with open('transferData.csv', 'w', newline='') as rewrite:
            writer = csv.writer(rewrite)

            with open('junkProfData.csv', 'a', newline='') as data_junk:
                junk = csv.writer(data_junk)

                # realiza a leitura das linhas
                for line in reader:
                    if line[i-1] == data_hunt:
                        junk.writerow(line)
                        existe += 1
                        print(f"DELETADO: {line}")
                    else:
                        writer.writerow(line)

                data_junk.close()
            rewrite.close()
        original.close()

    with open('transferData.csv', 'r') as give:
        transfer = csv.reader(give)

        with open('profData.csv', 'w', newline='') as recieve:
            reciver = csv.writer(recieve)

            for line in transfer:
                reciver.writerow(line)

            recieve.close()
        give.close()

        if existe == 0:
            print("\nDado errado ou não cadastrado")
    print()

def listagem():

    with open('studentData.csv', 'r') as readData_file:
        reader = csv.reader(readData_file)

        for line in reader:
            for i in range(len(line)):
                print(f"{line[i]:^20}", end='' )
            print()

        readData_file.close()

def listagem_prof():

    with open('profData.csv', 'r') as readData_file:
        reader = csv.reader(readData_file)

        for line in reader:
            for i in range(len(line)):
                print(f"{line[i]:^20}", end='' )
            print()

        readData_file.close()