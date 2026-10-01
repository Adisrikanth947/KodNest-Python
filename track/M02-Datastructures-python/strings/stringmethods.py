# Case converstion methods 
s="Srikanth Adisri"
print(s.lower())
print(s.upper())
print(s.title())
print(s.swapcase())
print(s.capitalize())

#searching & counting
print(s.find("sri"))
print(s.count("a"))
# start and end check
print(s.startswith("Sri"))
print(s.endswith("sri"))

# splittig & joining

ss="Srikanth studying in kodnest 947"
print("Split:",ss.split())
print("join:","-".join(ss))

# Strip spaces 
print("strip:",ss.strip())
print("lstrip:",ss.lstrip())
print("rstrip:",ss.rstrip())            

# checkinng methods 
print("isaplha:",ss.isalpha())
print("isspace:",ss.isspace())
print("isdigit:",ss.isdigit())
print("isalnum:",ss.isalnum())

# replace 
print("replace:('947','20272'):",ss.replace("947","20272"))
#length
print("length is:",len(ss))