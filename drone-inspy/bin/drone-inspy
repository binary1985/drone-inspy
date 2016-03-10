#!/usr/bin/env python2
# Copyright (c) 2016 Jonathan Broche (@g0jhonny)


import os, sys, json, requests, urlparse, argparse, HTMLParser
from pylair import models
from pylair import client

parser = argparse.ArgumentParser(description='drone-inspy - Import InSpy JSON output into the Lair framework', version="1.0.0")
parser.add_argument('id', help="Lair Project ID")
parser.add_argument('json_file', help="InSpy JSON output file")
parser.add_argument('-k', help="Allow insecure SSL connections", action='store_true')

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
hparser=HTMLParser.HTMLParser()
requests.packages.urllib3.disable_warnings()

try:
    lair_url = os.environ['LAIR_API_SERVER']

    u = urlparse.urlparse(lair_url)
    if u.username and u.password:
        project_id = args.id
        project = dict(models.project)
        project['id'] = project_id
        project['commands'] = [{'command': 'InSpy', 'tool': 'InSpy'}]
        project['tool'] = 'drone-inspy'

        opts = client.Options(u.username, u.password, "{}:{}".format(u.hostname, u.port), project_id, scheme=u.scheme, insecure_skip_verify=args.k)

        with open(args.json_file) as f:
            data = json.load(f)

        for employee in data['employees']:
            employee_name = employee['employeename'].title().strip(',')
            person = dict(models.person)
            person['projectId'] = project_id
            person['principalName'] = employee_name
            person['firstName'] = employee_name.split()[0]
            person['lastName'] = employee_name.split()[-1]
            person['department'] = employee['title']
            person['emails'] = []
            person['emails'].append(employee['email'])

            project['people'].append(person)

        res = client.import_project(project, opts)
        if res['status'] != 'Ok':
            print "[!] {}: {}".format(res['status'], res['message'])
        else: print "[*] Success: Operation completed successfully"
    else:
        print "[!] Error: Missing username and/or password"

except IOError as e:
    print "[!] Error: IOError opening JSON file: {}".format(e)
except KeyError as e:
    print "[!] Missing LAIR_API_SERVER environment variable. {}".format(e)