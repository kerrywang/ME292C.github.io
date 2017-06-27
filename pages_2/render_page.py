from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
	loader=FileSystemLoader("./")
)
teams_info = [
	{"page_title":"HM Plot", "team_name":"Team DJR","team_number":"1"},
	{"page_title":"HM Plot", "team_name":"Social Squirrels","team_number":"2"},
	{"page_title":"HM Plot", "team_name":"Fire Water","team_number":"3"},
	{"page_title":"HM Plot", "team_name":"Team Four","team_number":"4"},
	{"page_title":"HM Plot", "team_name":"H2Woah","team_number":"5"},
	{"page_title":"HM Plot", "team_name":"Drive for Life","team_number":"6"},
	{"page_title":"HM Plot", "team_name":"Eat-It","team_number":"7"},
	{"page_title":"HM Plot", "team_name":"Cal Study Spots","team_number":"9"}

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