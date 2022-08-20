whitelist = [{'name':'str_1','place':'plc_1','rail':['private','protected'],'port':[100,101,102,103]}, {'name':'str_2','place':'plc_2','rail':['protected'],'port':[201,202]}, {'name':'str_3','place':'plc_3','rail':['private'],'port':[303]}]

for index, row in df.iterrows():

for wl_list in whitelist:
    if wl_list['name'] in row['name']:
        variable = request.get("link",headers=headers).json()
    else:
        variable = None

if row['services'] !=0 :
    for t_service in row['services']:
        if wl_list['name'] != 'global' and variable != None:
            for var in variable :
                if (var['status']== 'active' and var['id'] in service['id']) and ('private' in var['rail'] or 'protected' in var['rail'] ):
                    if wl_list['place'] in var['place']:
                        for wl_rail in wl_list['rail']:
                            if wl_rail in var['rail'] and 'ports' in var.keys():
                                for v_port in var['ports']:
                                    if len(v_port) != 0:
                                        if v_port['from'] == v_port['to']:

                                            if 'private' in wl_rail:
                                                if v_port['from'] in wl_list['port']:
                                                    n_private = 0
                                                else:
                                                    n_private = 1
                                            if 'protected' in wl_rail:
                                                if v_port['from'] in wl_list['port']:
                                                    n_protected = 0
                                                else:
                                                    n_protected = 1
                                        else:
                                            for wl_port in wl_list['port']:
                                                if wl_port > v_port['from'] and wl_port < v_port['to']:
                                                    if 'private' in wl_rail:
                                                if v_port['from'] in wl_list['port']:
                                                    n_private = 0
                                                else:
                                                    n_private = 1
                                            if 'protected' in wl_rail:
                                                if v_port['from'] in wl_list['port']:
                                                    n_protected = 0
                                                else:
                                                    n_protected = 1 


                    else:
                        if 'private' in var['rail']:
                            n_private = 1
                        if 'protected' in var['rail']:
                            n_protected = 1