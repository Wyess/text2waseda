#!/usr/bin/env python3

import re
#import MeCab
import janome.tokenizer
import yaml

def parse(in_txt='in.txt', raw=False, dic_merge_split_yaml=''): 
    with open(in_txt, 'r') as f:
        text = f.read()

    s = '表層形,品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音,符号クラス\n'
    #m = MeCab.Tagger()
    #s += m.parse(text)
    t = janome.tokenizer.Tokenizer()
    
    for token in t.tokenize(text):
        s += f"{token}\n"

    s = re.sub('\t', ',', s)

    if raw:
        return s

    with open(dic_merge_split_yaml) as stream:
        docs = yaml.safe_load_all(stream)
        dic = next(docs)

        for entry in dic:
            target = r'\S*?\n'.join(entry[:-1] + [''])
            s = re.sub(rf"^{target}", f"{entry[-1]}\n", s, flags=re.MULTILINE|re.DOTALL)

        #print(s)
        
        while True:
            m = re.search(r'(?P<quoted>^".+?\n".+?\n)', s, re.MULTILINE | re.DOTALL)
            #m = re.search(r'(?P<quoted>^「.+?\n」.+?\n)', s, re.MULTILINE | re.DOTALL)
            if m:
                word = ''
                yomi = ''
                for line in m.group('quoted').splitlines()[1:-1]:
                    word += line.split(',')[0]
                    yomi += line.split(',')[-1]
                
                new = f"{word},{'*,' * 8}{yomi}\n"
                orig = m.group(0)
                s = re.sub(re.escape(orig), new, s)
            else:
                break
    return s

if __name__ == '__main__':
    print(parse('in.txt'), end='')
