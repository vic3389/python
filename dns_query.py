import argparse
import dns.resolver
import dns.exception


def query(domain: str, record_type: str, nameserver: str) -> list[str] | None:
    """Return a list of record texts or None when not found."""
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [nameserver]
    try:
        answers = resolver.resolve(domain, record_type)
        return [r.to_text() for r in answers]
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer,
            dns.rdatatype.UnknownRdatatype, dns.exception.Timeout):
        return None


def main() -> None:
    parser = argparse.ArgumentParser(description="簡易 DNS 查詢工具")
    parser.add_argument("domain", help="要查詢的網域名稱")
    parser.add_argument("record_type", choices=["A", "NS"],
                        help="查詢 Record 類型")
    parser.add_argument("--nameserver", default="8.8.8.8",
                        help="DNS server (預設: 8.8.8.8)")
    parser.add_argument("--retry", type=int, default=1,
                        help="失敗時重試次數")
    args = parser.parse_args()

    for i in range(1, args.retry + 1):
        result = query(args.domain, args.record_type, args.nameserver)
        if result:
            for r in result:
                print(f"第 {i} 次查詢 {args.domain} {args.record_type} Record ： {r}")
            break
        else:
            print(f"第 {i} 次查詢失敗，無記錄")
    else:
        print(f"查詢 {args.domain} {args.record_type} 無記錄")


if __name__ == "__main__":
    main()
