import * as d3 from 'd3';

const PieChart = ({ data }) => {
  const svgWidth = 300;
  const svgHeight = 300;
  const radius = Math.min(svgWidth, svgHeight) / 2;

  const color = d3.scaleOrdinal(['#adadad', '#f5d53f', '#636fbb', '#08e8de', '#86db4a', '#de2c2c']);

  const arc = d3.arc()
   .innerRadius(0)
   .outerRadius(radius);

  const pie = d3.pie()
   .value((d) => d.value);

  const svg = d3.select('body').append('svg')
   .attr('width', svgWidth)
   .attr('height', svgHeight)
   .append('g')
   .attr('transform', `translate(${svgWidth / 2}, ${svgHeight / 2})`);

  const g = svg.selectAll('.arc')
   .data(pie(data))
   .enter()
   .append('g')
   .attr('class', 'arc');

  g.append('path')
   .attr('d', arc)
   .style('fill', (d) => color(d.data.label));

  g.append('text')
   .attr('transform', (d) => `translate(${arc.centroid(d)})`)
   .text((d) => d.data.label);

  return null;
};

export default PieChart;