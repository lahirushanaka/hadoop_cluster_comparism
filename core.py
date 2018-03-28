import Source, requests, csv, json, os
"""
Auther - Lahiru Shanaka Fernando
Country - Sri Lanka
Email - lahirushanaka@gmail.com
"""



try:
    os.remove('compare.txt')
except OSError:
    pass

server2_tags = {}
server1_tags = {}

server_2_tags = requests.get(Source.URL_2 + "/api/v1/clusters/" + Source.Cluster_name_2 + "?fields=Clusters/desired_configs", auth=(Source.username_2,Source.password_2), verify=False )
J2 = server_2_tags.json()['Clusters']['desired_configs']
server_1_tags = requests.get(Source.URL_1 + "/api/v1/clusters/" + Source.Cluster_name_1 + "?fields=Clusters/desired_configs", auth=(Source.username_1,Source.password_1), verify=False )
J1 = server_1_tags.json()['Clusters']['desired_configs']
#print J1

server1_tags = {key:value for key, value in  J1.items() if key in Source.tags}

server2_tags = {key:value for key, value in  J2.items() if key in Source.tags}

server1 = {}
server2 = {}



for i in Source.tags:
    print i
    with open('compare.txt', 'a') as filec:
        filec.write(i)
        filec.write('\n')


    if i not in server1_tags:
        #print i + " " + " Not available"
        server1[i] = "EMPTY"
        #continue
#    print i
    elif i not in  server2_tags:
        server2[i] = "EMPTY"
    else:

        tag_v_1 = server1_tags[i]['tag']
        tag_v_2 = server2_tags[i]['tag']
        #print  tag_v_1
        srv1 = requests.get(Source.URL_1 + "/api/v1/clusters/" + Source.Cluster_name_1 + "/configurations?type=" + i +"&tag=" + tag_v_1, auth=(Source.username_1,Source.password_1), verify=False )
        PRTS_1 = srv1.json()
        server1[i] = PRTS_1['items'][0]['properties']
        A = []
        B = []

        #print "server 1"
        for prt1 in server1[i]:
            A.append(prt1)
            #print prt1
        srv2 = requests.get(Source.URL_2 + "/api/v1/clusters/" + Source.Cluster_name_2 + "/configurations?type=" + i +"&tag=" + tag_v_2, auth=(Source.username_2,Source.password_2), verify=False )
        PRTS_2 = srv2.json()
        server2[i] = PRTS_2['items'][0]['properties']
        for prt2 in server2[i]:
            #print prt2
            B.append(prt2)
        AB = A + B
        C = set(AB)
        C = [x for x in C if x != 'content']

        for prot in C:
            with open('compare.txt', 'a') as filec:


                if prot not in server1[i] and prot in server2[i]:
                    print(prot +"~"+"Not Available" + "~" + server2[i][prot])

                    filec.write(prot +"~"+"Not Available" + "~" + server2[i][prot] + '\n')
                elif prot in server1[i] and prot not in server2[i]:
                    print(prot + "~" + server1[i][prot] + "~" + "Not Available" )
                    #with open('compare.txt', 'a') as filec:
                    filec.write(prot + "~" + server1[i][prot] + "~" + "Not Available" + '\n')
                elif prot in server1[i] and prot in server2[i]:
                    print(prot + "~" + server1[i][prot] + "~" + server2[i][prot])
                    #with open('compare.txt', 'a') as filec:
                    filec.write(prot + "~" + server1[i][prot] + "~" + server2[i][prot]+ '\n')
                else:
                    print(prot + "~" + "Not Available" + "~:" + "Not Available")
                    #with open('compare.txt', 'a') as filec:
                    filec.write(prot + "~" + "Not Available" + "~:" + "Not Available"+ '\n')








