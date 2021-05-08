import dns
import dns.resolver

try:
    A = dns.resolver.query('123.104.com.tw', 'A')
except dns.resolver.NXDOMAIN:
    print("fail")
#except dns.resolver.NoAnswer:
#    print("fail")