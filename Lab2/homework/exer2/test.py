for tr in tr_list:

    solieu = tr.find_all('td',{'style':"width:15%;padding:4px;color:#014377;font-weight:bold;"})
    tieude = tr.find('td',{'style':"width:32%;color:#014377;font-weight:bold;"})
    if tieude != None:
        list2 = []
        for item in solieu:
            so_lieu = item.string
            list2.append(so_lieu)
        bao_cao = dict(zip(list1,list2))
        bao_cao['Title'] : tieude.string


        solieu = tr.find_all('td',{'style':"width:15%;padding:4px;color:#014377;"})
        tieude_ = tr.find('td',{'style':"width:32%;color:#014377;"})
    if tieude_ != None:
        list2 = []
        for item in solieu:
            so_lieu = item.string
            list2.append(so_lieu)
        bao_cao = dict(zip(list1,list2))
        bao_cao['Title'] : tieude_.string

    ban_bao_cao.append(bao_cao)

import pyexcel
pyexcel.save_as(records= ban_bao_cao, dest_file_name= 'ban_bao_cao.xlsx')
