"""
这是一个工具集合
"""
"""
用来封装
"""
import json
import traceback
def body_to_dict(body):
    body_dict = {}
    if body is not None:
        body_str = str(body, encoding="utf-8")
        # 字符串转成字典
        body_dict = json.loads(body_str)
        return body_dict
    else:
        return body_dict

def get_request_by_key(req,key):
    if key is not None:
        value = None
        try:
            value = req[key]
        except KeyError:
            value = None
        return value
    else:
        traceback.print_exc()
        return None
