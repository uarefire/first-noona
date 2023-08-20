filename = "very_important"
data = "secret data"

f = open(filename, "w") #filename 을 open하겠다 "write"로
f.write(data)
print("wroted")
f.close()

