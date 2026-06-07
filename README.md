# Updated-Hosted-agent

> Hosted Agent — runs in Foundry Agent Service (isolated sandbox)

## Description
A Updated customer support agent that can search a knowledge base, create support tickets, track ticket status, and escalate complex issues to human agents when needed. It responds politely, provides step-by-step troubleshooting, and always confirms resolution before closing a case.

## Architecture
This agent uses the **Agent Framework** with **ResponsesHostServer** to run as a
containerized hosted agent in Foundry Agent Service. The platform manages:
- Isolated VM sandbox per session
- Automatic scaling and lifecycle
- Session state persistence
- OpenTelemetry traces and monitoring

## Quick Start (Local Testing)

```bash
# 1. Install azd and the Foundry extension
azd ext install microsoft.foundry
azd auth login

# 2. Initialize from this project
azd ai agent init

# 3. Provision Azure resources
azd provision

# 4. Test locally
azd ai agent run --no-inspector

# 5. In another terminal, invoke
azd ai agent invoke --local "Hello, I need help"
```

## Deploy to Foundry

```bash
azd deploy
```

After deployment, the agent is available at:
- **Playground**: Foundry portal → Agents → Updated-Hosted-agent → Playground
- **API**: `{project_endpoint}/agents/Updated-Hosted-agent/endpoint/protocols/openai/responses`

## Environment Variables
| Variable | Description |
|----------|-------------|
| `FOUNDRY_PROJECT_ENDPOINT` | Foundry project endpoint URL |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Model deployment name (e.g., gpt-4o) |

## Protocols
This agent uses the **Responses** protocol (OpenAI-compatible).
Any OpenAI SDK client can interact with it.

## CI/CD
The included GitHub Actions workflow deploys on push to `main` using `azd deploy`.
