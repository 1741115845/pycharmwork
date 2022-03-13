import yaml

def read_yaml():
    with open('login.yaml','r',encoding='utf-8') as f:
        return yaml.safe_load(f)
if __name__=='__main__':
    read_yaml()