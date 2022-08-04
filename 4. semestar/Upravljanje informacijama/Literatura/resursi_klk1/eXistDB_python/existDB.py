import httplib2

class ExistDB:

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def construct_url(self, name, collection='', xpath=''):
        url = self.url

        if collection != '':
            url+='/'+ collection
             
        url+='/'+name

        if xpath != '':
            url+='?_query='+xpath

        return url

    def create_document(self, collection, name, document):
        req = httplib2.Http()
        headers = {
            'Content-Type': 'application/xml'
        }
        req.add_credentials(self.username,self.password)
        url=self.construct_url(name, collection)
        resp, _ = req.request(url, "PUT", body=document, headers=headers)
        
        if resp.status == 401:
            print("Bad Credentials")

        if resp.status != 201:
            print("Document wasn't added to the database")
    
    def read_document(self, name, collection, xpath=''):
        req = httplib2.Http()
        headers = {
            'Content-Type': 'application/xml'
        }
        req.add_credentials(self.username,self.password)
        url=self.construct_url(name, collection, xpath=xpath)
        resp, content = req.request(url, "GET", headers=headers)
        
        if resp.status == 401:
            print("Bad Credentials")
            return

        if resp.status==404:
            print("Document wasn't found")
            return

        #Converting byte array to string
        content=content.decode("utf-8")
        return content;
