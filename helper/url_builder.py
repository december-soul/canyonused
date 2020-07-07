#https://www.canyon.com/de-de/factory-seconds-outlet-bikes/?cgid=factory-seconds-outlet-bikes&prefn1=pc_familie&prefn2=pc_outlet&prefv1=Endurace%7CSpeedmax&prefv2=true&srule=sort_last_added
#https://www.canyon.com/de-de/factory-seconds-outlet-bikes/?cgid=factory-seconds-outlet-bikes&prefn1=pc_familie&prefn2=pc_outlet&prefv1=Endurace&prefv2=true&srule=sort_last_added
#https://www.canyon.com/de-de/factory-seconds-outlet-bikes/?cgid=factory-seconds-outlet-bikes&pmax=2.000%2C00&pmin=1.000%2C00&prefn1=pc_familie&prefn2=pc_outlet&prefv1=Endurace&prefv2=true&srule=sort_last_added
#https://www.canyon.com/de-de/factory-seconds-outlet-bikes/?cgid=factory-seconds-outlet-bikes&pmax=2.000%2C00&pmin=1.000%2C00&prefn1=pc_familie&prefn2=pc_outlet&prefn3=pc_welt&prefv1=Endurace&prefv2=true&prefv3=Road&srule=sort_last_added

def buildUrl(args):
    website =           "https://www.canyon.com/"
    locale =            "en-%s/" % args.locale
    outlet =            "factory-seconds-outlet-bikes/"
    outletType =        "?cgid=factory-seconds-outlet-bikes"
    price =             "&pmax=%s" % args.max_price
    prefn1 =            "&prefn1=pc_familie"
    prefn2 =            "&prefn2=pc_geschlecht"
    prefn3 =            "&prefn3=pc_outlet"
    prefn4 =            "&prefn4=pc_rahmengroesse"   
    prefv1 =            "&prefv1=%s" % args.model
    prefv2 =            "&prefv2=%s" % args.gender
    prefv3 =            "&prefv3=true"
    prefv4 =            "&prefv4=%s" % args.size
    sorting =           "&srule=sort_price_ascending"
    hideFilters =       "&hideSelectedFilters=true"

    url = "".join([website, 
                    locale, 
                    outlet,
                    outletType,
                    price,
                    prefn1,
                    prefn2,
                    prefn3,
                    prefn4,
                    prefv1,
                    prefv2,
                    prefv3,
                    prefv4,
                    sorting,
                    hideFilters
                ])
    return url

