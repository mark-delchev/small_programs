#The code bellow can be used if you want to block the websites for a certain amount of time
#from datetime import datetime
#end_time = datetime(2030, 6, 6, 20)
sites_blocked = []
user = input("How many websites do you want to block? ")
number_of_websites = int(user)
for website in range(number_of_websites):
    website_to_block = input()
    sites_blocked.append(website_to_block)
block = False
print(*sites_blocked, sep=", ")
answer = input("Are you sure you want to block these websites?(If your answer is no the sites will be unblocked) ")
if answer.lower() == "yes":
    block = True
else:
    print("unblocking...")

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"


def block_sites():
    if block:
        print("The websites were blocked")
        with open(hosts_path, "r+") as hostsfile:
            hosts_content = hostsfile.read()
            for site in sites_blocked:
                if site not in hosts_content:
                    hostsfile.write(redirect + " " + site + "\n")
    else:
        print("The websites were unblocked")
        with open(hosts_path, "r+") as hostsfile:
            lines = hostsfile.readlines()
            hostsfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_blocked):
                    hostsfile.write(line)
            hostsfile.truncate()


if __name__ == "__main__":
    block_sites()
input("Press any key to exit")
