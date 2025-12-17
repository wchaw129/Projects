from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

def get_preprocessor():
    """provides ColumnTransformer object"""
    
    nominal_features = ['race/ethnicity']
    ordinal_features = ['parental level of education']
    binary_features = ['gender', 'lunch', 'test preparation course']

    education_order = [
        'some high school', 'high school', 'some college', 
        "associate's degree", "bachelor's degree", "master's degree"
    ]

    preprocessor = ColumnTransformer(
        transformers = [
            ('nominal', OneHotEncoder(drop='first', handle_unknown='ignore'), nominal_features),
            ('ordinal', OrdinalEncoder(categories=[education_order]), ordinal_features),
            ('binary', OneHotEncoder(drop='if_binary'), binary_features)
        ],
        remainder='passthrough'
    )
    
    return preprocessor