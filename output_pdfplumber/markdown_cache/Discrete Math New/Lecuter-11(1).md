# Extracted Content: Lecuter-11(1).pdf

### Example (Page 4)
**Category**: Solution

> Introduction
> o Informally, a graph is a diagram consisting of points, called vertices, joined
> together by lines, called edges; each edge joins exactly two vertices.
> o A graph G is a triple consisting of a vertex set of V(G), an edge set E(G).
> Example:
> • V:={1, 2, 3, 4, 5, 6, 7}
> • E:={{1,2}, {2,4}, {2,3}, {4,5}, {4,6}, {6,7}} 340

---

### Example (Page 6)
**Category**: Solution

> Undirected and Directed Graphs
> o Undirected graph: The edges of a graph are assumed to be unordered
> pairs of nodes. Sometimes we say undirected graph to emphasize this point.
> In an undirected graph, we write edges using curly braces to denote
> unordered pairs. For example, an undirected edge {2,3} from vertex 2 to
> vertex 3 is the same thing as an undirected edge {3,2} from vertex 3 to
> vertex 2.
> o Directed graph: In a directed graph, the two directions are counted as
> being distinct directed edges. In an directed graph, we write edges using
> parentheses to denote ordered pairs. For example, edge (2,3) is directed
> from 2 to 3 , which is different than the directed edge (3,2) from 3 to 2.
> Directed graphs are drawn with arrowheads on the links, as shown below:
> 342

---

### Example (Page 8)
**Category**: Solution

> Neighborhood and Degree
> o Two vertices are called adjacent if they share a common edge, in which case the
> common edge is said to join the two vertices. An edge and a vertex on that edge are
> called incident.
> o See the 6-node graph Fig 1.4 for examples of adjacent and incident:
> • Nodes 4 and 6 are adjacent (as well as many other pairs of nodes)
> • Nodes 1 and 3 are not adjacent (as well as many other pairs of nodes)
> • Edge {2,5} is incident to node 2 and node 5.
> o The neighborhood of a vertex v in a graph G is the set of vertices adjacent to v. The
> neighborhood is denoted N(v). The neighborhood does not include v itself. For
> example, in the graph below N(5) = {4,2,1} and N(6) = {4}.
> o The degree of a vertex is the total number of vertices adjacent to the vertex. The
> degree of a vertex v is denoted deg(v). We can equivalently define the degree of a
> vertex as the cardinality of its neighborhood and say that for any vertex v, deg(v)
> = |N(v)|.
> Fig 1.4
> 344

---

### Theorem (Page 9)
**Category**: Law

> Degree of a Vertex
> Theorem: The sum of the degrees of the vertices of a graph G is equal to twice
> the number of edges in G, i.e.
> Illustration: Consider the graph in Fig 1.4. The sum of degrees equals 14 which, as
> expected, is twice the number of edges.
> Example: How many edges are there in a graph with 10 vertices each of degree 6?
> Solution: It follows that 2e = 60. Therefore, e = 30.
> o A vertex is said to be even or odd according as its degree is an even or an odd
> number. Thus 1 and 3 are even whereas 2, 4, 5 and 6 are odd vertices in Fig 1.4.
> o The Theorem also holds for multigraphs where a loop is counted twice toward
> the degree of its endpoint. For example, in the below graph we have deg (V) = ?
> Why.
> 345
> o A vertex of degree zero is called an isolated vertex.
> 2 e  v
>  V
> d e g ( v )
> v

---

### Example (Page 14)
**Category**: Solution

> Isomorphic Graphs
> Example: (a) Show that the graphs G(U, E) and H(V, F) are isomorphic in Fig 2.17.
> (b) show that the graphs displayed in Fig 2.18 are not isomorphic.
> v1 v2
> u1 u2
> v4
> u4 v3
> u3 H
> G
> Figure 2.17
> b
> b
> c
> a c a
> Fig. 2.18 350
> e d
> e d
> H
> G

---

### Solution (Page 15)
**Category**: Solution

> Isomorphic Graphs

---

