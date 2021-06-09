from generator import *
output = Generator()
output.create_diag("mon diag")
output.create_cluster("my cluster")
output.create_element('Server')
output.create_element('Lambda')
output.create_link("Server", "Lambda")

print(output.output)

with open("output.py", "r+")as f:
    f.write(output.output)