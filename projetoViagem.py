import streamlit as st

viagem= ""
agendarViagem, checklist= st.tabs(["Agendar Viagem", "O que levar?"])

with agendarViagem:
    st.title('_Minha viagem_ :airplane:')

    local = st.text_input("Onde quero conhecer?")
    dataIda = st.date_input("Data da ida: ")
    dataVolta = st.date_input("Data da volta: ")
    dias = st.text_input("Vou ficar quantos dias?")
    horaIda = st.time_input("Horário de partida: ")
    horaVolta = st.time_input("Horário da volta: ")
    transporte = st.text_input("Meio de transporte: ")
    valorInicial, valorFinal = st.select_slider('Quanto pretendo gastar?',
    options=['Menos de R$600', 'R$900', 'R$1200', 'R$1500', 'R$1800', 'R$2100', 'R$2300', 'R$2600', 'R$2900', 'R$3100', 'R$3400', 'R$3700', 'R$4000', 'R$4300','mais de R$4600'],
    value=('R$900', 'R$1500'))

    if st.button("salvar"):
        with open("agendamento.txt", "a") as agenda:
            agenda.write("local: "+ local + "\n" + "Data ida: " + str(dataIda) + "\n" + "Data Volta: " + str(dataVolta) + "\n" + "Vai ficar {} dias".format(dias) + "\n" + "Hora da ida: " + str(horaIda) + "\n" + "Hora da volta: " + str(horaVolta) + "\n" + "Meio de transporte: " + transporte + "\n" + "Pretendo gastar de {} até {}".format(valorInicial, valorFinal + "\n"))
        agenda.close()

with checklist:
    st.title('_Meu checklist_ :heavy_check_mark:')
    st.text('Minha viagem:')
    with open("agendamento.txt", "r") as agenda:
        viagem = agenda.read()
        st.text(viagem)

with checklist:
    st.subheader("O que levar?")
    st.checkbox("Camisetas")
    qtdeCamisetas = st.selectbox('Quantidade', ('1', '2', '3', '4', '5', '6', '7', '8'), key="<qtde1>")
    st.checkbox("Camisas")
    qtdeCamisas = st.selectbox('Quantidade', ('1', '2', '3', '4', '5', '6', '7', '8'), key="<qtde2>")
    st.checkbox("Calças")
    qtdeCalcas = st.selectbox('Quantidade', ('1', '2', '3', '4', '5', '6', '7', '8'), key="<qtde3>")
    st.checkbox("Bermudas")
    qtdeBermu = st.selectbox('Quantidade', ('1', '2', '3', '4', '5', '6', '7', '8'), key="<qtde4>")
    st.checkbox("Meias")
    qtdeMeia = st.selectbox('Quantidade', ('1', '2', '3', '4', '5', '6', '7', '8'), key="<qtde5>")
    st.checkbox("Escova de dente")
    st.checkbox("Roupa de frio")
    st.checkbox("Chinelo")
    st.checkbox("Documentos")
    st.checkbox("Remédios")
    nomeRemedio = st.text_area("Digite o nome dos remédios")
    st.checkbox("Passagens")
    st.checkbox("Dinheiro")
    valorLevar = st.text_input("Digite o valor a ser levado: ")
    st.checkbox("Cartão")
    cartao = st.text_area("Quais cartões devo levar: ")
    st.checkbox("Celular")
    st.checkbox("Carregador de celular")
    st.checkbox("Fone de ouvido")
    outros = st.text_area("Digite outros itens indispensáveis para sua viagem: ")

    if st.button("Adicionar"):
        with open("checklist.txt", "a") as check:
            checklist = check.write("Camisetas: quantidade: " + str(qtdeCamisetas) + "\n" + "Camisas: quantidade: " + str(qtdeCamisas) + "\n" + "Calças: quantidade: " + str(qtdeCalcas) + "\n" + "Bermuda: quantidade: " + str(qtdeBermu) +  "\n" + "Meia: quantidade: " + str(qtdeMeia) + "\n" + "Escova de Dente" + "\n" + "Roupa de Frio" + "\n" + "Chinelo" + "\n" + "Documentos" + "\n" + "Remedios: nome dos remédios: " + str(nomeRemedio) + "\n" + "Passagens" + "\n" + "Dinheiro. Levar R${}".format(valorLevar) + "\n" + "Cartões. Quais cartões: " + cartao + "\n" + "Carregador de Celular" + "\n" + "Fone de ouvido" + "\n" + "Outros itens a ser levados: " + str(outros))
            check.close()
        with open("checklist.txt", "r") as check:
            st.text("Lista de itens: ")
            lista = check.read()
            st.text(lista)