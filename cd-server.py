from BaseHTTPServer import BaseHTTPRequestHandler
import io,shutil    
import urllib2  
import os, sys  
import cgi
import json
import subprocess


class TodoHandler(BaseHTTPRequestHandler):
    def do_resp(self):
        self.send_response(200)

    def do_GET(self):
        return 

    def do_POST(self):
        self.do_resp()
        data = self.rfile.read(int(self.headers['content-length']))  
        post_body = urllib2.unquote(data)[len("payload="):]
        post_body.decode('utf8')
        json_obj = json.loads(post_body)

        print "====================="
        print "New CI result:"
        print "Repo: "+str(json_obj["repository"]["url"])+"/"+str(json_obj["repository"]["owner_name"])\
            +"/"+str(json_obj["repository"]["name"])
        print "Branch: "+str(json_obj["branch"])
        print "commit: \n"+str(json_obj["message"])
        print "committer: "+json_obj["committer_name"]
        print "commit at: "+str(json_obj["committed_at"])
        print "commit: "+str(json_obj["commit"])
        print ""
        print "Build state: "+str(json_obj["state"])
        self.do_deploy(json_obj)

    def do_deploy(self, json_obj):  
        if str(json_obj["state"]) == "passed":
            print "===================="
            print "Deploy"
            print ""
            subprocess.call("git pull")
            print ""
            subprocess.call("./deploy.sh")
            print "deploy ends"
            print "==================="
        else:
            print "===================="
            print "not deploy"
            print "===================="

if __name__ == '__main__':
    # Start a simple server, and loop forever
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('', 8888), TodoHandler)
    print("Starting server, use <Ctrl-C> to stop")
    server.serve_forever()

