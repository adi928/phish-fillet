# Phish-Fillet
A command line tool used to scrape bulk phishing urls for various data.


![phish-fillet](https://i.imgur.com/AdgnlQw.png)

## Install

**Required**
> git clone https://github.com/00011100/phish-fillet.git

Run this command to clone the git repository to your current working folder.

>pip3 install -r requirements.txt

This should install all required dependencies. Else, the program will ask if you would like to download any missing dependencies.



**Recommended**
>wget https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-links-NEW-today.txt -O raw-urls.txt

This program relies on phishing URLs. You can get hourly updated phishing URLS from Mitchell Krogza's database.

>sort raw-urls.txt | uniqe -w20 > urls.txt

This will assist in sorting and removing any duplicate domain entries.  

## Example

**./fillet.py -gvf urls.txt -d zip php -dd /tmp/found**

**-v** verbose

**-g** enable geo-ip location

**-f** specify the file

**-d** download zip and php file types

**-dd** save downloads to specfied directory

Screenshot of similiar results: https://i.imgur.com/Q0lNoaa.png

## Features

**Random user-agents:** Select a random user agent when sending http requests. Default is phish-fillet user agent.

**Url Exclusions:**    You can pass a list of domains which you wish to exclude from scanning. For exaple, if you want to avoid
                   scanning anything hosted on geocities.. all url's containing something like geocities.com/phishing/blaah/01
                   will be excluded.
                   
**Download Files:**    You can specify a filetype to download. If you want to download every zip file found on the phishing url
                   you can do that. If you want to download every zip,php,txt and css file? You can do that. Just specifiy the 
                   file types.
                   
**Verbose modes:**     There is a verbose mode to spit out additional information to the screen as well as a quiet mode which just 
                   features a progress bar.
                   
## Bugs
### I'm sure there are plenty. 

For starters: urls with specified ports will not be scanned. This is due to defaults within the urlparse function. 
This will be addressed.

The order in which some directories are searched may cause folders to be searched more than once. 
This is something that will be optimized.


## Planned Features

[+] Optimized output results

[+] Optimized folder searching

[+] Min and max size for downloads

[+] Color terminal

[+] Export files found files to CSV list

[+] Zip files for output archiving

[+] statistics / xlsx output file (geoip, etc)

[+] Quick Scan Module for a single url

[+] Option to bypass url and pull/utilize phishing links with curl command

[+] Allow ports in URL

[+] Image Snapshots of Websites (oh no! A wild dependency appears!)

[+] Brute Forcing Module

[+] CLI - Framework Module

[+] Spidering Module

[+] Post Data Module
    -- Find urls once bogus credential data has been posted
