from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
	loader=FileSystemLoader("./")
)
teams_info = [
	# {"page_title":"HM Plot", "team_name":"3D_Printing_Material","team_number":"1"},
	# {"page_title":"HM Plot", "team_name":"Autonomous_Veichles","team_number":"2"},
	# {"page_title":"HM Plot", "team_name":"Composite_Manfg","team_number":"3"},
	# {"page_title":"HM Plot", "team_name":"Eco-Solar","team_number":"4"},
	# {"page_title":"HM Plot", "team_name":"Energy&Connected_Cars","team_number":"5"},
	# {"page_title": "HM Plot", "team_name": "IOT_and_Robotices_1", "team_number": "6"},
	# {"page_title": "HM Plot", "team_name": "IOT_and_Robotices_2", "team_number": "7"},
	# {"page_title": "HM Plot", "team_name": "Mars_Suit", "team_number": "8"},
	# {"page_title": "HM Plot", "team_name": "MEMS_Sensors", "team_number": "9"},
	# {"page_title": "HM Plot", "team_name": "Million_Hands", "team_number": "10"},
	# {"page_title": "HM Plot", "team_name": "Morphing", "team_number": "11"},
	# {"page_title": "HM Plot", "team_name": "Pediatric_Exoskeleton", "team_number": "12"},
	# {"page_title": "HM Plot", "team_name": "Rotationg_Machinery", "team_number": "13"},
	# {"page_title": "HM Plot", "team_name": "Renault", "team_number": "14"},
	{"page_title": "HM Plot", "team_name": "Mars_suit_second_submission", "team_number": "22"},

	# {"page_title":"HM Plot", "team_name":"Scoliosis_Treatment","team_number":"15"},
	# {"page_title":"HM Plot", "team_name":"Smart_Exercise","team_number":"16"},
	# {"page_title":"HM Plot", "team_name":"Solar_Farm","team_number":"17"},
	# {"page_title":"HM Plot", "team_name":"Tensegrity_Robots","team_number":"18"},
	# {"page_title":"HM Plot", "team_name":"Virtual_Reality","team_number":"19"},
	# {"page_title": "HM Plot", "team_name": "Wind_Power", "team_number": "20"},

]
template = env.get_template("template.html")
for team_info in teams_info:
	# print template.render(team_info)
	# with open("team" + team_info["team_number"] + ".html", 'wb') as html:
	# 	html.write(template.render(team_info))
	with open(team_info["team_name"] + ".html", 'wb') as html:
		html.write(template.render(team_info))