cursor.execute("Select userName, Password from UserInfo WHERE UserID = 1")
x = [i[0] for i in cursor.fetchall()]
print(x)