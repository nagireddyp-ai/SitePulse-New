export const dashboardMetrics = {
  mttr: 42,
  slaBreaches: 2,
  ticketVolume: 128,
  agentActions: 312,
};

export const incidentStatus = [
  { name: "Open", value: 18 },
  { name: "In Progress", value: 12 },
  { name: "Resolved", value: 34 },
];

export const slaTrend = [
  { name: "Mon", breaches: 1, resolved: 8 },
  { name: "Tue", breaches: 0, resolved: 12 },
  { name: "Wed", breaches: 2, resolved: 10 },
  { name: "Thu", breaches: 1, resolved: 14 },
  { name: "Fri", breaches: 0, resolved: 18 },
];

export const resolutionTimes = [
  { name: "Network", minutes: 35 },
  { name: "Storage", minutes: 52 },
  { name: "Linux", minutes: 44 },
  { name: "Access", minutes: 28 },
];

export const kbArticles = [
  {
    id: "KB-3001",
    title: "Resolve Nginx 503 upstream timeout",
    tags: ["linux", "nginx", "P1"],
    updated: "2024-05-07",
    summary: "Inspect upstream health, validate service ports, and tune proxy_read_timeout.",
    sources: ["INC-1001"],
  },
  {
    id: "KB-3002",
    title: "Reduce disk usage on /var",
    tags: ["linux", "storage", "P2"],
    updated: "2024-05-06",
    summary: "Identify log growth, rotate logs, and clean cached packages to reclaim space.",
    sources: ["INC-1002"],
  },
];

export const chatTranscript = [
  {
    sender: "assistant",
    text: "Hi! Ask me about Linux incidents, recent logs, or KB articles.",
  },
  {
    sender: "user",
    text: "Why are nginx requests returning 503?",
  },
  {
    sender: "assistant",
    text: "Likely upstream timeout. Verify upstream service health and review nginx error logs for timeouts.",
    sources: ["KB-3001", "INC-1001"],
  },
];

export const incidents = [
  {
    id: "INC-1001",
    title: "Web server 503 errors",
    status: "Open",
    priority: "P1",
    sla: "00:45",
    owner: "Linux Ops",
  },
  {
    id: "INC-1002",
    title: "Disk space alert on /var",
    status: "In Progress",
    priority: "P2",
    sla: "02:00",
    owner: "Linux Ops",
  },
  {
    id: "INC-1003",
    title: "SSH login latency",
    status: "Resolved",
    priority: "P3",
    sla: "04:00",
    owner: "IT Support",
  },
];

export const serviceRequests = [
  {
    id: "SR-2001",
    title: "Provision new Linux VM",
    status: "Open",
    priority: "P3",
    sla: "06:00",
    owner: "Cloud Ops",
  },
  {
    id: "SR-2002",
    title: "Reset VPN credentials",
    status: "In Progress",
    priority: "P2",
    sla: "01:20",
    owner: "IT Support",
  },
];
