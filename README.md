# Summary :
This tool created for Active directory federation system [ADFS] Username enumeration according to a bug discoverd by Binary1985.</br>
idpinitiatedsignon endpoint is a feature that shouldn't be publicly accesiable by anyone.</br>
You can enumerate the usernames depending on the server response.

## NOTE 
Before using the tool, If you have valid username use it to determine the response time for the valid user and edit it in the script line 35.
This tool can produce false postivies because we are relaying on the server response and that can be affected by many factors. 

I created this tool only for educational purposes.

# How to use : 
> python3 ADFS-Enumeration.py -t https://example.com -w usernames.txt -d exmple.com






