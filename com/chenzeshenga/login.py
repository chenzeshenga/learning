# Read blocked users from the txt file. Every blocked user will be spilt by the blank;
# blocked users list
blocked_users = []

# Actually there should be try/catch block here in case the blockedUsers.txt doesn't exist or can't be accessed to.
# Since I haven't studied the exception in python yet, so I choose to create the txt file at first.
blocked_user_file = open("blockedUsers.txt", "r")
while True:
    blocked_user = blocked_user_file.readline()
    if not blocked_user:
        break
    blocked_users = blocked_user.split()
blocked_user_file.close()

# for investigation
print("the blocked_users are %s" % blocked_users)

# initial user info
# user list
users = ["user1", "user2", "user3", "user4"]
print("the initial users are %s" % users)
# password list
pwds = ["pwd1", "pwd2", "pwd3", "pwd4"]

# failed log in try
error_count = 0
# username which was tried last time
last_username = ''

while True:
    username = input("please input your username:")
    password = input("please input your password:")

    # identity user whether in blocked_users
    if username in blocked_users:
        print("User %s is blocked, please try other user." % username)
        last_username = username
        error_count += 1
        remaining_tries = 3 - error_count
        print("Fail to login with %s attempts"
              ", with another %s attempts, the system would break" % (error_count, remaining_tries))
        if error_count >= 3:
            print("system breaks")
            break
        continue

    if (username in users) and password == pwds[users.index(username)]:
        last_username = username
        print("User %s, welcome to log in." % username)
        continue
    elif username not in users:
        last_username = username
        print("User %s is not in the initial user list." % username)
        error_count += 1
        remaining_tries = 3 - error_count
        print("Fail to login with %s attempts"
              ", with another %s attempts, the system would break" % (error_count, remaining_tries))
        if error_count >= 3:
            print("system breaks")
            break
    elif (username in users) and password != pwds[users.index(username)]:
        if username == last_username:
            last_username = username
            blocked_user_file = open("blockedUsers.txt", "a")
            blocked_user_file.write(" ")
            blocked_user_file.write(username)
            blocked_user_file.close()
            print("User %s is blocked to log in for too many attempt." % username)
            error_count += 1
            remaining_tries = 3 - error_count
            print("Fail to login with %s attempts"
                  ", with another %s attempts, the system would break" % (error_count, remaining_tries))
            if error_count >= 3:
                print("system breaks")
                break
        else:
            print("Password error for user %s, please try another password. "
                  "If password still gets wrong in next attempt, the user would be blocked." % username)
            error_count += 1
            remaining_tries = 3 - error_count
            print("Fail to login with %s attempts"
                  ", with another %s attempts, the system would break" % (error_count, remaining_tries))
            if error_count >= 3:
                print("system breaks")
                break
