import json
import sqlite3

# 读取JSON文件
with open('word_list.json', 'r') as f:
    datas = json.load(f)

# 将数据插入到SQLite数据库
conn = sqlite3.connect('/Users/lele/develop/vue/orion-app/data/db.sqlite3')
cursor = conn.cursor()

for data in datas:
    cursor.execute('INSERT INTO word_list (id, word, paraphrase, classification, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)', (data['id'], data['word'], data['paraphrase'], data['classification'], data['created_at'][0:-10], data['updated_at'][0:-10]))

conn.commit()
conn.close()

