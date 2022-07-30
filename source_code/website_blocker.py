#The code bellow can be used if you want to block the websites for a certain amount of time
#from datetime import datetime
#end_time = datetime(2030, 6, 6, 20)

block = False
answer = input("Do you want to block the stupid bulgarian news sites? ")
if answer.lower() == "yes":
    block = True
else:
    print("unblocking...")
sites_blocked = ["dir.bg", "www.dir.bg", "btvnovinite.bg", "www.btvnovinite.bg", "nova.bg", "www.nova.bg","bntnews.bg", "www.bntnews.bg", "dnevnik.bg", "www.dnevnik.bg"]

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"


def block_sites():
    if block:
        print("block sites")
        with open(hosts_path, "r+") as hostsfile:
            hosts_content = hostsfile.read()
            for site in sites_blocked:
                if site not in hosts_content:
                    hostsfile.write(redirect + " " + site + "\n")
    else:
        print("unblock sites")
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