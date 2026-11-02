# K9s | The BEST Terminal UI for Kubernetes (2025)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `AMUQzyPvO04` · [watch](https://youtu.be/AMUQzyPvO04) · **date:** 2025-11-02 · **length:** 4:45 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed Better Stack host · **orgs:** Better Stack
- **topics:** dev-tools, infra-cost-scaling · **tags:** k9s, kubernetes, kubectl, terminal-ui, port-forwarding, cluster-management, skins, aliases, image-scanning

> A 5-minute walkthrough of K9s, a terminal UI for Kubernetes, covering navigation, per-resource shortcuts, port-forwarding, live edits, aliases and skins. The speaker keeps kubectl for applying manifests.

## Summary
The Better Stack host argues that K9s, a terminal UI for Kubernetes, is a faster alternative to kubectl for everyday cluster management. The video walks through the main UI: a resource table, breadcrumbs, a context-sensitive shortcut bar, command mode with autocomplete, and filtering. It then covers per-resource actions such as viewing logs, opening a shell in a container, port-forwarding with Shift+F, editing YAML, changing a deployment's image, and scaling replicas, all applied live. Customization is covered too: custom aliases, config options (mouse mode, logoless and no-icons modes), and skins such as a Tokyo Night variant and Dracula. The image-scan vulnerability feature is shown as a preview that is off by default. The speaker concludes that kubectl is still needed for applying directories of manifest files. The content is a short, practical tool walkthrough with no sponsor segment.

## Key ideas
- **K9s is pitched as a faster replacement for kubectl for day-to-day cluster work, for example port-forwarding with one key combo instead of a multi-command sequence.** — The host opens with the claim that K9s replaces kubectl for managing clusters and presents the video as a quick tour of the main features. ([0:00](https://youtu.be/AMUQzyPvO04?t=0))
- **Navigation is keyboard-driven: colon opens command mode with autocomplete, slash filters the current view, and namespace and context can be switched in the UI.** — Typing deploy after colon autocompletes to deployments. Filtering uses slash, and the at symbol switches context. ([0:00](https://youtu.be/AMUQzyPvO04?t=0))
- **Resource stats such as CPU and memory need the Kubernetes metrics server; without it the views show no usage numbers.** — The speaker's first cluster had no metrics server, so the stats were blank. After adding one, resource stats appear. ([1:24](https://youtu.be/AMUQzyPvO04?t=84))
- **The shortcut bar is context-sensitive: K9s adds namespace shortcuts for the namespaces you visit, and per-resource keys change with the resource type.** — Visiting a new namespace adds it to the quick-switch list. The question-mark key lists the shortcuts for the current view. ([1:24](https://youtu.be/AMUQzyPvO04?t=84))
- **Pods and containers can be handled directly from the table: logs, a container shell, port-forwarding, YAML view and edit, and describe.** — The speaker shows L for logs, F for full screen, S for a container shell (used to open the MongoDB shell), Shift+F for port-forwarding, Y for YAML, E for editing YAML, and D for describe. ([1:24](https://youtu.be/AMUQzyPvO04?t=84))
- **Deployments can be changed in place: I updates the container image and S scales replicas, and both take effect immediately in the live view.** — The speaker changes the image to 8.0.5 and confirms it with describe. He then scales replicas, and the change shows up in real time. ([2:48](https://youtu.be/AMUQzyPvO04?t=168))
- **Aliases and config are customizable: custom command aliases live in a file in K9s's config directory, and the config file controls mouse mode, logoless and no-icons modes, and the skin.** — Ctrl+A lists the built-in aliases such as CRB for cluster role bindings. The speaker's custom aliases file already contains entries. ([2:48](https://youtu.be/AMUQzyPvO04?t=168))
- **Skins are swapped through config and need a restart. The speaker's customized Tokyo Night skin is linked in the video description, and Dracula comes from the official K9s skins repo.** — The config change is applied after restarting K9s. ([3:42](https://youtu.be/AMUQzyPvO04?t=222))
- **Image scanning is an opt-in preview that shows a vulnerability score per resource. The speaker still needs kubectl for applying manifest directories.** — The score is shown as a 5-position vector. V opens the vulnerabilities, and Enter opens one in the browser. The feature is off by default and loads slowly. The speaker advises keeping kubectl installed. ([3:42](https://youtu.be/AMUQzyPvO04?t=222))

## Techniques
- **Port-forward a pod from K9s** — Select the pod in the pods view, press Shift+F, and confirm with OK. An F marker then shows the forward is active. To stop it, open the port-forwards view (the F key, per the speaker), press Ctrl+D on the forward, and confirm OK. *When:* Quick local access to a pod's port (the speaker uses it to reach a MongoDB pod) without typing kubectl port-forward commands.
- **Edit a deployment's image or replica count live** — In the deployments view, press I to change the container image (the speaker sets 8.0.5, which applies immediately) and press S to change the replica count. Check the result with D (describe). *When:* Fast iteration in a dev or staging cluster, or a quick rollback during an incident. These are live cluster changes.
- **Open a shell in a container** — Drill from the pod to its containers level in the breadcrumbs, then press S to open a shell in the container. The speaker runs the MongoDB shell from there. *When:* Inspecting a running container's state (such as database contents) without kubectl exec.
- **Command mode and filtering** — Press colon and type a resource name (for example deploy, then accept autocomplete) to switch views. Press slash and type text to filter the current list. Use the at symbol to switch context. *When:* Navigating between resource types and clusters without remembering kubectl get syntax.
- **Custom aliases and config** — Press Ctrl+A to list aliases, or type alias in command mode. Custom aliases are added to the aliases file in K9s's config directory (the speaker does not show the exact path). The main config file controls mouse mode, logoless mode, no-icons mode, and the skin. Restart K9s after changing the skin. *When:* Adding short commands for resources you open often, such as a custom alias for a long resource name, and tuning the look for a terminal.
- **Enable image vulnerability scans (preview)** — Turn on the image-scan option in the K9s config file (it is false by default). Scores are displayed per resource. Press V to view vulnerabilities, and press Enter on one to open it in the browser. Expect slow loading because the feature is in preview. *When:* A quick first look at image vulnerabilities inside the cluster view. The speaker treats it as experimental.

## Numbers
- Video length is 4:45. ([0:00](https://youtu.be/AMUQzyPvO04?t=0))
- Image-scan vulnerability score is shown as a 5-position vector. The feature is a preview and is off by default. ([3:42](https://youtu.be/AMUQzyPvO04?t=222))
- Example image change to 8.0.5 is applied immediately and confirmed with describe. ([2:48](https://youtu.be/AMUQzyPvO04?t=168))
- Cluster has 6 namespaces, but only 3 namespace shortcuts appear until more namespaces are visited. ([1:24](https://youtu.be/AMUQzyPvO04?t=84))

## Hot takes
- K9s is said to be the better choice for general cluster management, but kubectl is still needed for applying manifest directories.
- The image-scan feature is labelled a preview and is off by default, with slow loading noted at recording time.
- No sponsor segment. The title's 'BEST' is a superlative with little comparative evidence, so the content is a feature tour rather than a benchmark.

## Tools mentioned
K9s, kubectl, Kubernetes metrics server, MongoDB shell, Tokyo Night skin (community variant, linked in the video description), Dracula skin (from the official K9s skins repo)
