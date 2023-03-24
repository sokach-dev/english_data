import json
import sqlite3

# 读取JSON文件
with open('story.json', 'r') as f:
    datas = json.load(f)

# 将数据插入到SQLite数据库
conn = sqlite3.connect('/Users/lele/develop/vue/orion-app/data/db.sqlite3')
cursor = conn.cursor()

for data in datas:
    cursor.execute('INSERT INTO story (id, words, content, read_count, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)', (data['id'], ",".join(data['words']), data['content'], data['read_count'], data['created_at'][0:-10], data['updated_at'][0:-10]))

conn.commit()
conn.close()

