import configparser
config = configparser.ConfigParser()

class database():
    def __init__(self, file: str = "dbw.ink"):
        self.file = file


    #создать класс
    def create(self, classname, json):
        config[classname] = json
    #создать объект в классе
    def createobjecr(self, classname, object, input):
        config[classname][object] = input


    #посмотреть что означает объект в класс-е
    def readobject(self, classname, object, type: "string"):
        if type.lower() == "int":
                return int(config[classname].getint(object))
        elif type.lower() == "float":
                return float(config[classname].getfloat(object))
        elif type.lower() == "string" or type.lower() =="str":
                return str(config[classname].get(object))
        elif type.lower() == "bool" or type.lower() =="boolean":
                return bool(config[classname].getboolean(object))
        elif type.lower() == "list" or type.lower() == "array":
                return config[classname].get(object).replace("[", "").replace("]", "").replace(",", "").split()
        else: return "null"
        
    #количество классов
    def countclass(self, type):
        if type.lower() == "number":
            return len(config.sections())
        elif type.lower() == "name":
            return config.sections()
        else: return "null"
    #количество объектов
    def countobject(self, classname, type):
        if type.lower() == "number":
             return len(config[classname])
        elif type.lower() == "name":
             return list(config[classname])
        else: return "null"
        
    #загрузить/сохранить базу данных
    def readdb(self):
        config.read(self.file)
    def savedb(self):
         with open(self.file, 'w') as configfile:
            config.write(configfile)
