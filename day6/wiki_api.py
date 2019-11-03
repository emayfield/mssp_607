
import hashlib, os, json, requests
from lxml import etree

# Input: Page name of a Wikipedia article.
# 
# Returns: Full HTML source of the named article if it exists,
#          or None if no such page exists.
def __api_GET_latest_page(title):
    parameters = {
        "action": "parse",
        "page": title,
        "format": "json"
    }
    response_json = __get("revisions", title, parameters)
    if("parse" in response_json.keys() 
        and "text" in response_json["parse"].keys() 
        and "*" in response_json["parse"]["text"].keys()):
        return response_json["parse"]["text"]["*"]
    return None    

# Internal function to hide a caching API request into a single private function.
# This function will save you a lot of headaches in writing your own HTTP requests
# and will save the Wikimedia foundation some bandwidth since you'll fetch a local
# copy if you have already retrieved an article text at least once.
def __get(function_key, key, parameters, check_cache=True, write_cache=True):
    target = "https://en.wikipedia.org/w/api.php"
    cache_path = "cached_api"
    params_unicode = str(parameters).encode('utf-8')
    md5 = hashlib.md5(params_unicode).hexdigest()
    return_json = None

    cache_file = os.path.join(cache_path, function_key, str(key), md5)
    cache_exists = os.path.isfile(cache_file)
    if cache_exists:
        try:
            json_in = open(cache_file, "r")
            json_str = json_in.read()
            return_json = json.loads(json_str)
            if "error" in return_json.keys() and "code" in return_json["error"].keys() and return_json["error"]["code"]=="maxlag":
                cache_exists = False
        except:
            cache_exists = False

    if not cache_exists:
        cache_dir = os.path.dirname(cache_file)
        if not os.path.isdir(cache_dir):
            os.makedirs(cache_dir)
        r = requests.get(target, params=parameters)
        request_json = r.json()
        json_out = open(cache_file, "w")
        print(json.dumps(request_json), file=json_out)
        return_json = request_json
    return return_json

# This function takes as input a parsed HTML tree and returns the same
# tree but with a set of tags removed, mostly the contents of tables and scripts.
# This makes parsing the actual contents of a page easier.
def __remove_tables_and_scripts(tree):
    tags_to_remove = ["tbody", "td", "script"]
    for tag in tags_to_remove:
        elements = tree.find(f".//{tag}")
        if elements is not None:
            for e in elements:
                e.getparent().remove(e)
    return tree

# This function takes two required and one optional parameters as input.
#
# Required:
# name: Name of a Wikipedia page to retrieve.
# format: Type of content that you want returned. Options include:
#         "html" : Full HTML content of the page you requested.
#         "text" : Full content of the page you requested as a single string,
#                  with all HTML tags removed.
#         "list" : Full content of the page you requested with all HTML removed,
#                  but each paragraph on the page is a separate string, and the
#                  page as a whole is returned to you as a list of paragraphs.
#
# Optional:
# include_tables: By default, all tables and scripts in the HTML text will be 
#                 removed from the text that gets sent back to you. If you want
#                 to include that content, you can pass in True instead.
#
# This function returns the content of the page in the format that you specified.
def page_text(name, format, include_tables = False):
    try:
        result = __api_GET_latest_page(name)
    except:
        print("API request failed.")
    if result:
        e = etree.fromstring(result)
        if not include_tables:
            e = __remove_tables_and_scripts(e)
        if format == "html":
            return str(etree.tostring(e))
        elif format == "text":
            return ''.join(e.itertext())
        elif format == "list":
            return ''.join(e.itertext()).split('\n')
    else:
        print("Failed to retrieve a page.")
        return None