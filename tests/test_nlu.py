import json

def test_nlu_intents():
    pass 

def test_date_slot():
    sentence = '2020年7月20日是我的生日'
    import jieba
    import jieba.posseg as pseg
    words = pseg.cut(sentence)