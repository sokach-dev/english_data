import json
import sqlite3

# 读取JSON文件
with open('vocabulary.json', 'r') as f:
    datas = json.load(f)

# 将数据插入到SQLite数据库
conn = sqlite3.connect('/Users/lele/develop/vue/orion-app/data/db.sqlite3')
cursor = conn.cursor()

for data in datas:
    cursor.execute('INSERT INTO vocabulary (id, word, soundmark,roots,paraphrase,collocations,synonyms,examples,created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (data['id'], data['word'], data['soundmark'], data['roots'],  data['paraphrase'], data['collocations'],data['synonyms'], data['examples'], data['created_at'][0:-10], data['updated_at'][0:-10]))

conn.commit()
conn.close()

