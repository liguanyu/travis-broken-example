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
        json_obj = json.loads(post_body)

        print "====================="
        print "New CI result:"
        print "Repo: "+json_obj["repository"]["url"]+"/"+json_obj["repository"]["owner_name"]\
            +"/"+json_obj["repository"]["name"]
        print "Branch: "+json_obj["branch"]
        print "commit: \n"+json_obj["message"]
        print "committer: "+json_obj["committer_name"]
        print "commit at: "+json_obj["committed_at"]
        print "commit: "+json_obj["commit"]
        print ""
        print "Build state: "+json_obj["state"]
        self.do_deploy(json_obj)

    def do_deploy(self, json_obj):  
        if json_obj["state"] == "passed":
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

