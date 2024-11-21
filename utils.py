import json

def exportar_para_json(dados):
    try:
        with open('consulta_clientes.json', 'w') as f:
            json.dump(dados, f, indent=4)
        print("Consulta exportada para JSON com sucesso!")
    except Exception as e:
        print(f"Erro ao exportar para JSON: {e}")
