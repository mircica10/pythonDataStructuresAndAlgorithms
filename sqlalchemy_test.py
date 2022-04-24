

import sqlalchemy  
from sqlalchemy.engine.create import create_engine
import pandas as pd

def copy_row():
    conn = create_engine('postgresql://postgres:ANTAnanarivo1234@localhost:5432/spiel_bk')
    source_table = 'test.tweet'
    dest_table = 'test.tweet_desc'


    data = conn.execute(f'select comment from {source_table}')
    for a in data: 
        print(a)
        if data:
            conn.execute(f'insert into {dest_table}(comment) values(\'{a[0]}\') ')
        
def copy_table():
    engine = create_engine('postgresql://postgres:ANTAnanarivo1234@localhost:5432/spiel_bk')
    source_table = 'test.tweet'
    dest_table = 'tweet_desc'
    dbConnection = engine.connect();
    
    dataFrame = pd.read_sql(f"select * from {source_table}", dbConnection);
    print(dataFrame);

    dataFrame.to_sql(dest_table, dbConnection, schema = 'test', if_exists='append', index = False);

    dbConnection.close();


copy_table()