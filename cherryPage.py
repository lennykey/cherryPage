import cherrypy
import glob
import os
from jinja2 import Template, Environment, PackageLoader
import simplejson as json


#jinja2 environment
jinjaEnv = Environment(loader=PackageLoader('cherryPage', 'templates'))


class OnePage(object):
    @cherrypy.expose
    def index(self):
        return "one page!"


class Trenner(object):
    @cherrypy.expose
    def blog(self, jahr, monat, tag):
        content = jahr,monat,tag

        return content

#root = Trenner()

class Formular(object):

    @cherrypy.expose
    def index(self, username=None, password=None):

        content = []
        content.append('<html>')
        content.append('<head>')
        content.append('</head>')
        content.append('<body>')
        content.append('''
                        <form action="/formular" method="get">
                            <p>Username</p>
                            <input type="text" name="username" value=""
                            size="15" maxlength="40"/>
                            <p>Password</p>
                            <input type="password" name="password" value=""
                            size="10" maxlength="40"/>
                            <p><input type="submit" value="Login"/></p>
                            <p><input type="reset" value="Clear"/></p>
                        </form>
                        ''')

        content.append('username: %s passwort: %s' % (username,password))
        content.append('</body>')
        content.append('</html>')

        return content



class HelloWorld(object):
    # Wird direkt im Root unter onepage aufgerufen
    onepage = OnePage()
    formular = Formular()
    trenner = Trenner()
    
    @cherrypy.expose
    def index(self, cool=None):
        #superRoot = os.getcwd()
        #os.chdir("/home/mars/programmieren/python/")

        return 'Hello myWorld <a href="/formular">Link</a>'
    # Wird aufgerufen unter dem Namen repositories direkt im Root
    @cherrypy.expose
    def repositories(self, path):
        myFiles = []

        #print(path)
        splitted = path.split('.')
        newPath = '/'.join(splitted)
        #print(splitted)
        #print(newPath)
        for dirpath, dirname, filename in os.walk('/home/mars/%s' % newPath):
            for name in dirname:
                #print('working')
                if name.endswith('.git') and name != '.git':
                    myFiles.append('git clone mars@mars-pc:' + os.path.join(dirpath, name))

        #print(myFiles)
        entries = []
        entries.append('<html>')
        entries.append('<body>')
        entries.append('<ul>')
        for entry in myFiles:
            entries.append('<li>' + entry + '</li>')
        entries.append('</ul>')
        entries.append('</body>')
        entries.append('</html>')

        return entries 

#cherrypy.quickstart(HelloWorld())


class CherryPage(object):
    # Wird direkt im Root unter onepage aufgerufen
    onepage = OnePage()
    formular = Formular()
    trenner = Trenner()

    @cherrypy.expose
    def index(self):
        #template = Template('Hello {{ name }}!')
        #testjson = json.load('testJson.json') 
        linksFile = open('links.json', 'r')
        pwd = os.getcwd() 
        print("Ort: " + os.getcwd())
        #print(links)
        linksList = json.load(linksFile) 
        #google = {'Google' : 'http://www.google.de', 'Gmail' :'http://mail.google.com'}
        #social = {'facebook' : 'http://www.facebook.de',
        #          'Google+':'https://plus.google.com',
        #          'Xing' : 'http://www.xing.de'
        #         }
        #fun = {'Reddit' : 'http://www.reddit.com'}

        #print(linksList)
        #for key, value in linksList.items():
        #    print(key)
        #    for subkey, subvalue in value.items():
                #print('cool')
               #if(subvalue is type({})):
        #        while(isinstance(subvalue, dict)):
        #            #print("Dict")
        #            for subsubkey, subsubvalue in subvalue.items():
        #                print(subsubval ue)




        template = jinjaEnv.get_template('index.html')
        return template.render(name='John Doe', linksList=linksList, pwd=pwd)


cherrypy.tree.mount(CherryPage())
# CherryPy autoreload must be disabled for the flup server to work
cherrypy.config.update({'engine.autoreload_on':False})