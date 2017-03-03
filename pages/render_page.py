from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
	loader=FileSystemLoader("./")
)
teams_info = [
	{"page_title":"HM Plot Demo", "team_name":"HM Plot of Autonomous Vehicle Team", "team_number":"1"}
]
template = env.get_template("template.html")
for team_info in teams_info:
	# print template.render(team_info)
	with open("team" + team_info["team_number"] + ".html", 'wb') as html:
		html.write(template.render(team_info))