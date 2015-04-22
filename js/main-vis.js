function createVis(){

var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 700 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .rangeRound([height, 0]);

var color = d3.scale.ordinal()
    //.range(["#cb181d", "#fb6a4a", "#fcae91", "#fee5d9", "#ffffb2", "#edf8e9", "#bae4b3", "#74c476", "#238b45"]);
	.range(["#d73027","#f46d43","#fdae61","#fee08b","#ffffbf","#d9ef8b","#a6d96a","#66bd63","#1a9850"]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .tickFormat(d3.format(".2s"));

var svg = d3.select("#VisBody").append("svg")
    .attr("width", width + margin.left + margin.right+ 100)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.csv("data/data.csv", function(error, data) {

  color.domain(d3.keys(data[0]).filter(function(key) { return key !== "State"; }));

  data.forEach(function(d) {
    var y0 = 0;
    d.ages = color.domain().map(function(name) { return {name: name, y0: y0, y1: y0 += +d[name]}; });
    d.total = d.ages[d.ages.length - 1].y1;
  });


  data.sort(function(a, b) { return b.total - a.total; });

  x.domain(data.map(function(d) { return d.State; }));
  y.domain([0, d3.max(data, function(d) { return d.total; })]);

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

/*   svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end"); */

  var state = svg.selectAll(".state")
      .data(data)
    .enter().append("g")
      .attr("class", "g")
      .attr("transform", function(d) { return "translate(" + x(d.State) + ",0)"; });

  state.selectAll("rect")
      .data(function(d) { return d.ages; })
	  .enter().append("rect")
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d.y1); })
      .attr("height", function(d) { return y(d.y0) - y(d.y1); })
      .style("fill", function(d) { return color(d.name); });

  var legend = svg.selectAll(".legend")
      .data(color.domain().slice().reverse())
      .enter().append("g")
      .attr("class", "legend")
      .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

  legend.append("rect")
      .attr("x", width + 10)
      .attr("y", 20)
      .attr("width", 18)
      .attr("height", 18)
      .style("fill", color);

  legend.append("text")
      .attr("x", width + 30)
      .attr("y", 30)
      .attr("dy", ".35em")
      //.style("text-anchor", "end")
      .text(function(d) { return d; });
	  
	svg.append("text")
      .attr("class", "title")
      .attr("x", width + 7)
      .attr("y", 7)
      .attr("font-weight", "bold")
      .attr("font-size", "12px")
      .text("Sentiment");

});



// end createVis function
}


var preData =
[
{
"State": "1 Star",
"Extremely Negative": "100",
"Extremely Positive": "100",
"Negative": "100",
"Neutral": "200",
"Positive": "100",
"Slightly Negative": "100",
"Slightly Positive": "100",
"Strongly Negative": "100",
"Strongly Positive": "100"
},
{
"State": "2 Star",
"Extremely Negative": "100",
"Extremely Positive": "100",
"Negative": "100",
"Neutral": "200",
"Positive": "100",
"Slightly Negative": "100",
"Slightly Positive": "100",
"Strongly Negative": "100",
"Strongly Positive": "100"
},
{
"State": "3 Star",
"Extremely Negative": "100",
"Extremely Positive": "100",
"Negative": "100",
"Neutral": "200",
"Positive": "100",
"Slightly Negative": "100",
"Slightly Positive": "100",
"Strongly Negative": "100",
"Strongly Positive": "100"
},
{
"State": "4 Star",
"Extremely Negative": "100",
"Extremely Positive": "100",
"Negative": "100",
"Neutral": "200",
"Positive": "100",
"Slightly Negative": "100",
"Slightly Positive": "100",
"Strongly Negative": "100",
"Strongly Positive": "100"
},
{
"State": "5 Star",
"Extremely Negative": "100",
"Extremely Positive": "100",
"Negative": "100",
"Neutral": "200",
"Positive": "100",
"Slightly Negative": "100",
"Slightly Positive": "100",
"Strongly Negative": "100",
"Strongly Positive": "100"
}


]