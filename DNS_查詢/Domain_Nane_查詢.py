import dns
from dns import resolver
from dns import rdtypes


DN = input('請輸入要查詢網域名稱 ：')
DN_type = input('請輸入要查詢 Record 種類 A or NS :')

for i in range(1,11):

    if 'A' in DN_type:
        pass
    elif 'NS' in DN_type:
        pass
    else:
        print("請確認輸入查詢 Type")
        break

    try:
        DNS_DIG = resolver.Resolver()
        DNS_DIG.nameservers = ['8.8.8.8']
        answers = DNS_DIG.resolve(DN, DN_type)
        for ans in answers.response.answer:
            #print(ans)
            for r in ans:
                print(type(r))
                if isinstance(r, rdtypes.IN.A.A):
                    print("第", i, "次查詢", DN, DN_type, "Record ：", r)
                elif isinstance(r, rdtypes.ANY.NS.NS):
                    print("第", i, "次查詢", DN, DN_type, "Record ：", r)

    except dns.resolver.NXDOMAIN:
        print("您所查詢", DN, DN_type, "Record 無記錄")
    except  dns.resolver.NoAnswer:
        print("您所查詢", DN, DN_type, "Record 無記錄")
    except  dns.rdatatype.UnknownRdatatype:
        print("您所查詢", DN, DN_type, "Record 無記錄")