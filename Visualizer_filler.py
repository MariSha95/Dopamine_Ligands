import pandas as pd
df= pd.read_csv('enriched_dopamine_ec50.csv')
def load_data(self):
        return pd.read_csv(self.path_to_file, sep=';')
        df= pd.read_csv('enriched_dopamine_ec50.csv')
print(df.head())
def preprocess_data(df, target_column):
   
    X = df.drop(columns=['MW', 'LogP', 'H_Donors','H_Acceptors', 'TPSA', 'Rotatable_Bonds', 'SMILES', 'Target Name'])
    y = df['pEC50']

    # Определение числовых и категориальных признаков
    numeric_features = ['MW', 'LogP', 'H_Donors','H_Acceptors', 'TPSA', 'Rotatable_Bonds']
    categorical_features = ['SMILES', 'Target Name']

    # Создание препроцессора
    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(drop='first')

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # Применение препроцессора к данным
    X_processed = preprocessor.fit_transform(X)
    return X_processed, y, preprocessor
