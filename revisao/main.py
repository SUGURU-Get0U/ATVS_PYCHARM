import threading
from threading import BoundedSemaphore, Lock
from time import sleep

# calcular valores estaticos setados pelo usuario

#primeiro receber os valores do usuario, mas antes vamos criar as threads e suas funções

# criar uma variavel chamada limite de números, e faze-la um bounded sephamore

# Variaveis Globais!
maxnumbers= 6
pool_sema = BoundedSemaphore(value=maxnumbers)
Array = []
array_lock = Lock()
input_finished = threading.Event()

def get_a_number():
    
    global Array
    
    print(f"Digite {maxnumbers} números:")
    
    for i in range(maxnumbers):
        try:
            number = float(input(f"digite o número {i + 1}: "))
            
            # Fazer os processos de Lock do array com o array_lock
            with array_lock:
                Array.append(number)
                print(f"O número {number} foi adicionado ao Array")
        
        except ValueError:
            print("Por favor digite um número válido!")
            return
        
    # Sinalizar que a entrda de dados terminou
    input_finished.set()
    print("Todos os números foram coletados! 🚀")
    
    
def media_thread():
    # Esperar o input terminar de coisar
    input_finished.wait()
    
    # verificar erros do input
    with array_lock:
        if len(Array) == 0:
            print("Não tem poha nenhuma no Array, casa caiu!")
            return
        
        total_sum = sum(Array)
        average = total_sum / len(Array)
        
        print(f"\n=== RESULTADOS DA MÉDIA ===")
        print(f"Números inseridos: {Array}")
        print(f"Quantidade de números: {len(Array)}")
        print(f"Soma total: {total_sum}")
        print(f"Média: {average:.2f}")
        
def maior_thread():
    # Esperar o input terminar de coisar
    input_finished.wait()
    
    # verificar erros do input
    with array_lock:
        if len(Array) == 0:
            print("Não tem poha nenhuma no Array, casa caiu!")
            return
        
        organized_array = sorted(Array)
        
        print(f"\n=== MAIOR NÚMERO ===")
        print(f"Números inseridos: {Array}")
        print(f"Quantidade de números: {len(Array)}")
        print(f"Maior Número / Valor maximo: {organized_array[-1]}")
        
        
def menor_thread():
    # Esperar o input terminar de coisar
    input_finished.wait()
    
    # verificar erros do input
    with array_lock:
        if len(Array) == 0:
            print("Não tem poha nenhuma no Array, casa caiu!")
            return
        
        organized_array = sorted(Array)
        
        print(f"\n=== MENOR NÚMERO ===")
        print(f"Números inseridos: {Array}")
        print(f"Quantidade de números: {len(Array)}")
        print(f"Menor Número / Valor minimo: {organized_array[0]}")
        
def main():
    """Função Principal ou main pra inicar as threads"""
    
    # Criar as threads:
    input_thread = threading.Thread(target=get_a_number, name="InputzaoDaMassa")
    calc_media_thread = threading.Thread(target=media_thread, name="Siricutico")
    calc_maior_thread = threading.Thread(target=maior_thread, name="Espingoliro")
    calc_menor_thread = threading.Thread(target=menor_thread, name="jão")
    
    #iniciar as threads:
    input_thread.start()
    calc_media_thread.start()
    calc_media_thread.join()
    calc_maior_thread.start()
    calc_maior_thread.join()
    calc_menor_thread.start()
    calc_menor_thread.join()
    
    # Sincronizar as threads com o .join
    input_thread.join()
    calc_media_thread.join()
    calc_maior_thread.join()
    calc_menor_thread.join()
    
    print("\nSincronização concluida")

if __name__ == "__main__":
    main()