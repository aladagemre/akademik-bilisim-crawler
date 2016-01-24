import json


papers = json.loads(open("papers.json").read())
sessions = json.loads(open("sessions.json").read())

def get_paper(id_):
    if "-" in str(id_):
        id_ = id_.split("-")[0]

    for paper in papers:
        if paper['pid'] == str(id_):
            return paper

def get_cell(session):
    ids = map(lambda x: x.strip(), session['ids'])

    result = ""
    topic = session['topic'].strip()
    if topic == "S":
        topic = "Seminer"
    elif topic == "Ç":
        topic = "Çalıştay"
    elif topic == "P":
        topic = "Panel"

    result += "<h4>%s</h4>" % topic
    result += "<ul>\n"
    for id_ in ids:
        print(id_)
        id_0 = id_.split("-")[0]
        paper = get_paper(id_)
        if paper:
            title = paper['title']
            result += "<li><a href='http://ab.org.tr/ab16/ozet/%(id_0)s.html'>%(id_)s - %(title)s</a></li>\n" % {'id_0': id_0, 'id_': id_, 'title': title}
        else:
            print(id_," not found")

    result += "</ul>\n"
    return topic, result


dates = [u'3/02/16', u'04/02/16', u'05/02/16']
for date in dates:
    todays_sessions = sorted(filter(lambda x: x['date']==date, sessions), key=lambda x: x['time'])

    f = open("%s.html" % date.replace("/", "-"), "w")
    content = ""
    if date == "3/02/16":
        content += """
        <tr>
            <th>09:30-11.00</th>
            <td colspan="9">Açılış</td>
        </tr>
        """
    s = []
    prev_time = None
    for session in todays_sessions:
        current_time = session['time']
        if current_time != prev_time:
            if prev_time != None:
                content += "</tr>\n"
            content += "<tr>\n"
            content += "\t<th>%s</th>\n" % current_time
            prev_time = current_time

        topic, cell_content = get_cell(session)
        if topic in ["Panel", "Çalıştay", "Forum"]:
            tdcls = "red"
        elif topic == "Seminer":
            tdcls = "pink"
        else:
            tdcls = "white"

        content += "\t<td class='%s'>%s</td>\n" % (tdcls, cell_content)
        #print session['time'], session['salloon']
    f.write(open("template.html").read() % {'content': content})
    f.close()
