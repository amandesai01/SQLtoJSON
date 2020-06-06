import requests
import json

class AuthErrorException(Exception):
    """ Access Denied for given set of credentials """
    pass

class ServerError(Exception):
    """ Error while communication to db"""
    pass

class s2j:
    def __init__(self, host, username, password, database):
        self.__username = username
        self.__password = password
        self.__host = host
        self.__database = database
        self.__authenticate(host, username, password, database)
        self.__history = []

    def __authenticate(self, username, password):
        data = { 'username': username , 'password': password }
        rawres = requests.get("", json = data).json()
        if rawres['status'] == 'failure':
            raise AuthErrorException
        else:
            self.__header = {'token' : rawres['token']}

    def execQuery(self, query):
        data = {'query' : query}
        headers = {'token' : self.__header}
        rawres = requests.get("https://127.0.0.1:4909/execQuery", json = data, headers = headers).json()
        history_element = {}
        history_element['query'] = query
        history_element['success'] = False
        history_element['response'] = None
        history_element['error'] = None
        if rawres.get['status'] == "failure":  
            print(rawres.get("error_message"))
            history_element['error'] = rawres.get("error_message")
            self.__history.append(history_element)
            return None
        history_element['success'] = True
        history_element['response'] = rawres.get("data")
        return rawres