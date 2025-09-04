from pathlib import Path

Path("nuovadirectory").mkdir(exist_ok=True)

percorsodeipy = Path(__file__).parent
print(f"il file python in esecuzione si trova qui: {percorsodeipy}")

percorsodellanuovadirectory = percorsodeipy / "nuovadirectory"
print(f"la nuova cartella creata si trova qui: {percorsodellanuovadirectory}")

percorsodelfiletestodentronuovadirectory = percorsodellanuovadirectory / "testo.txt"

filetrovati = 0
bytescomplessivi = 0

with open(percorsodelfiletestodentronuovadirectory, "w") as f:
    for elemento in percorsodeipy.iterdir():
        if elemento.is_file():
            f.write(f"{elemento.name}\n")
            filetrovati += 1
            bytescomplessivi += elemento.stat().st_size
            
            

    f.write(f"\nTotale file: {filetrovati}")
    f.write(f"\nDimensione complessiva dei file(bytes): {bytescomplessivi}")
