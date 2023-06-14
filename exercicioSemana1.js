const readline = require('readline');

// considerando grafo sem setinha, (n da pra um aresta apontar pra ela msm)

//exemplo matriz 2x2        
/*
	[ 	1   2
		1	[0, 1],
		2	[1, 0] -> tem q ser simétrica
	]
*/

// exemplo matriz 3x3

/*
	[
		[2, 1, 1],
		[3, 4, 2],
		[5, 6, 4]
	]
*/

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function prompt(question) {
  return new Promise((resolve) => {
    rl.question(question, (answer) => {
      resolve(answer);
    });
  });
}

const initializeGraph = (numVertices) => {
  if (numVertices > 20) {
    console.log("O número de vértices deve ser até 20");
    return;
  }

  let graph = [];

  for (let i = 0; i < numVertices; i++) {
    graph[i] = [];
    for (let j = 0; j < numVertices; j++) {
      graph[i][j] = 0; // preenchendo a matriz toda com 0 inicialmente
    }
  }

  return graph;
};

async function initializeValues(graph) {
  for (let i = 0; i < graph.length; i++) {
    for (let j = i + 1; j < graph.length; j++) {
      const value = await prompt(
        `Digite o peso da aresta entre o vertice ${i} e o vertice ${j}: `
      );
      graph[i][j] = parseInt(value);
			graph[j][i] = parseInt(value);
    }
  }
  rl.close();
}

const main = async () => {
  const graph = initializeGraph(2); // retornar um grafo com n vertices (até 20)

  await initializeValues(graph);

  console.log(graph);
};

main();
