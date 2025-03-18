from sklearn.linear_model import LinearRegression
from sklearn.metrics import euclidean_distances
from sqlalchemy import create_engine

def assign_engagement_score(df, features, cluster_centers):
    """
    Assign engagement score as Euclidean distance from the least engaged cluster center.
    """
    df['engagement_score'] = euclidean_distances(df[features], [cluster_centers[0]]).flatten()
    return df

def assign_experience_score(df, features, cluster_centers):
    """
    Assign experience score as Euclidean distance from the worst experience cluster center.
    """
    df['experience_score'] = euclidean_distances(df[features], [cluster_centers[0]]).flatten()
    return df

def calculate_satisfaction(df):
    """
    Calculate satisfaction score as the average of engagement and experience scores.
    """
    df['satisfaction_score'] = df[['engagement_score', 'experience_score']].mean(axis=1)
    return df

def predict_satisfaction(df, features):
    """
    Build a regression model to predict satisfaction scores.
    """
    model = LinearRegression()
    X = df[features]
    y = df['satisfaction_score']
    model.fit(X, y)
    return model

def export_to_mysql(df, db_name, table_name):
    """
    Export the final table to a local MySQL database.
    """
    engine = create_engine(f'mysql+pymysql://besu:Besu@hazi21@localhost/{db_name}')
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Data exported to {db_name}.{table_name}")