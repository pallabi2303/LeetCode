class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start_node, int end_node) {
        // Adjacency list: each node has a list of Pair (neighbor, probability)
        List<List<Pair>> adj = new ArrayList<>(n);
        double[] dist = new double[n];
        // Initialize adjacency list
        for (int i = 0; i < n; i++)
            adj.add(new ArrayList<>());
        // Build the adjacency list
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0], v = edges[i][1];
            adj.get(u).add(new Pair(v, succProb[i]));
            adj.get(v).add(new Pair(u, succProb[i]));
        }
        // Priority queue to simulate max-heap: (probability, node)
        PriorityQueue<double[]> pq = new PriorityQueue<>((a, b) -> Double.compare(b[0], a[0]));
        pq.offer(new double[]{1, start_node});
        dist[start_node] = 1;
        while (!pq.isEmpty()) {
            double[] curr = pq.poll();
            double prob = curr[0];
            int node = (int) curr[1];
            if (node == end_node)
                return prob;
            for (Pair neighbor : adj.get(node)) {
                double newProb = prob * neighbor.second;
                if (newProb > dist[neighbor.first]) {
                    dist[neighbor.first] = newProb;
                    pq.offer(new double[]{newProb, neighbor.first});
                }
            }
        }
        return 0;
    }
}
class Pair {
    public int first;
    public double second;
    Pair (int first, double second){
        this.first = first;
        this.second = second;
    }
}