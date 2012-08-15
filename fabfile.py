from fabric.api import local, settings

def stop(port):
    ''' Usage: stop:port'''
    #local('lsof %s')
    with settings(warn_only=True):
        print('Hello World') 
        process = local('lsof -i :%s | grep LISTEN' % port, capture=True)
        if process.failed:
            print("No such a port is listening")
        else:
            #print(process)
            #print(process.split())
            lsofList = process.split()
            pid = lsofList[1]
            local('kill -9 %s' % pid)

def start(configfile):
    ''' Usage: start:configfile'''
    local('cherryd -i cherryPage -c %s &' % configfile)
