import os
import argparse
from pathlib import Path

# Exit codes for actions
# https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions

def buscar_en_archivo(ruta, texto):
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            for num_linea, linea in enumerate(archivo, 1):
                if texto in linea:
                    yield num_linea, linea.strip()
    except UnicodeDecodeError:
        # Ignoramos archivos que no se puedan leer como texto
        pass
    except Exception as e:
        print(f"Error leyendo archivo {ruta}: {str(e)}")

def buscar_contenido(ruta_base, texto):
    ruta_base = Path(ruta_base)
    
    # Si no existe, error
    if not ruta_base.exists():
        print(f"Error: La ruta {ruta_base} no existe")
        return
    
    # Si no es un directorio, error
    if not ruta_base.is_dir():
        print(f"Error: La  ruta {ruta_base} no es un directorio")
        return
    
    count = 0
    
    # Buscamos en todos los archivos
    for root, _, files in os.walk(ruta_base):

        for nombre_archivo in files:

            ruta_completa = Path(root) / nombre_archivo
            
            # Buscamos  en el archivo
            for num_linea, linea in buscar_en_archivo(ruta_completa, texto):
                count+=1
                ruta_relativa = ruta_completa.relative_to(ruta_base)
                print(f"Encontrado  en {ruta_relativa}, línea {num_linea}:")  
    
    return count

def main():

    parser =  argparse.ArgumentParser(description="Busca contenido en archivos")
    parser.add_argument("ruta", help="Ruta base para buscar")
    parser.add_argument("texto",help="Texto a buscar en el contenido de la ruta") 

    args = parser.parse_args()

    coincidencias = buscar_contenido(args.ruta, args.texto)

    if (coincidencias > 0):
        exit(coincidencias)
    
    print("No se han encontrado coincidencias!")

if __name__ == "__main__":
    main()