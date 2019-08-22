#Python program
#import os
#os.system("./ansibleAdhoc.bash")

#declaration of variables

hospital="Sunny Brook Health"

#insert the top of the html code into the html file
html_code_top="""<!DOCTYPE html>
<html>
<head>
<style>
table {{
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}}

td, th {{
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}}

tr:nth-child(even) {{
  background-color: #dddddd;
}}
</style>
</head>
<body>

<h2>{site}</h2>
<table>
      <tr>
         <th>Server</th>
         <th>Cache Version</th>
         <th>OS Version</th>
         <th>Apache Version</th>
      </tr>
      <tr>""".format(site=hospital)

file = open("site_audit.html","w+")

#insert the above code into
file.write(html_code_top)

#close the sites.html file
file.close()

def appendValueInTableRow(value, endOfRow):
       file = open("site_audit.html","a")
       append_rows = """        <td>{value}</td>""".format(value=value)
       file.write(append_rows)
       if endOfRow == True:
                file.write("</tr> <tr>")
       file.close()

def closeHTMLFile():

       file = open("site_audit.html","a")
       append_rows = "</table></body></html>"
       file.write(append_rows)
       file.close()


def main():
        #open the ansible output file
        file = open("audit.txt","r")

        #contents = file.read()
        #print(contents)

        lines = file.readlines()
        #Parse the output of ansible and gather SERVER, Cache_Version, OS_Version, and Apache_Version from file
        for x in lines:
                data = x.split("^")

                if data[0] == "SERVER":
                        server = data[1]
                        appendValueInTableRow(server,False)

                        cache_version = data[3]
                        appendValueInTableRow(cache_version,False)

                if data[0] == "OS_Version":
                        os_version = data[1]
                        appendValueInTableRow(os_version,True)

                if data[0] == "Apache_Version":
                        apache_version = data[1]
                        appendValueInTableRow(apache_version,True)

        #close the audit.txt file
        file.close()

        closeHTMLFile()


if __name__ == "__main__":
        main()
