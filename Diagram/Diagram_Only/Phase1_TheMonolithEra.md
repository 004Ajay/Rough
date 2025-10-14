## Single Box (Monolith)

```mermaid
%%{init: {'flowchart': {'htmlLabels': false}}}%%
graph LR
  %% Nodes (Shapes/Conceptual Components)
  A[User]
  B(Django Monolith App)
  C((PostgreSQL DB))
  
subgraph Outside World
direction LR
  A 
end

subgraph Single Server
direction LR
  A --https request--> B
  B --Read/Write--> C
end
```

## Separating App & DB

```mermaid
%%{init: {'flowchart': {'htmlLabels': false}}}%%

graph LR
  %% Nodes (Shapes/Conceptual Components)
  A[User]
  B(Django App Server)
  C((PostgreSQL DB))

subgraph Outside World
direction LR
  A 
end

subgraph App Server
direction LR
  A --https request--> B
end

subgraph Database Server
direction LR
  B --Read/Write--> C
end
```

## The Traffic Cop (Nginx Load Balancing)

```mermaid
%%{init: {'flowchart': {'htmlLabels': false}}}%%
graph LR
%% Nodes (Shapes/Conceptual Components)
A[User]
B["Nginx Load Balancer <br> (Algorithm: Round Robin or Least Connections)"]
C(Django Monolith App 1)
D(Django Monolith App 2)
E((PostgreSQL DB))        
%% The Traffic Cop (Load Balancing)
subgraph C4: Load Balancing
direction LR
    A --https request--> B
    B ---> C 
    B ---> D
    C --Read/Write--> E
    D --Read/Write--> E
end
```