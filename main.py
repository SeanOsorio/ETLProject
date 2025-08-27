from Extract.extractor import Extractor
from Transform.transformer import Transformer
from Load.loader import Loader
from Config.config import Config

def main():
    # Paso 1: Extraer los datos
    extractor = Extractor(Config.INPUT_PATH)
    df = extractor.extract()
    
    if df is None:
        print("No se pudieron extraer los datos. Abortando el proceso.")
        return

    # Paso 2: Transformar los datos
    transformer = Transformer(df)
    cleaned_df = transformer.clean()
    
    if cleaned_df is None:
        print("No se pudieron transformar los datos. Abortando el proceso.")
        return

    # Paso 3: Cargar los datos
    loader = Loader(cleaned_df)
    loader.to_csv(Config.OUTPUT_PATH)

if __name__ == "__main__":
    main()

