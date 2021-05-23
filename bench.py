import dns.resolver

DNS_SERVERS = {
    "Google-1": "8.8.8.8",
    "Google-2": "8.8.4.4",
    "opendns-1": "208.67.222.222",
    "opendns-2": "208.67.220.220",
    "CloudFlare-1": "1.1.1.1",
    "Cloudflare-2": "1.0.0.1",
    "Quad9-1": "9.9.9.9",
    "Quad9-2": "149.112.112.112",
    "Softlayer": "169.38.73.5",
    "Reliance-1": "202.138.120.86",
    "Reliance-2": "202.138.120.4",
    "Reliance-3": "202.138.120.6",
    "artech": "202.86.251.201",
    "SignNet": "115.42.228.246",
    "Mobile1-Singapore-1": "118.189.211.221",
    "DigitalOcean-Singapore-1": "128.199.241.188",
    "DigitalOcean-Singapore-2": "128.199.102.32",
    "Default Server": None,
}


def query_dns(domain):
    responses = []
    for name, server in DNS_SERVERS.items():
        my_resolver = dns.resolver.Resolver()
        if server:
            my_resolver.nameservers = [
                server,
            ]
        try:
            resp = my_resolver.resolve(domain, "A")
            timing = resp.response.time * 1000
            print( f"Processed : {name}")
            responses.append(
                (
                    name,
                    timing,
                )
            )
        except Exception as e:
            print(name, ":failed" + str(e))
    responses = sorted(responses, key=lambda x: x[1])
    print(f"Best option 1: {responses[0][0]} ({responses[0][1]} msecs)")
    print(f"Best option 2: {responses[1][0]} ({responses[1][1]} msecs)")
    print(f"Best option 3: {responses[2][0]} ({responses[2][1]} msecs)")


query_dns("www.vivekv.info")
