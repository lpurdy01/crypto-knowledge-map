# Graph Visualization Methods
It would be cool to include a graph visualization of the notes on the web version.

## Some cool references
[plotly 3D network graph](https://plotly.com/python/v3/3d-network-graph/)


[plotly new network graphs page](https://plotly.com/python/network-graphs/)


It looks like [netlify](https://www.netlify.com/) has a nice way to generate webpages from
a collection of markdown files. 

It uses generators to create the webpages. [Jamstack](https://jamstack.org/generators/)

It looks like jamstack provides a bunch of services to generate webpages.

MKdocs looks like a good option, it is python based.

Mermaid is a graph visualization tool. It's flowchart might be a neat way to generate a little tree at the top
of a webpage to visualize the prerequisites.

## Mkdocs notes
Special characters are not supported in wikilinks names, and it doesn't look like it can drill down in paths.

For links to look correct in rendered markdown they need to have double enters behind them.

# Design goals

- Make a little graph visualization on each page showing some of the prerequisites, or connections between topics.
- Have the website hostable on github pages.
- Have the website easily generated from the notes
- Have a link checker that tests all links in the website
- Make a nice logo for the top right hand corner
- Figure out how to make the links work correctly
