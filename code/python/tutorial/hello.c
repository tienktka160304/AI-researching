#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_N 100
#define MAX_M 1000

typedef struct {
    int vertex;
    int cost;
} Edge;

typedef struct {
    Edge edges[MAX_M];
    int size;
} Graph;

Graph graph[MAX_N + 1];
int n, m, u, v;

void addEdge(int from, int to, int cost) {
    graph[from].edges[graph[from].size].vertex = to;
    graph[from].edges[graph[from].size].cost = cost;
    graph[from].size++;
}

typedef struct {
    int vertex;
    int cost;
} Node;

Node queue[MAX_N];
int front = 0, rear = 0;

void enqueue(int vertex, int cost) {
    queue[rear++] = (Node){vertex, cost};
}

Node dequeue() {
    return queue[front++];
}

int isEmpty() {
    return front == rear;
}

int ucs(int start, int goal, int prev[]) {
    int costs[MAX_N + 1];
    int visited[MAX_N + 1] = {0};

    for (int i = 1; i <= n; i++) {
        costs[i] = INT_MAX;
        prev[i] = -1;
    }
    costs[start] = 0;

    enqueue(start, 0);

    while (!isEmpty()) {
        Node current = dequeue();
        int node = current.vertex;

        if (visited[node]) continue;
        visited[node] = 1;

        if (node == goal) {
            return costs[node];
        }

        for (int i = 0; i < graph[node].size; i++) {
            Edge edge = graph[node].edges[i];
            if (!visited[edge.vertex] && costs[node] + edge.cost < costs[edge.vertex]) {
                costs[edge.vertex] = costs[node] + edge.cost;
                prev[edge.vertex] = node;
                enqueue(edge.vertex, costs[edge.vertex]);
            }
        }
    }
    return -1; // Không tìm thấy đường đi
}

void printPath(int goal, int prev[], FILE *output) {
    if (goal == -1) return;
    printPath(prev[goal], prev, output);
    fprintf(output, "%d", goal);
    if (prev[goal] != -1) fprintf(output, "->");
}

int main() {
    FILE *input = fopen("TK.in", "r");
    FILE *output = fopen("TK.out", "w");

    fscanf(input, "%d %d %d %d", &n, &m, &u, &v);
    for (int i = 0; i < m; i++) {
        int from, to, cost;
        fscanf(input, "%d %d %d", &from, &to, &cost);
        addEdge(from, to, cost);
    }

    int prev[MAX_N + 1];
    int cost = ucs(u, v, prev);
    if (cost == -1) {
        fprintf(output, "Khong ton tai duong di\n");
    } else {
        fprintf(output, "Duong di tu %d den %d la: ", u, v);
        printPath(v, prev, output);
        fprintf(output, "\nChi phi tren duong di la: %d\n", cost);
    }

    fclose(input);
    fclose(output);
    return 0;
}