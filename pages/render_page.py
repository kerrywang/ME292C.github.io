from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
	loader=FileSystemLoader("./")
)
teams_info = [
	# {"page_title":"HM Plot", "team_name":"Freeweight Assistant","team_number":"2"},
	{"page_title":"HM Plot", "team_name":"OverView","team_number":"6"}
	# {"page_title":"HM Plot", "team_name":"IoT/Smart home","team_number":"6"},
	# {"page_title":"HM Plot", "team_name":"Mabe Food","team_number":"8"},
	# {"page_title":"HM Plot", "team_name":"Principle Power","team_number":"12"},
	# {"page_title":"HM Plot", "team_name":"Skateboard","team_number":"14"}
]
template = env.get_template("template.html")
for team_info in teams_info:
	# print template.render(team_info)
	with open("team" + team_info["team_number"] + ".html", 'wb') as html:
		html.write(template.render(team_info))