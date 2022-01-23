import yaml
import json

if __name__ == '__main__':
    stream = open("sample.yaml", 'r')
    dictionary = yaml.load(stream, Loader=yaml.FullLoader)
    try:
        for key, value in dictionary.items():
            print (key + " : " + str(value))
        json_data_string = json.dumps(dictionary)
        print(json_data_string)
    except Exception as e:
        print("e",e)
