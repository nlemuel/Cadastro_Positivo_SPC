import matplotlib.pyplot as plt
import csv
import pandas as pd

import tkinter as tk
from tkinter import filedialog
import pandas as pd


######TELA INICIAL######
root= tk.Tk()
root.title('SmartData')

canvas1 = tk.Canvas(root, width = 570, height = 400, bg = '#a6a6a6')
canvas1.pack()
canvas1.create_text(310,15,fill="#ffcc00",font="Impact 20 bold",text="- SPC Brasil -")
canvas1.create_text(310,40,fill="#0000cc",font="Impact 20",text="- Pesquisa de dados por ID. -")
############

######FUNÇÕES PARA LER CADA ARQUIVO ESCOLHIDO######
def getfontes ():
    global fontes
    import_file_path = filedialog.askopenfilename()
    canvas1.create_text(310,80,fill='gray',font='Impact 13 bold',text= import_file_path)
    fontes = pd.read_excel (import_file_path)
def getmodalidades ():
    global modalidades
    import_file_path = filedialog.askopenfilename()
    canvas1.create_text(310,120,fill='gray',font='Impact 13 bold',text= import_file_path)
    modalidades = pd.read_excel (import_file_path)
def getpagamentos ():
    global pagamentos
    import_file_path = filedialog.askopenfilename()
    canvas1.create_text(310,160,fill='gray',font='Impact 13 bold',text= import_file_path)
    pagamentos = pd.read_excel (import_file_path)
def getmovimentacoes ():
    global movimentacoes
    import_file_path = filedialog.askopenfilename()
    canvas1.create_text(310,200,fill='gray',font='Impact 13 bold',text= import_file_path)
    movimentacoes = pd.read_excel (import_file_path)
def getoperacoes ():
    global operacoes
    import_file_path = filedialog.askopenfilename()
    canvas1.create_text(310,240,fill='gray',font='Impact 13 bold',text= import_file_path)
    operacoes = pd.read_excel (import_file_path)
############
    
######BOTÕES PARA ESCOLHER OS ARQUIVOS EXCEL######
browseButton_Excel = tk.Button(text='Fontes', command=getfontes, bg='#007399', fg='white', font=('helvetica', 12, 'bold'), width=15, height=1)
canvas1.create_window(310, 80, window=browseButton_Excel)
browseButton_Excel = tk.Button(text='Modalidades', command=getmodalidades, bg='#007399', fg='white', font=('helvetica', 12, 'bold'), width=15, height=1)
canvas1.create_window(310, 120, window=browseButton_Excel)
browseButton_Excel = tk.Button(text='Pagamentos', command=getpagamentos, bg='#007399', fg='white', font=('helvetica', 12, 'bold'), width=15, height=1)
canvas1.create_window(310, 160, window=browseButton_Excel)
browseButton_Excel = tk.Button(text='Movimentações', command=getmovimentacoes, bg='#007399', fg='white', font=('helvetica', 12, 'bold'), width=15, height=1)
canvas1.create_window(310, 200, window=browseButton_Excel)
browseButton_Excel = tk.Button(text='Operações', command=getoperacoes, bg='#007399', fg='white', font=('helvetica', 12, 'bold'), width=15, height=1)
canvas1.create_window(310, 240, window=browseButton_Excel)
############

######INDICADORES######
def gerar_indicadores():


    ###FONTE###
    fonte = entrada.get()
    fonte_buscada = fontes.query(f"ID_STG_FNT_ITT == {fonte}")
    nome_fonte = fonte_buscada.get('NOM_COM')
    
    cnpj = fontes.query(f"ID_STG_FNT_ITT == {fonte}")
    n_cnpj = cnpj.get("NUM_CNPJ")

    cmp = fontes.query(f"ID_STG_FNT_ITT == {fonte}")
    n_cmp = cmp.get("NUM_CMP_CNPJ")

    rzs = fontes.query(f"ID_STG_FNT_ITT == {fonte}")
    n_rzs = rzs.get("NOM_RAZ_SCL")
    

    ###RESULTADOS###
    
    print("ID DA FONTE: ",fonte)
    print("CNPJ: ",n_cnpj.to_string(index=False, header=False))
    print("COMPLEMENTO DO CNPJ: ",n_cmp.to_string(index=False, header=False))
    print("RAZÃO SOCIAL: ",n_rzs.to_string(index=False, header=False))
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
                                 
    ###OPERAÇÃO###
    operacao = entrada.get()
    op_buscada = operacoes.query(f"ID_STG_OPR_ITT == {operacao}")
    nome_operacao = op_buscada.get("VLR_CTRD_CSC")

    quantidade_parcelas = entrada.get()
    qp_buscada = operacoes.query(f"ID_STG_OPR_ITT == {quantidade_parcelas}")
    qtd_pcl = qp_buscada.get("QTD_PCL")

    valor_devedor = entrada.get()
    vd_buscado = operacoes.query(f"ID_STG_OPR_ITT == {valor_devedor}")
    qtd_vd = vd_buscado.get("VLR_SDO_DDR")
    
    quantidade_operacoes = entrada.get()
    qo_buscado = operacoes.query(f"ID_STG_OPR_ITT == {quantidade_operacoes}")
    qtd_opr = qo_buscado.get("QTD_OPR")

    qtd_cad_pos = entrada.get()
    qcp_buscado = operacoes.query(f"ID_STG_OPR_ITT == {qtd_cad_pos}")
    qtd_qcp = qcp_buscado.get("QTD_CLI_CAD_POS")
    
    id_da_fnt = entrada.get()
    fnt_buscada = operacoes.query(f"ID_STG_OPR_ITT == {id_da_fnt}")
    qtd_fnt = fnt_buscada.get("ID_FNT_ITT")

    id_mod = entrada.get()
    mdl_buscada = operacoes.query(f"ID_STG_OPR_ITT == {id_mod}")
    qtd_mdl = mdl_buscada.get("ID_MDL")

    tipo_pessoa = entrada.get()
    pessoa_buscada = operacoes.query(f"ID_STG_OPR_ITT == {tipo_pessoa}")
    qtd_pessoa = pessoa_buscada.get("DES_TIP_PSS")

    ###RESULTADOS###
    print("INFORMAÇÕES SOBRE AS OPERAÇÕES.")
    print('REMESSA DA FONTE: ',nome_fonte.to_string(index = False, header = False))
    print('Valor total contratado: R$ ', nome_operacao.to_string(index=False, header=False))
    print('Quantidade de parcelas: ',qtd_pcl.to_string(index=False, header=False))
    print('Valor total do saldo devedor: R$',qtd_vd.to_string(index=False, header=False))
    print('Quantidade de operações: ',qtd_opr.to_string(index=False, header=False))
    print('Quantidade de clientes no cadastro positivo: ',qtd_qcp.to_string(index=False, header=False))
    print('ID DA FONTE: ',qtd_fnt.to_string(index=False, header=False))
    print('ID DA MODALIDADE: ',qtd_mdl.to_string(index=False, header=False))
    print('Tipo de pessoa: ',qtd_pessoa.to_string(index=False, header=False))
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
    
    ###PAGAMENTO###
    
    vlr_pgt_ft = entrada.get()
    vpf_buscada = pagamentos.query(f"ID_STG_PGT == {vlr_pgt_ft}")
    qtd_vpf = vpf_buscada.get("VLR_PGT_FAT")

    dat_vt = entrada.get()
    dv_buscada = pagamentos.query(f"ID_STG_PGT == {dat_vt}")
    qtd_dv = dv_buscada.get("DAT_VCT")

    cd_mdl = entrada.get()
    mdl_buscado = pagamentos.query(f"ID_STG_PGT == {cd_mdl}")
    qtdmdl = mdl_buscado.get("COD_MDL")

    qcp = entrada.get()
    qcp_buscada = pagamentos.query(f"ID_STG_PGT == {qcp}")
    qtd_qcp = qcp_buscada.get("QTD_CLI_CAD_POS")

    qp = entrada.get()
    qp_buscado = pagamentos.query(f"ID_STG_PGT == {qp}")
    qtd_qp = qp_buscado.get("QTD_PGT")

    iftt = entrada.get()
    iftt_buscada = pagamentos.query(f"ID_STG_PGT == {iftt}")
    qtd_iftt = iftt_buscada.get("ID_FNT_ITT")

    tdp = entrada.get()
    tdp_buscado = pagamentos.query(f"ID_STG_PGT == {tdp}")
    qtd_tdp = tdp_buscado.get("DES_TIP_PSS")

    
    ###RESULTADOS###
    print("INFORMAÇÕES DE PAGAMENTO DO CADASTRO POSITIVO:")
    print('ID DO PAGAMENTO: ', entrada.get())
    print('Valor do pagamento por fatura: R$',qtd_vpf.to_string(index=False, header=False))
    print('Data de vencimento: ',qtd_dv.to_string(index=False, header=False))
    print('Codigo da modalidade: ',qtdmdl.to_string(index=False, header=False))
    print('Quantidade de pagamento: ',qtd_qp.to_string(index=False, header=False))
    print('Quantidade de clientes do cadastro positivo: ',qtd_qcp.to_string(index=False, header=False))
    print('ID DA FONTE :  ', qtd_iftt.to_string(index=False, header=False))
    print('Tipo de pessoa: ',qtd_tdp.to_string(index=False, header=False))
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    ###MODALIDADE###

    idmdl = entrada.get()
    idmdl_buscado = modalidades.query(f"ID_STG_MDL == {idmdl}")
    qtd_idmdl = idmdl_buscado.get("COD_MDL")

    des_mdl = entrada.get()
    des_mdl_buscado = modalidades.query(f"ID_STG_MDL == {des_mdl}")
    qtd_des_mdl = des_mdl_buscado.get("DES_MDL")
    
    ###RESULTADOS###
    print("INFORMACOES DE MODALIDADE (CREDITO, CHEQUE, CONSORCIO E ETC) QUE FORAM DISPONIBILIZADAS.")
    print('ID DA MODALIDADE: ',entrada.get())
    print('Codigo da modalidade: ', qtd_idmdl.to_string(index=False, header=False))
    print('Descrição da modalidade: ', qtd_des_mdl.to_string(index=False, header=False))
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    
    ###MOVIMENTO###

    vlr_sld_utz = entrada.get()
    vlr_buscado = movimentacoes.query(f"ID_STG_MVT_CRD == {vlr_sld_utz}")
    qtd_vlr = vlr_buscado.get("VLR_SDO_UTZ_CRD_RTO")

    vlr_tot_ft = entrada.get()
    vtf_buscado = movimentacoes.query(f"ID_STG_MVT_CRD == {vlr_tot_ft}")
    qtd_vtf = vtf_buscado.get("VLR_TOT_FAT")

    vlr_mim_ft = entrada.get()
    vmf_buscado = movimentacoes.query(f"ID_STG_MVT_CRD == {vlr_mim_ft}")
    qtd_vmf = vmf_buscado.get("VLR_MIM_FAT")

    vlr_pcl_ft = entrada.get()
    vpf_buscado = movimentacoes.query(f"ID_STG_MVT_CRD == {vlr_pcl_ft}")
    qtd_vpf = vpf_buscado.get("VLR_PCL_FAT")

    qcp2 = entrada.get()
    qcp2_buscado = movimentacoes.query(f"ID_STG_MVT_CRD == {qcp2}")
    qtd_qcp2 = qcp2_buscado.get("QTD_CLI_CAD_POS")

    qmvt = entrada.get()
    qmvt_buscado = movimentacoes.query(f"ID_STG_MVT_CRD == {qmvt}")
    qtd_qmvt = qmvt_buscado.get("QTD_MVT")

    desc_tp = entrada.get()
    dt_buscado = movimentacoes.query(f"ID_STG_MVT_CRD == {desc_tp}")
    qtd_dt = dt_buscado.get("DES_TIP_PSS")

    idfntm = entrada.get()
    ifnt_buscado = movimentacoes.query(f"ID_STG_MVT_CRD == {idfntm}")
    qtd_ifnt = ifnt_buscado.get("ID_FNT_ITT")

    cml = entrada.get()
    cml_buscado = movimentacoes.query(f"ID_STG_MVT_CRD == {cml}")
    qtd_cml = cml_buscado.get("COD_MDL")
    

    ###RESULTADOS###
    print("INFORMACOES DE MOVIMENTACAO DAS OPERACOES DO CADASTRO POSITIVO.")
    print('ID DO MOVIMENTO DE CREDITO: ',entrada.get())
    print('Valor do saldo utilizado: R$', qtd_vlr.to_string(index=False, header=False))
    print('Valor total de faturamento: ',qtd_vtf.to_string(index=False, header=False))
    print('Valor minimo de faturamento: R$',qtd_vmf.to_string(index=False, header=False))
    print('Valor da parcela da movimentacao enviada pela fonte: ',qtd_vpf.to_string(index=False, header=False))
    print('Quantidade de CNPJ/CPF distintos na base do cadastro positivo: ' ,qtd_qcp2.to_string(index=False, header=False))
    print('Quantidade de movimentação: R$ ',qtd_qmvt.to_string(index=False, header=False))
    print('Tipo do cliente: ',qtd_dt.to_string(index=False, header=False))
    print('Id da fonte que enviou os dados: ',qtd_ifnt.to_string(index=False, header=False))
    print('Codigo da modalidade da movimentacao: ',qtd_cml.to_string(index=False, header=False))
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
############

entrada = tk.Entry(root)
descrição = tk.Label(root, text="Insira o ID da fonte desejada: ")
canvas1.create_window(310,280, window=descrição)
canvas1.create_window(307, 315, window=entrada)
button1 = tk.Button(text='Pesquisar', command=gerar_indicadores, bg='#154695', fg='white')
canvas1.create_window(305, 350, window=button1)



