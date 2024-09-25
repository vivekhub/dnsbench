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
    # "Reliance-India-1": "202.138.120.86",
    # "Reliance-India-2": "202.138.120.4",
    # "Reliance-India-3": "202.138.120.6",
    # "artech": "202.86.251.201",
    "SignNet": "115.42.228.246",
    "Mobile1-Singapore-1": "118.189.211.221",
    "Default Server": None,
    "My Server": "192.168.2.25",
}


def query_dns(domain):
    responses = []
    for name, server in DNS_SERVERS.items():
        my_resolver = dns.resolver.Resolver(configure=False)
        if server:
            my_resolver.nameservers = [
                server,
            ]
        try:
            resp = my_resolver.resolve(domain, "A")
            timing = resp.response.time * 1000
            print(f"Processed : {name} \t with time: {timing:.1f} msecs")
            responses.append(
                (
                    name,
                    timing,
                )
            )
        except Exception as e:
            print(name, ":failed" + str(e))
    responses = sorted(responses, key=lambda x: x[1])

    for i in range(0, 3):
        print(f"Best option {i+1}: {responses[i][0]} ({responses[i][1]:.2f} msecs)")


query_dns("www.vivekv.info")
