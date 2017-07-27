from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
	loader=FileSystemLoader("./")
)
teams_info = [
	{"page_title":"Team Phoebe", "team_name":"Team Phoebe","team_number":"1"},
	{"page_title":"Team Summer", "team_name":"Team Summer","team_number":"2"},
	{"page_title":"Team Connect", "team_name":"Team Connect","team_number":"3"},
	{"page_title":"Team I4G", "team_name":"Team I4G","team_number":"4"},
	{"page_title":"Team BFF'S", "team_name":"Team BFF'S","team_number":"5"},
	{"page_title":"Team Fire Away", "team_name":"Team Fire Away","team_number":"6"},
	{"page_title":"Team Phoebe", "team_name":"Team Phoebe","team_number":"01"},
	{"page_title":"Team Summer", "team_name":"Team Summer","team_number":"02"},
	{"page_title":"Team Connect", "team_name":"Team Connect","team_number":"03"},
	{"page_title":"Team I4G", "team_name":"Team I4G","team_number":"04"},
	{"page_title":"Team BFF'S", "team_name":"Team BFF'S","team_number":"05"},
	{"page_title":"Team Fire Away", "team_name":"Team Fire Away","team_number":"06"},
	 

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