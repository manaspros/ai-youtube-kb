# STOP Using Docker Compose. Switch to Kubernetes in 6 Mins (With Kompose)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `cyGF_PLBx4c` · [watch](https://youtu.be/cyGF_PLBx4c) · **date:** 2025-11-02 · **length:** 6:24 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools, infra-cost-scaling · **tags:** kubernetes, docker-compose, kompose, kind, local-cluster, nodeport, imagepullpolicy, tutorial

> Tutorial that converts a two-container Docker Compose app to Kubernetes manifests with Kompose, runs it on a local kind cluster, and fixes two first-deploy failures (image pull policy and ClusterIP).

## Summary
The speaker argues that a Compose app running on several servers should move to an orchestrator such as Kubernetes, and claims the conversion is quick. He converts a two-container Compose project (nginx in front of a Bun app) into Kubernetes manifests with Kompose, which writes Deployment, ConfigMap and Service files into a K8s folder. He then creates a local kind cluster from a config file that maps ports, loads the locally built Bun image into it, and applies the manifests with kubectl. The first apply shows two failures: an ImagePullBackOff on the :latest-tagged image and no reachable port. He fixes the pull policy, switches the nginx Service to NodePort 30000, and reaches the app at localhost:30000. Ingress, production clusters and multi-node setups are not covered. Sponsored plugs for Better Stack's newsletter and observability product take up two of the six minutes.

## Key ideas
- **Compose files are for one host; a multi-server deployment needs an orchestrator such as Swarm, Nomad or Kubernetes** — The speaker argues against running Compose in production across several servers. He claims a two-container app can be converted to Kubernetes in under 10 minutes with a converter, rather than a rewrite. ([0:00](https://youtu.be/cyGF_PLBx4c?t=0))
- **A Kompose-style converter emits a folder of Kubernetes manifests from the Compose file** — The output includes a Deployment, a ConfigMap and Services in a K8s folder. The Compose annotations only track the resources the tool created; the speaker keeps them, and says they can be removed without breaking anything (not tested in the video). ([1:26](https://youtu.be/cyGF_PLBx4c?t=86))
- **kind nodes are Docker containers, so a local image has to be loaded into the cluster before pods can use it** — The kind cluster is created from a config file that exposes ports. Public images such as nginx pull fine, but the locally built Bun image is not visible to the cluster until it is added with a separate command. ([2:40](https://youtu.be/cyGF_PLBx4c?t=160))
- **The first apply fails with ImagePullBackOff because :latest-tagged images get a different default pull policy** — Kubernetes tries the registry for the :latest image instead of the copy on the node. The speaker inspects the node's images with docker exec to confirm the Bun image is there, then sets an imagePullPolicy on the Deployment so the node's copy is used. ([3:54](https://youtu.be/cyGF_PLBx4c?t=234))
- **A ClusterIP Service is not reachable from the host; NodePort plus a port that matches the kind port mapping makes the app reachable** — The nginx Service is changed to type NodePort with nodePort 30000, matching the kind config. After applying, localhost:30000 serves the app, which is the only externally reachable path in the demo. ([5:20](https://youtu.be/cyGF_PLBx4c?t=320))
- **Ingress and production use are explicitly left out of scope** — The closing lines raise ingress and running in production as follow-up questions. The video does not cover ingress, persistent storage, secrets or multi-node scheduling. ([5:20](https://youtu.be/cyGF_PLBx4c?t=320))

## Techniques
- **Convert Compose to Kubernetes manifests with Kompose** — Run the converter from the project directory. It writes Kubernetes manifests into a K8s folder (Deployment, ConfigMap, Service). The exact command and flags are not spelled out in the transcript. Leave the Compose annotations in or delete them; the speaker says they only track resources. *When:* First pass when moving a single-host Compose app to Kubernetes. Expect to hand-edit the output.
- **Create a local kind cluster with exposed ports** — Create the cluster from a kind config file that maps host ports into the cluster. The speaker links the file in the description; its contents are not shown. Minikube or Docker Desktop's Kubernetes can be used instead. *When:* Testing manifests on a laptop before a real cluster.
- **Load a locally built image into kind** — Public images pull normally, but a locally built image has to be loaded into the kind cluster with a separate command (not spelled out in the transcript) before pods can start with it. *When:* Any local image that is not in a registry the cluster can reach.
- **Inspect a kind node's images with docker exec** — Because each kind node is a Docker container, run docker exec into the node container to list the images it holds. Confirm the local image is present and check its tag. *When:* Debugging ImagePullBackOff on a local cluster.
- **Fix pulls of :latest-tagged local images by setting imagePullPolicy** — Add an imagePullPolicy to the container spec in the Deployment manifest so the node's copy is used instead of the registry. The policy value is not named in the transcript. Re-apply the file with kubectl apply. *When:* A locally loaded image is tagged latest and pods stay in ImagePullBackOff.
- **Expose a Service on a fixed host port with NodePort** — Change the Service type from ClusterIP to NodePort and set nodePort to the port that the kind config maps (30000 in the video). Apply the manifest, then open localhost on that port. *When:* Reaching an in-cluster service from the host during local testing.
- **Check cluster state with kubectl get all** — After applying the manifest files with kubectl, run kubectl get all to see pods, services, deployments and replica sets. Look for pods that are not Running and for Services without a reachable port. *When:* Verifying a deploy and finding why pods or ports are not working.

## Numbers
- Claims a Compose-to-Kubernetes conversion takes under 10 minutes for a two-container app ([0:00](https://youtu.be/cyGF_PLBx4c?t=0))
- The converter run that produces the manifests takes a few seconds on screen ('Wow, that was quick') ([1:26](https://youtu.be/cyGF_PLBx4c?t=86))
- kubectl get all shows 2 pods, 3 services, several deployments and replica sets on the first apply, with 1 pod stuck in ImagePullBackOff ([2:40](https://youtu.be/cyGF_PLBx4c?t=160))
- Final access port is NodePort 30000, matching the kind port mapping ([5:20](https://youtu.be/cyGF_PLBx4c?t=320))
- Video length is 6:24 ([0:00](https://youtu.be/cyGF_PLBx4c?t=0))

## Hot takes
- The title ('STOP Using Docker Compose') and the opening claim overreach: the demo is a single laptop kind cluster, and the video never shows multi-node scheduling, ingress, storage or secrets, which the closing lines defer.
- Sponsored plugs at 1:26 (the speaker's free newsletter) and 5:20 (Better Stack observability, 'costs nothing to get started') take a large share of a 6-minute video. Quality is capped at 2 for this reason.
- The 'under 10 minutes' claim holds only because the converter output is used unmodified and cluster creation is fast-forwarded. The speaker says the Compose annotations can be removed and 'everything should work just fine' but does not test it.
- The 'Compose' the speaker says is the Kompose converter, and the transcript never names Kompose; the tool name here comes from the speaker's phrasing and common usage.

## Tools mentioned
Docker Compose, Kompose (auto-caption reads it as 'Compose'), kubectl, kind, Kubernetes, Docker, nginx, Bun, Minikube, Docker Desktop, Homebrew, Docker Swarm, Nomad

## Relevance to our work
- **agentos** (1/3): AgentOS runs several services (Rust proxy, Postgres, Redis, Neo4j, Prometheus) on one RTX 5090 host. The video shows the Compose-to-Kubernetes first pass for a multi-service stack, but only covers two containers, local kind and NodePort, with no volumes, env handling or ingress. → *If AgentOS ever needs more than one host, run kompose convert on a copy of its compose file in a throwaway kind cluster to see what resources it generates, then check volumes and env by hand.*
