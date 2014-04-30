#SWEETLIME beta
![](https://cdn1.iconfinder.com/data/icons/Limon_iContainer/128/Lime.png)
## SweetLime (beta) for SublimeText3
SweetLime is ST3 plugin to develop Apigee Proxies. With built in template support for policies, steps and flows, SweetLime helps proxy developers build proxies with ease.

[Intro video](https://www.youtube.com/watch?v=W-WDjIkeDcs)
##Installing
###Package Control (Not yet submitted - for now use the other two options)
The easiest way to install this is with Package Control.
To install just go to [Package Control](http://wbond.net/sublime_packages/package_control) and follow the instructions - you probably need to restart Sublime Text 3 before doing this next bit.

Bring up the Command Palette (Command+Shift+p on OS X, Control+Shift+p on Linux/Windows).
Select "Package Control: Install Package" (it'll take a few seconds)
Select **Apigee SweetLime** when the list appears.
Package Control will automatically keep SweetLime up to date with the latest version.

###Without Git: 
Download the latest source from GitHub and copy the SweetLime folder to your Sublime Text "Packages" directory.

###With Git (easiest way as of now): 
Clone the repository in your Sublime Text "Packages" directory:

OSX
> `git clone git@github.com:apigee/Sweetlime.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/ApigeeSweetLime'

Windows
> coming soon (testing underway)

##Using SweetLime

##Create proxy, add policies
SweetLime is very intuitive. Bring up the command pallette (OS X: command + shift + p) and type Apigee to see the list of all possible options Sweetlime provides.

###Apigee: New Proxy
to create a new proxy from scratch
###Apigee: Add Flow to Proxy
to add the flow template to your proxy
###Apigee: Add Step
to add a steps - existing and new
###Apigee: Create New Policy
to create new policy from a list of policy templates
###Apigee: Fetch Policy Templates
to fetch a policy template to a file

[Video: Developing proxies for Apigee Edge](https://www.youtube.com/watch?v=TMVIEFuQr7k)

##Deploying
Proxies developed with SweetLime can be deployed to either the Apigee cloud or your on-prem apigee edge installation (OPDK customers).

SweetLime utilizes the Build framework provided by SublimeText to achieve the deploy feature. 

Proxies created with SweetLime now come with a new json file called "deploy_vars.json" with the following content

```json
{
    "org":"ORGNAME (MANDATORY)",
    "env":"ENVIRONMENT (MANDATORY)",
    "username":"USERNAME (MANDATORY)",
    "password":"PASSWORD" (OPTIONAL), 
    "uri":"MANAGEMENT SERVER URL (OPTIONAL)" 
}
```

[Video: Deploying proxies to Apigee Edge](http://youtu.be/ya1Jt4apFjM)

###password 
If the "password" field is left empty SweetLime tries to read the same from mac's keychain.

To connect to keychain, SweetLime uses an open source python module called "keyring" (https://pypi.python.org/pypi/keyring). Installation of keyring is mandatory if you wish to go the secure way. 

```
$ easy_install keyring 
keyring.set_password("orgname", "username", "password")
```
###uri
If your deploy destination is Apigee cloud then leave this empty, else provide the url to the management server on your OPDK installation

##Credits
Thanks to all the super-geeks who have coded modules like Fetch, STProjectTemplates and many other super awesome sublime plugins that helped me in my endeavor

##Contribute
All proxy developers - please use SweetLime, break it, harass it and ask for feature developments
Want to contribute more? - fork sweetlime, start coding and send me a pull request.

##Licence

All of SweetLime is licensed under the Apache License, Version 2

Copyright (c) 2014 Girish Rangaswamy @ Apigee Corp 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.






