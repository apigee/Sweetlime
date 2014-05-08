import os
import json
import subprocess
from pprint import pprint


def maintainDefaults():
	print('------------------------------------------------------------------')	
	print("APIGEE SWEETLIME: Deploy Proxy | uses 'apigeetool deployproxy' cmd")
	print('------------------------------------------------------------------')
	os.environ['proxy'] = os.path.basename(os.getcwd())
	os.environ['dir'] = os.getcwd()

def extractDeployVars():
	maintainDefaults()
	json_data=open('deploy_vars.json')
	data = json.load(json_data)
	json_data.close()
	validateAndDeploy(data)


def validateAndDeploy(data):
#optional fields
	os.environ['uri'] = data['uri']
	os.environ['basepath']= data['basepath']
	os.environ['displayname']= data['displayname']

#mandatory ones
	if data["env"] and data["org"] and data["username"]:
		os.environ['user'] = data["username"]
		os.environ['org']  = data["org"]
		os.environ['env'] = data["env"]
		if not data["password"] or data["password"] is None:
			print("INFO: Picked up values for Organisation, Environment & Username")
			print("INFO: No Password specified in 'deploy_vars.json' - trying to access Mac keychain")
			try:
				import keyring
				os.environ['pass'] = keyring.get_password(os.environ['org'],os.environ['user']) or ""
				if not os.environ['pass']:
					print("ERROR: Maintain password either in 'deploy_vars.json' or in Mac Keychain | Deploy suspended")
				else:
					print("INFO: Password found in Mac Keychain ")
					print("INFO: Started Deploying")
					deployApi()
			except Exception, e:
				print('ERROR: ' + str(e));
		else:
			print("INFO: Picked up values for Organisation, Environment, Username & Password")
			os.environ['pass'] = data["password"]
			print("INFO: Started Deploying")
			deployApi()

	else:
		print("ERROR: Maintain values for 'org', 'env','username' in 'deploy_vars.json' | Deploy suspended")

def deployApi():
	command = "/usr/local/bin/apigeetool deployproxy -o $org -e $env -u $user -p $pass -d $dir"
	
	if os.environ['displayname']:
		command += " -n $displayname"
	else:
		command += " -n $proxy"

	if os.environ['uri']:
		command += " -l $uri"

	if os.environ['basepath']:
		command += " -b $basepath"

	print("INFO: This takes a while - anywhere from 30 - 50 secs on Apigee cloud (psst:'ctrl+c' will cancel deploying)")

	p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	output, errors = p.communicate()

	print('');
	print('------------------------------------------------------------------')
	print('Result')
	print('------------------------------------------------------------------')

	print output


# in hook 
extractDeployVars()