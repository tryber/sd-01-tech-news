import os.path

valid_Header = ['url', 'title', 'timestamp', 'writer', 'shares_count', 'comments_count', 'summary', 'sources', 'categories']


def validHeader(header, verifyArray=valid_Header):
    isValid = True
    for key in verifyArray:
        isContain = key in header
        if not isContain:
            isValid = False
            break
    if isValid:
        print('Cabeçario valido')
    else:
        raise Exception('Cabeçalho inválido')
    return isValid


def isExist(file):
    if os.path.exists(file):
        print(f'Arquivo {file} encontrado!')
    else:
        raise Exception(f'Arquivo {file} não encontrado!')


def validTypeFile(file, typeFile):
    if not len(file.split('.')) == 2:
        raise Exception('Formato inválido')
    if not file.split('.')[1] == typeFile:
        raise Exception('Formato inválido')
    return True

