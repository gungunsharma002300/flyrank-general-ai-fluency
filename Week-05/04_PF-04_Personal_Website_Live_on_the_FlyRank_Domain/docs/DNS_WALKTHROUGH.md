# PF-04 DNS Walkthrough — Gungun Sharma

## What DNS does

DNS (Domain Name System) is the system that turns a human-friendly website name into the network address a browser can use. Instead of remembering an IP address, a visitor types a name such as `gungunsharma.netlify.app`. DNS helps the browser discover where that name should go.

## What a CNAME record is

A CNAME (Canonical Name) record is an alias. It tells DNS that one hostname should resolve through another hostname. For example, if `www.example.com` has a CNAME pointing to `example.netlify.app`, the DNS system follows that alias and eventually reaches the host responsible for the site. CNAMEs are normally used for hostnames such as `www`; the root/apex domain has different DNS constraints and is usually handled with the DNS provider's supported records.

## What happens when someone opens the site

1. The visitor types the website address into the browser.
2. The browser and operating system first check their local DNS caches. If they already know the answer and it has not expired, they can reuse it.
3. If the answer is not cached, the device asks a recursive DNS resolver, usually provided by the network, ISP, or a public DNS service.
4. The resolver finds the authoritative nameserver for the domain and asks it for the relevant DNS record.
5. The authoritative server returns the record (for example, an A/AAAA record or a CNAME chain that ultimately leads to the hosting destination).
6. The resolver gives the result back to the device and caches it for the record's TTL.
7. The browser can now connect to the hosting service. For an HTTPS site, the browser also performs TLS/HTTPS setup so the connection is encrypted.
8. The host receives the HTTP request, finds the requested site/file, and sends the page back to the browser.

The important idea is that DNS is the naming layer. It does not itself send the webpage. DNS helps the browser discover where to connect; HTTPS and HTTP then handle the secure connection and the actual web request/response.

## For this portfolio

This project uses a free Netlify URL for the assignment. A custom domain is not required now. If I connect one later, I will configure the DNS records at the domain/DNS provider, verify the records, and let Netlify provision HTTPS for the site. I should always check the final DNS values in the hosting provider's current instructions rather than copying an old example.
