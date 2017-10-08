page_render = function(num, type){

    d3.select(".chart").selectAll("svg").remove();
    d3.selectAll("tooltip").remove();
	// 	mapping_file = mapping_file,
	// 	graph_file = graph_file;
    console.log(type)
	var concept_file = "../static/data/Team" + num.toString()
	var	mapping_file = "../static/graph_data/Mapping_Team" + num.toString()
	var	graph_file = "../static/graph_data/Team" + num.toString()

	if (type == "Equal") {
		concept_file += "_Equal.csv";
		mapping_file += "_Equal.csv";
		graph_file += "_Equal.csv";
	} else if (type == "Half") {
		concept_file += "_Half.csv";
		mapping_file += "_Half.csv";
		graph_file += "_Half.csv";
	} else if (type == "Double") {
		concept_file += "_Double.csv";
		mapping_file += "_Double.csv";
		graph_file += "_Double.csv";
	}
//	console.log(mapping_file)

	var margin = {top: 20, right:20, bottom: 80, left: 100},
		width = 500 - margin.left - margin.right,
		height = 500 - margin.top - margin.bottom;

	// setup x
	var xValue = function(d) {
//			 console.log(d.Human_Label_Index);
			return d.Human_Label_Index;
		},
		xScale = d3.scale.linear().range([0,width]),
		xMap = function(d) {
//			 console.log("xValue:"+xValue(d));
//			 console.log("xScale:"+xScale(xValue(d)));
			return xScale(xValue(d));
		}
		xAxis = d3.svg.axis().scale(xScale).orient("bottom");

	// setup y
	var yValue = function(d) {return d.Machine_Label_Index;},
		yScale = d3.scale.linear().range([height, 0]),
		yMap = function(d) {
//			 console.log("yValue:"+yValue(d));
			return yScale(yValue(d));
		}
		yAxis = d3.svg.axis().scale(yScale).orient("left");

	// add the graph canvas to the body of the webpage
	var svg = d3.select(".chart").append("svg")
		.attr("width", width + margin.left + margin.right)
		.attr("height", height + margin.top + margin.bottom)
	  .append("g")
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	// add the tooltip area to the webpage
	var tooltip = d3.select("body").append("div")
		.attr("class", "tooltip")
		.style("opacity", 0);

	d3.csv(mapping_file,function(error, data){
	    console.log(data)
        var Human_Length = 0;
        var Machine_Length = 0;
		data.forEach(function(d){
		    if (d.Machine_Index != "") Machine_Length += 1;
		    if (d.Human_Index != "") Human_Length += 1;
			d.Index =+ d.Index;
			console.log(Machine_Length)
			console.log(Human_Length)
            console.log(">>>>>>>>>>>>>>>>>>>>>>")

		});
		// x-axis
		xScale.domain([0,Human_Length - 1]); // changed from data.length - 1
		xAxis.ticks(Human_Length).tickFormat(function(d,i){ // changed from data.length
				console.log(data[d].Human_Index);

				if (data[d].Human_Index != "") {
				    return data[d].Human_Label;
				}
			});

		svg.append("g")
			.attr("class", "x axis")
			.attr("transform", "translate(0," + height + ")")
			.call(xAxis)
		   .selectAll("text")
			.attr("y", 20)
			.attr("x", 0)
			.attr("dy", ".35em")
			.attr("transform", "rotate(-20)")
			.style("font-size",10)
			.style("text-anchor", "end")

		svg.selectAll('.x.axis')
		   .append("text")
			.attr("class", "label")
			.attr("x",width)
			.attr("y", -6)
			.style("text-anchor", "end")
			.text("Human Cluster")

		svg.selectAll('.x.axis .tick')
			.on("click",function(d){
				d3.csv(concept_file,function(csv){
					csv = csv.filter(function(row){
						return row["Human Label"] == data[d].Human_Label;
					});
//					console.log(csv);
					tabulate(csv);
				});
			})

		// y-axis
		yScale.domain([0,Machine_Length - 1]);
		yAxis.ticks(Machine_Length).tickFormat(function(d,i){
//		    console.log(data[d].Machine_Label)
		    if (data[d] && data[d].Machine_Index != "") {
		        console.log(data[d]);
			    return data[d].Machine_Label;
			}
		})

		svg.append("g")
			.attr("class", "y axis")
			.call(yAxis)
		   .selectAll("text")
			.style("font-size",10)

		svg.selectAll(".y.axis")
		   .append("text")
			.attr("class", "label")
			.attr("transform", "rotate(-90)")
			.attr("y", 6)
			.attr("dy", ".71em")
			.style("text-anchor", "end")
			.text("Machine Cluster");

		svg.selectAll(".y.axis .tick")
			.on("click", function(d){
				d3.csv(concept_file,function(csv){
					csv = csv.filter(function(row){
						return row["Machine Label"] == data[d].Machine_Label;
					});
//					 console.log(csv);
					tabulate(csv);
				})
			});


		d3.csv(graph_file,function(error, data){
			// change string (from CSV) into proper format
			data.forEach(function(d){
				d.Bubble_size = +d.Bubble_size
				d.Concept_Indices = JSON.parse(d.Concept_Indices.replace(/;/g,","))
				d.Human_Label_Index = +d.Human_Label_Index
				d.Machine_Label_Index = +d.Machine_Label_Index
//				 console.log(d)
			});

			svg.selectAll(".dot")
				.data(data)
				.enter().append("circle")
				.attr("class", "dot")
				.attr("r",function(d){
					return d.Bubble_size*3;
				})
				.attr("cx", xMap)
				.attr("cy", yMap)
				.style("fill","#d8452f")
				.style("opacity",.9)
				.on("click", function(d){
//					 console.log(d);
//					 console.log(d.Human_Label + ":" + d.Machine_Label)
					d3.csv(concept_file,function(csv){
//						console.log(csv);
						csv = csv.filter(function(row){
							return row["Human Label"] == d.Human_Label && row["Machine Label"] == d.Machine_Label;;
						});
//						 console.log(csv);
						tabulate(csv);
					});
				})
				.on("mouseover",function(d){
//					 console.log(d);
					tooltip.transition()
						.duration(200)
						.style("opacity", .9)
						.style("left", (d3.event.pageX + 5) + "px")
						.style("top", (d3.event.pageY - 28) + "px");
//					tooltip.html(d.Concept_Indices);
				})

		});

	});



	d3.csv(concept_file,function(data){
		tabulate(data);

	});

	tabulate = function(data){
//	    console.log(data[0])
		d3.select("#table > *").remove()
		var table = d3.select("#table").append('table')
		var thead = table.append('thead')
		var tbody = table.append('tbody')

		columns = Object.keys(data[0])
//		 console.log(columns)

		//header row
		thead.append('tr')
			.selectAll('th')
			.data(columns).enter()
			.append('th')
				.text(function(column) { return column;})

		// row for each object
		var rows = tbody.selectAll('tr')
			.data(data).enter()
			.append('tr');

		//cell in each row
		var cells = rows.selectAll('td')
			.data(function (row) {
				return columns.map(function (column){
					return {column: column, value: row[column]};
				});
			})
			.enter()
			.append('td')
				.text(function(d) {return d.value});


		return table;
//		console.log("Generated a table");
	}
//	        d3.selectAll("svg").remove();
}