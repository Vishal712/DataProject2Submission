var svgWidth = 1410;
var svgHeight = 700;

var margin = {
  top: 20,
  right: 40,
  bottom: 80,
  left: 500
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart
var svg = d3
  .select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

// Append an SVG group
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`)

// Initial params
var chosenXAxis = "Height";
var chosenYAxis = "PPG";

// Function used for updating x-scale var upon click on axis label
function xScale(nbaData, chosenXAxis) {
  // Create scales
  var xLinearScale = d3.scaleLinear()
      .domain([d3.min(nbaData, d => d[chosenXAxis]) * .99, d3.max(nbaData, d => d[chosenXAxis]) * 1.01])
      .range([0, width])
  return xLinearScale
}

// Function used for updating y-scale var upon click on axis label
function yScale(nbaData, chosenYAxis) {
  // Create scales
  var yLinearScale = d3.scaleLinear()
      .domain([-.4, d3.max(nbaData, d => d[chosenYAxis]) * 1.05])
      .range([height, 0])
  return yLinearScale
}

// Function used for updating xAxis var upon click on axis label
function renderXAxes(newXScale, xAxis) {
  var bottomAxis = d3.axisBottom(newXScale);

  xAxis.transition()
    .duration(1000)
    .call(bottomAxis.ticks(20));

  return xAxis;
}

// Function used for updating yAxis var upon click on axis label
function renderYAxes(newYScale, yAxis) {
  var leftAxis = d3.axisLeft(newYScale);

  yAxis.transition()
    .duration(1000)
    .call(leftAxis);

  return yAxis;
}

// function used for updating circles group with a transition 
function renderCircles(circlesGroup, newXScale, newYScale, chosenXAxis, chosenYAxis) {

  circlesGroup.transition()
    .duration(1000)
    .attr("cx", d => newXScale(d[chosenXAxis]))
    .attr("cy", d => newYScale(d[chosenYAxis]));

  return circlesGroup;
}

function renderLabels(circleLabels, newXScale, newYScale, chosenXAxis, chosenYAxis) {

circleLabels.transition()
  .duration(1000)
  .attr("x", d => newXScale(d[chosenXAxis]))
  .attr("y", d => newYScale(d[chosenYAxis]));

return circleLabels;
}

// function used for updating circles group with new tooltip
function updateToolTip(chosenXAxis, chosenYAxis, circlesGroup, circleLabels) {

  var labelx;

  if (chosenXAxis === "Height") {
    labelx = "Height:";
  }
  else {
    labelx = "Weight";
  }
  
  var labely;

  if (chosenYAxis === "PPG") {
    labely = "PPG:";
  }
  else if (chosenYAxis === "APG") {
    labely = "APG:";
  }
  else if (chosenYAxis === "RPG") {
    labely = "RPG:";
  }
  else {
    labely = "TPG:";
  }

  var toolTip = d3.tip()
    .offset([80, -60])
    .attr("class", "d3-tip")
    .html(function(d) {
      return (`<a href= "/data/${d.Name}" target="_blank">${d.Name} </a><br/> ${labelx} ${d[chosenXAxis]}<br> ${labely} ${d[chosenYAxis]})`)
    });

  circlesGroup.call(toolTip);

  circlesGroup.on("mouseover", function(data) {
    toolTip.show(data);
  })
    // onmouseout event
    .on("dblclick", function(data, index) {
      toolTip.hide(data);
    });
  circleLabels.call(toolTip);

  circleLabels.on("dblclick", function(data) {
    toolTip.show(data);
  })
    // onmouseout event
    .on("dblclick", function(data, index) {
      toolTip.hide(data);
    });

  return circlesGroup;
}

// Retrieve data from the CSV file and execute everything below
d3.json("/NBAData", function(nbaData) {
  

  // Parse data
  nbaData.forEach(function(data){
      data.Height = +data.Height
      data.Weight = +data.Weight
      data.PPG = +data.PPG
      data.APG = +data.APG
      data.RPG = +data.RPG
      data.TPG = +data.TPG
  });
  // xLinearScale function above csv import
  var xLinearScale = xScale(nbaData, chosenXAxis)

  // Create y scale function
  var yLinearScale = yScale(nbaData, chosenYAxis)

  // Create initial axis functions
  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);

  // append x axis
  var xAxis = chartGroup.append("g")
  .classed("x-axis", true)
  .attr("transform", `translate(0, ${height})`)
  .attr("class", "axisWhite")
  .call(bottomAxis.ticks(20));

  // append y axis
  var yAxis = chartGroup.append("g")
  .attr("class", "axisWhite")
  .call(leftAxis);
  
  // append initial circles
  var circlesGroup = chartGroup.selectAll("circle").data(nbaData)
  var circlesElement = circlesGroup.enter()
  var circles = circlesElement
  .append("circle")
  .attr("cx", d => xLinearScale(d[chosenXAxis]))
  .attr("cy", d => yLinearScale(d[chosenYAxis]))
  .attr("r", 8)
  .classed("basketballCircle", true )

  // Create circle labels (used the help of stack overflow to figure out syntax to adding labels to circles)
  var circleLabels = circlesElement
  .append("text")
  .attr("x", d => {return xLinearScale(d.Height)})
  .attr("y", d => {return yLinearScale(d.PPG)})
  .attr("dy", ".35em")
  .text(d => {return d.Name})
  .classed("basketballText", true)

  // Create group for two x-axis labels
  var labelsXGroup = chartGroup.append("g")
  .attr("transform", `translate(${width / 2}, ${height + 20})`);

  var heightLabel = labelsXGroup.append("text")
    .attr("x", 0)
    .attr("y", 20)
    .attr("value", "Height") 
    .classed("active", true)
    .text("Height");

  var weightLabel = labelsXGroup.append("text")
    .attr("x", 0)
    .attr("y", 40)
    .attr("value", "Weight") 
    .classed("inactive", true)
    .text("Weight");
  // Create group for two y-axis labels
  var labelsYGroup = chartGroup.append("g")
  .attr("transform", "rotate(-90)")

  var ppgLabel = labelsYGroup.append("text")
    .attr("y", 450 - margin.left)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .attr("value", "PPG") 
    .classed("active", true)
    .text("PPG");

  var apgLabel = labelsYGroup.append("text")
    .attr("y", 430 - margin.left)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .attr("value", "APG") 
    .classed("inactive", true)
    .text("APG");

  var rpgLabel = labelsYGroup.append("text")
    .attr("y", 410 - margin.left)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .attr("value", "RPG") 
    .classed("inactive", true)
    .text("RPG");

  var tpgLabel = labelsYGroup.append("text")
    .attr("y", 390 - margin.left)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .attr("value", "TPG") 
    .classed("inactive", true)
    .text("TPG");

  // UpdateToolTip function above csv import
  var circlesGroup = updateToolTip(chosenXAxis, chosenYAxis, circles, circleLabels);

  // X axis labels event listener
  labelsXGroup.selectAll("text")
  .on("click", function(){
      // Select value
      var value = d3.select(this).attr("value")
          // Replace chosenXAxis value
          chosenXAxis = value
          // Update xscale with new data
          xLinearScale = xScale(nbaData, chosenXAxis);
          // Adds transition
          xAxis = renderXAxes(xLinearScale, xAxis);
          // updates circles with new x values
          circles = renderCircles(circlesGroup, xLinearScale, yLinearScale, chosenXAxis, chosenYAxis);
          // updates labels with new values
          circleLabels = renderLabels(circleLabels, xLinearScale, yLinearScale, chosenXAxis, chosenYAxis)
          // updates tooltips with new info
          circlesGroup = updateToolTip(chosenXAxis, chosenYAxis, circles, circleLabels);
          if (chosenXAxis === "Height"){
              heightLabel
              .classed("active", true)
              .classed("inactive", false);
              weightLabel
              .classed("active", false)
              .classed("inactive", true);
          }
          else {
              heightLabel
                .classed("active", false)
                .classed("inactive", true);
              weightLabel
                .classed("active", true)
                .classed("inactive", false);
          }
  });
  // Y axis labels event listener
  labelsYGroup.selectAll("text")
  .on("click", function(){
      // Select value
      var value = d3.select(this).attr("value")
          // Replace chosenXAxis value
          chosenYAxis = value
          // Update xscale with new data
          yLinearScale = yScale(nbaData, chosenYAxis);
          // Adds transition
          yAxis = renderYAxes(yLinearScale, yAxis);
          // updates circles with new x values
          circles = renderCircles(circlesGroup, xLinearScale, yLinearScale, chosenXAxis, chosenYAxis);
          // updates labels with new values
          circleLabels = renderLabels(circleLabels, xLinearScale, yLinearScale, chosenXAxis, chosenYAxis)
          // updates tooltips with new info
          circlesGroup = updateToolTip(chosenXAxis, chosenYAxis, circles, circleLabels);
          if (chosenYAxis === "PPG"){
              ppgLabel
              .classed("active", true)
              .classed("inactive", false);
              apgLabel
              .classed("active", false)
              .classed("inactive", true);
              rpgLabel
              .classed("active", false)
              .classed("inactive", true);
              tpgLabel
              .classed("active", false)
              .classed("inactive", true);
          }
          else if (chosenYAxis === "APG"){
              ppgLabel
              .classed("active", false)
              .classed("inactive", true);
              apgLabel
              .classed("active", true)
              .classed("inactive", false);
              rpgLabel
              .classed("active", false)
              .classed("inactive", true);
              tpgLabel
              .classed("active", false)
              .classed("inactive", true);
          }
          else if (chosenYAxis === "RPG"){
              ppgLabel
              .classed("active", false)
              .classed("inactive", true);
              apgLabel
              .classed("active", false)
              .classed("inactive", true);
              rpgLabel
              .classed("active", true)
              .classed("inactive", false);
              tpgLabel
              .classed("active", false)
              .classed("inactive", true);
          }
          else {
              ppgLabel
              .classed("active", false)
              .classed("inactive", true);
              apgLabel
              .classed("active", false)
              .classed("inactive", true);
              rpgLabel
              .classed("active", false)
              .classed("inactive", true);
              tpgLabel
              .classed("active", true)
              .classed("inactive", false);  
          }
  });
})