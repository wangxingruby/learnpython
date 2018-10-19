from urllib import request
from numpy import unicode
import re
import json
import time

filename = 'write_data.txt' 
with open(filename,'w',encoding='utf-8') as f: 
    # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！ 
    # res = json.dumps(booklist)
    ensure_ascii=False

    s = {'za':'中文','sz':'中文'}
    res = json.dumps(s,ensure_ascii=False)

    f.write(res)
