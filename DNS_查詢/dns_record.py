import dns
import dns.resolver
import dns.rdtypes
import dns.rdtypes.IN.A
import dns.rdtypes.ANY.NS

DN = input('請輸入要查詢網域名稱 ：')
DN_type = input('請輸入要查詢 Record 種類 A or NS :')


for  i  in  range(1,11):

    if 'A' in DN_type:
        pass
    elif 'NS' in DN_type:
        pass
    else:
        print("請確認輸入查詢 Type")
        break

    print("第", i, "查詢")

    try:
        DNS_DIG = dns.resolver.query(DN, DN_type)
        for ans in DNS_DIG.response.answer:
            for r in ans:
                if type(r) == dns.rdtypes.IN.A.A:
                    print(DN, DN_type, "Record ：", r)
                elif type(r) == dns.rdtypes.ANY.NS.NS:
                    print(DN, DN_type, "Record ：", r)

    except dns.resolver.NXDOMAIN:
        print("您所查詢", DN, DN_type, "Record 無記錄")
        break
    except  dns.resolver.NoAnswer:
        print("您所查詢", DN, DN_type, "Record 無記錄")
        break
    except  dns.rdatatype.UnknownRdatatype:
        print("您所查詢", DN, DN_type, "Record 無記錄")
        break
    except  dns.exception.Timeout:
        print("您所查詢", DN, DN_type, "Record 無記錄")
        break

    print()