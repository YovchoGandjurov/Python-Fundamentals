class Website:
    def __init__(self, host, domain, queries):
        self.host = host
        self.domain = domain
        self.queries = queries

websites = []
inp = input()
print(inp)
while inp != "end":
    data = input().split(" | ")
    print(data)

    if len(data) > 2:
        curr_website = Website(data[0], data[1],
                               [x for x in data[2].split(",")])

    else:
        curr_website = Website(data[0], data[1], '')
   
    websites.append(curr_website)

    inp = input()

print(len(websites))
for item in websites:
    print(f"https://www.{item.host}.{item.domain}", end="")
    if len(item.queries) > 0:
        print(f"/query?=[{']&['.join(item.queries)}]")
