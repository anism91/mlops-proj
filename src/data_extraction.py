import pandas as pd

def load_reviews_data(file_path: str) -> pd.DataFrame:
    """
    Charge les avis des utilisateurs à partir d'un fichier CSV.
    Gère les erreurs liées aux fichiers manquants ou mal formatés.
    
    :param file_path: Chemin du fichier CSV
    :return: DataFrame contenant les avis des utilisateurs
    """
    df = pd.read_csv(file_path)
    
    # Vérifier si les colonnes attendues sont présentes
    expected_columns = {"reviewId", "userName", "content", "score", "at", "appId"}
    if not expected_columns.issubset(df.columns):
        raise ValueError("Le fichier ne contient pas toutes les colonnes attendues.")
    
    return df
    
def clean_reviews_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie les données en supprimant les valeurs manquantes et en formatant les colonnes.
    
    :param df: DataFrame brut
    :return: DataFrame nettoyé
    """
    df = df.dropna(subset=["content", "score", "at"])
    df["at"] = pd.to_datetime(df["at"], errors='coerce')
    df = df.dropna(subset=["at"])  # Supprimer les dates invalides
    return df

if __name__ == "__main__":
    file_path = "../data/dataset.csv"
    print("1")
    df = load_reviews_data(file_path)
    print("2")
    if not df.empty:
        df = clean_reviews_data(df)
        print(df.head())
