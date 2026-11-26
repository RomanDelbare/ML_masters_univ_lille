"""
Fusion des extraits annuels en un seul CSV, avec les colonnes du notebook 2024.
Aucune colonne n'est créée et aucune valeur n'est déduite : les lignes sont mises bout à bout.

Usage :
    python merge_extracts.py
    python merge_extracts.py --dossier ./extracts --sortie extract_all.csv
"""
import argparse
from pathlib import Path

import pandas as pd
# Racine du dépôt : src/ -> ..
ROOT = Path(__file__).resolve().parents[1]
DOSSIER_EXTRAITS = ROOT / "data" / "interim" / "extract"
SORTIE_CSV = DOSSIER_EXTRAITS / "extract_all.csv"

# Extraits produits par les notebooks d'extraction (adapter les noms si besoin, notamment 2024).
FICHIERS = [
    "Master2019_ALL-SHS_P_extract.xlsx",
    "Master2019_DEG_P_extract.xlsx",
    "Master2019_ST_P_extract.xlsx",
    "Master2019_Santé_P_extract.xlsx",
    "Master2020_ALL-SHS_P_extract.xlsx",
    "Master2020_DEG_P_extract.xlsx",
    "Master2020_sante_staps_P_extract.xlsx",
    "Master2022_ALL-SHS_P_extract.xlsx",
    "Master2022_DEG_P_extract.xlsx",
    "Master2022_ST_P_extract.xlsx",
    "Master2022_Sante_P_extract.xlsx",
    "Master2023_ALL-SHS_P_extract.xlsx",
    "Master2023_DEG_P_extract.xlsx",
    "Master2023_ST_P_extract.xlsx",
    "Master2023_Sante-STAPS_P_extract.xlsx",
    "Master2024_ALL-SHS_P_extract.xlsx",
    "Master2024_ST_P_extract.xlsx",
    "Master2024_Sante-STAPS_P_extract.xlsx",
    "Master2024_DEG_P_extract.xlsx",
    "Rep_Master2016_ALL-SHS_extract.xlsx",
    "Rep_Master2016_DEG_extract.xlsx",
    "Rep_Master2016_ST_extract.xlsx",
    "Rep_Master2016_Santé-STAPS_extract.xlsx",
    "Rep_Master2017_ALL-SHS_web_extract.xlsx",
    "Rep_Master2017_DEG_web_extract.xlsx",
    "Rep_Master2017_ST_web_extract.xlsx",
    "Rep_Master2017_Santé_web_extract.xlsx",
    "Rep_Master2018_ALL-SHS_P_extract.xlsx",
    "Rep_Master2018_DEG_P_extract.xlsx",
    "Rep_Master2018_ST_P_extract.xlsx",
    "Rep_Master2018_Santé_P_extract.xlsx",
    "master2020_ST_P_extract.xlsx",
]
# Colonnes conservées, dans l'ordre d'écriture du CSV.
COLONNES = [
    "mention", "parcours", "promotion", "situation", "n_interroges", "taux_reponse",
    "n_en_emploi", "n_recherche_emploi", "n_en_etudes", "n_autre_situation",
    "n_total_repondants", "n_emploi_stable", "n_emploi_non_stable", "effectif_insuffisant",
    "diplome", "intitule_emploi", "missions", "categorie_emploi", "type_emploi",
    "secteur_employeur", "activite_employeur", "lieu_emploi", "autre_diplome",
    "temps_partiel", "revenu_net", "emploi_stable",
]

# Seules différences de nom entre les extraits : on reprend les noms du notebook 2024.
RENOMMAGES = {
    "n_concernes": "n_interroges",  # 2016, 2017, 2020, 2022 : « concerné-e-s par l'enquête »
    "master": "parcours",           # 2016 : le pdf donne « Master <nom> », sans mention
}

COLONNES_ENTIERES = [
    "promotion", "n_interroges", "n_en_emploi", "n_recherche_emploi", "n_en_etudes",
    "n_autre_situation", "n_total_repondants", "n_emploi_stable", "n_emploi_non_stable",
]
COLONNES_BOOLEENNES = ["effectif_insuffisant", "temps_partiel", "emploi_stable"]


def lire_extrait(chemin):
    """Lit un extrait, retire l'éventuelle colonne d'index et applique les renommages."""
    if not chemin.exists():
        raise FileNotFoundError(f"Fichier introuvable : {chemin} (vérifier FICHIERS ou --dossier)")

    df = pd.read_csv(chemin) if chemin.suffix == ".csv" else pd.read_excel(chemin)
    df = df.loc[:, ~df.columns.str.startswith("Unnamed")]
    df = df.rename(columns=RENOMMAGES)

    absentes = [c for c in COLONNES if c not in df.columns]
    if absentes:
        print(f"  colonne(s) absente(s) de {chemin.name}, laissée(s) vide(s) : {absentes}")

    df = df.reindex(columns=COLONNES)

    # Selon les fichiers, Excel relit emploi_stable en booléen ou en 0.0 / 1.0 (si valeurs manquantes) :
    # on uniformise avant de mettre les fichiers bout à bout.
    for col in COLONNES_BOOLEENNES:
        df[col] = df[col].astype("boolean")
    return df


def fusionner(dossier, sortie):
    extraits = []
    for nom in FICHIERS:
        df = lire_extrait(Path(dossier) / nom)
        print(f"{nom} : {len(df)} lignes")
        extraits.append(df)

    df = pd.concat(extraits, ignore_index=True)

    # Entiers sans « .0 » dans le CSV (les valeurs manquantes restent vides).
    for col in COLONNES_ENTIERES:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

    df.to_csv(sortie, index=False, encoding="utf-8")
    print(f"\nCSV écrit : {sortie} ({len(df)} lignes, {len(df.columns)} colonnes)")
    return df


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Fusionne les extraits annuels en un seul CSV.")
    ap.add_argument("--dossier", default=DOSSIER_EXTRAITS, help="dossier contenant les extraits (défaut : dossier courant)")
    ap.add_argument("--sortie", default=SORTIE_CSV, help="CSV de sortie (défaut : extract_all.csv)")
    args = ap.parse_args()

    fusionner(args.dossier, args.sortie)
